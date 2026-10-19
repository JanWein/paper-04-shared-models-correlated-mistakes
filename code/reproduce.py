"""R1: paid collection of operating forecasts. All examples are synthetic.
Run from any directory. No network, real data, or external service required.
"""
from pathlib import Path
from fractions import Fraction as F
import csv,json,platform
import numpy as np
import scipy
from scipy.optimize import minimize,brentq
from scipy.integrate import quad
from scipy.stats import norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
rng=np.random.default_rng(4172026)
def save(name,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def formula(n,v,l,la,ga,k,h):
 A=1+la;G=1+ga;L=la-ga;B=l*(G+L/n);t=1/(1/v+(k+h)/l);f=(n-k)/n
 C=B+t*(G+L*f);b=A*t/C if k<n else 0.
 J=A*t-A*A*f*t*t/C
 a=1-b
 cov=np.full((n,n),a*a*t)
 if k:
  cov[:k,:k]=t;cov[:k,k:]=a*t;cov[k:,:k]=a*t
 for j in range(k,n):cov[j,j]+=b*b*l
 return dict(t=t,b=b,J=J,cov=cov)

def matrices(n,v,l,la,ga,k,h):
 """Build from RAW primitive noise and original information sets.
 Does not use the posterior or analytic operating-rule derivation.
 """
 d=1+n+h;omega=np.diag([v]+[l]*(n+h));G=1+ga;L=la-ga
 Q=G/n*np.eye(n)+L/n**2*np.ones((n,n))
 obs=[]
 for i in range(k):
  row=np.zeros(d);row[0]=1;row[1+i]=-1;obs.append(row)
 for i in range(h):
  row=np.zeros(d);row[0]=1;row[1+n+i]=-1;obs.append(row)
 public=np.array(obs).reshape(k+h,d)
 infos=[]
 for j in range(n):
  if j<k:infos.append(public.copy())
  else:
   y=np.zeros(d);y[0]=-1;y[1+j]=1
   infos.append(np.vstack([public,y]))
 indices=[(j,a) for j,O in enumerate(infos) for a in range(len(O))]
 H=np.zeros((len(indices),len(indices)));g=np.zeros(len(indices));e0=np.eye(1,d,0)[0]
 for x,(i,a) in enumerate(indices):
  g[x]=Q[i].sum()*(infos[i][a]@omega@e0)
  for y,(j,b) in enumerate(indices):H[x,y]=Q[i,j]*(infos[i][a]@omega@infos[j][b])
 sol=np.linalg.solve(H,-g) if len(indices) else np.zeros(0)
 M=np.tile(e0,(n,1))
 for z,(j,a) in zip(sol,indices):M[j]+=z*infos[j][a]
 return Q,omega,infos,indices,H,g,sol,M

def analytic_M(n,v,l,la,ga,k,h):
 z=formula(n,v,l,la,ga,k,h);d=n+h+1
 Uhat=np.zeros(d);Uhat[0]=(k+h)*z['t']/l
 Uhat[1:1+k]=-z['t']/l
 Uhat[1+n:]=-z['t']/l
 R=np.eye(1,d,0)[0]-Uhat;M=np.tile(R,(n,1))
 for j in range(k,n):
  M[j]=(1-z['b'])*R;M[j,1+j]+=z['b']
 return M

def choose(n,v,l,la,ga,cr,ce):
 j0=formula(n,v,l,la,ga,0,0)['J'];bound=int(np.floor(j0/min(cr,ce)))
 choices=[]
 for m in range(bound+1):
  for k in range(min(n,m)+1):
   h=m-k;z=formula(n,v,l,la,ga,k,h)
   choices.append((z['J']+cr*k+ce*h,k,h,z))
 return min(choices,key=lambda x:(x[0],x[1]+x[2],x[1])),choices,bound

# Direct primitive covariance optimization, no exchangeability constraints imposed.
max_cov=max_cost=max_rule=0.;checks=0
cases=[(2,1,1,0,0),(4,1,1,4,.2),(4,1,1,.1,5),(3,1,1,2,2),(1,1,1,0,0)]
for _ in range(90):
 cases.append((int(rng.integers(2,8)),10**rng.uniform(-2,1),10**rng.uniform(-2,1),float(rng.uniform(0,8)),float(rng.uniform(0,8))))
for n,v,l,la,ga in cases:
 for k,h in [(0,0),(0,2),(n,0),(n,2),(min(1,n),1),(max(n-1,0),0)]:
  z=formula(n,v,l,la,ga,k,h)
  Q,O,infos,indices,H,g,sol,M=matrices(n,v,l,la,ga,k,h)
  cv=M@O@M.T;j=np.trace(Q@cv);ma=analytic_M(n,v,l,la,ga,k,h)
  max_cov=max(max_cov,np.max(abs(cv-z['cov'])));max_cost=max(max_cost,abs(j-z['J']));max_rule=max(max_rule,np.max(abs(M-ma)))
  assert np.allclose(cv,z['cov'],atol=1e-8,rtol=1e-8)
  assert np.allclose(M,ma,atol=1e-8,rtol=1e-8)
  assert abs(j-z['J'])<1e-8
  assert 0<=z['b']<1 or k==n
  # Solve the raw quadratic again using a numerical optimizer in 12 small cases.
  if checks<12 and len(sol):
   fit=minimize(lambda x:x@H@x+2*g@x,x0=np.zeros(len(sol)),jac=lambda x:2*(H@x+g),method='BFGS',options={'gtol':1e-10})
   assert abs(fit.fun-(sol@H@sol+2*g@sol))<1e-8
  checks+=1
# Posterior joint covariance via Schur complement, independent of scalar formula.
posterior_gap=0.
for k,h in [(1,0),(3,0),(2,2),(4,1)]:
 n=4;v=l=1.;d=n+h+1;O=np.eye(d);rows=[]
 for j in list(range(1,1+k))+list(range(1+n,1+n+h)):
  row=np.zeros(d);row[0]=1;row[j]=-1;rows.append(row)
 Hobs=np.array(rows);P=O-O@Hobs.T@np.linalg.solve(Hobs@O@Hobs.T,Hobs@O)
 t=1/(1+k+h);ix=[0]+list(range(1,1+k))+list(range(1+n,1+n+h))
 posterior_gap=max(posterior_gap,np.max(abs(P[np.ix_(ix,ix)]-t)))
 assert np.allclose(P[np.ix_(ix,ix)],t)
# Exact rational policy reversal and exhaustive finite design choice.
n=4;v=l=1.;la=4.;ga=.2;cr=.12
rows=[];grids=[]
for ce in [.30,.32]:
 best,choices,bound=choose(n,v,l,la,ga,cr,ce)
 for total,k,h,z in choices:grids.append(dict(external_cost=ce,k=k,h=h,posterior_variance=z['t'],private_weight=z['b'],operating_loss=z['J'],collection_cost=cr*k+ce*h,total=total))
 rows.append(dict(external_cost=ce,k=best[1],h=best[2],operating_loss=best[3]['J'],total=best[0],enumeration_bound=bound))
assert (rows[0]['k'],rows[0]['h'])==(0,1)
assert (rows[1]['k'],rows[1]['h'])==(3,0)
save('optimal_designs.csv',rows);save('enumerated_designs.csv',grids)
threshold=F(95,86)+F(9,25)-F(215,186)
# Exact proof by enumerating all candidates whose costs could beat no collection,
# at the tie and both nearby rational costs. Fractions avoid floating-point ties.
def exact_J(k,h):
 t=F(1,1+k+h);f=F(4-k,4);A=F(5);B=F(43,20);G=F(6,5);L=F(19,5)
 return A*t-A*A*f*t*t/(B+t*(G+L*f))
exact_rows=[]
for ce in [F(3,10),threshold,F(8,25)]:
 candidates=[(exact_J(k,h)+F(3,25)*k+ce*h,k,h) for k in range(5) for h in range(13)]
 lowest=min(r[0] for r in candidates);winners=[(k,h) for val,k,h in candidates if val==lowest]
 exact_rows.append(dict(external_cost=str(ce),total=str(lowest),winners=winners))
assert exact_rows[1]['winners']==[(0,1),(3,0)]
# Fixed-total composition curvature and stationary candidate vs exhaustive integer search.
composition_checks=0
for _ in range(500):
 nn=int(rng.integers(2,20));m=int(rng.integers(0,20));vv,ll=10**rng.uniform(-1,1,2);aa=float(rng.uniform(0,8));gg=float(rng.uniform(0,8));rr,ee=rng.uniform(.01,.3,2)
 A=1+aa;G=1+gg;L=aa-gg;B=ll*(G+L/nn);t=1/(1/vv+m/ll);C=B+G*t;kmax=min(nn,m)
 vals=[formula(nn,vv,ll,aa,gg,k,m-k)['J']+rr*k+ee*(m-k) for k in range(kmax+1)]
 candidates={0,kmax}
 if L>0 and ee>rr:
  kc=np.clip(nn*(1+C/(L*t)-A/L*np.sqrt(C/(nn*(ee-rr)))),0,kmax)
  candidates|={int(np.floor(kc)),int(np.ceil(kc))}
 assert abs(min(vals[k] for k in candidates)-min(vals))<1e-8
 composition_checks+=1
# Stress comparison: freeze GAUSSIAN-derived rules, evaluate same costs directly.
# U = eta + shift*(Z-p); same unconditional v=1. No mixture-posterior claim.
p=.05;q=.2;shift=np.sqrt((v-q)/(p*(1-p)));K=.5;alpha=.975;delta=4.;ce=.30
policies=[('no_collection',0,0),('fresh_one',0,1),('reuse_three',3,0),('full_pooling',4,0)]
stress=[];mc=[];max_tail_error=0.
for name,k,h in policies:
 z=formula(n,v,l,la,ga,k,h);M=analytic_M(n,v,l,la,ga,k,h);Q,Om,*_=matrices(n,v,l,la,ga,k,h);w=np.ones(n)/n;c=w@M
 tau2=c[0]**2*q+l*np.sum(c[1:]**2);sd=np.sqrt(tau2);mus=c[0]*shift*(np.array([0,1])-p);ps=np.array([1-p,p])
 cdf=lambda x:np.sum(ps*norm.cdf((x-mus)/sd))
 quant=brentq(lambda x:cdf(x)-alpha,float(mus.min()-15*sd-1),float(mus.max()+15*sd+1))
 def trunc(hh):
  zz=(hh-mus)/sd;d=mus-K
  return float(np.sum(ps*((d*d+sd*sd)*norm.sf(zz)+sd*(2*d+sd*zz)*norm.pdf(zz))))
 eh=trunc(K);es=trunc(max(K,quant))/(1-alpha)
 integ=sum(prob*quad(lambda x:(x-K)**2*norm.pdf((x-mu)/sd)/sd,max(K,quant),np.inf)[0] for prob,mu in zip(ps,mus))/(1-alpha)
 max_tail_error=max(max_tail_error,abs(integ-es));assert abs(integ-es)<1e-7
 cost=cr*k+ce*h
 stress.append(dict(policy=name,k=k,h=h,posterior_t_Gaussian=z['t'],private_weight_unsampled=z['b'],J=z['J'],collection_cost=cost,total_quadratic=z['J']+cost,aggregate_variance=float(w@z['cov']@w),expected_capacity_loss=eh,capacity_ES=es,capacity_adjusted_total=z['J']+cost+delta*eh))
 # Monte Carlo error covariance and SAME full loss map.
 N=240000;prim=rng.normal(0,np.sqrt(l),(N,1+n+h));prim[:,0]=rng.normal(0,np.sqrt(q),N)+shift*(rng.binomial(1,p,N)-p)
 errors=prim@M.T;cv=np.cov(errors,rowvar=False);quadloss=np.einsum('ij,jk,ik->i',errors,Q,errors);ss=errors.mean(1);cap=np.maximum(ss-K,0)**2
 for metric,sample,target in [('J',quadloss,z['J']),('capacity_loss',cap,eh)]:
  se=sample.std(ddof=1)/np.sqrt(N);mean=sample.mean();assert abs(mean-target)<7*se+.0002
  mc.append(dict(policy=name,metric=metric,analytic=target,MC=mean,MC_SE=se))
 assert np.max(abs(cv-z['cov']))<.035
save('same_cost_map_stress.csv',stress);save('MC_validation.csv',mc)
# The wrong independent-diagnostic formula selects reuse incorrectly.
wrong=[]
for k in range(5):wrong.append((formula(n,v,l,la,ga,0,k)['J']+cr*k,k))
wrong_best=min(wrong)
# Figures.
fig,axs=plt.subplots(1,2,figsize=(10,3.7))
for mode in ['reuse','fresh']:
 vals=[formula(n,v,l,la,ga,j if mode=='reuse' else 0,j if mode=='fresh' else 0)['J'] for j in range(5)]
 axs[0].plot(range(5),vals,marker='o',label=mode)
axs[0].legend();axs[0].set_xlabel('Collected signals');axs[0].set_ylabel('Optimized operating loss')
for name,k,h in policies:
 if name in ['reuse_three','fresh_one']:axs[1].plot(range(1,n+1),np.diag(formula(n,v,l,la,ga,k,h)['cov']),marker='o',label=name.replace('_',' '))
axs[1].set_xlabel('Unit index (reuse reporters: 1-3)');axs[1].set_ylabel('Unit error variance');axs[1].legend()
for ax in axs:ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(OUT/'collection_roles.pdf');fig.savefig(OUT/'collection_roles.png',dpi=170);plt.close(fig)
# A cost frontier shows global choices, not a hand-picked local comparison.
front=[]
for ec in np.linspace(.26,.35,91):
 best,_,_=choose(n,v,l,la,ga,cr,float(ec));front.append(dict(cE=float(ec),k=best[1],h=best[2],total=best[0]))
save('cost_frontier.csv',front)
summary=dict(seed=4172026,matrix_cases=checks,max_covariance_error=max_cov,max_welfare_error=max_cost,max_rule_error=max_rule,max_joint_posterior_error=posterior_gap,composition_checks=composition_checks,max_ES_quadrature_error=max_tail_error,exact_reversal_threshold=str(threshold),threshold_decimal=float(threshold),exact_choices=exact_rows,wrong_independent_formula_reuse_choice=wrong_best,python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,matplotlib=matplotlib.__version__,all_checks_passed=True)
(OUT/'validation.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))

# Endogenous production extension. g acquired operating sources, k reported;
# n-g units only have public information. h fresh public diagnostic sources.
def production(n,v,l,la,ga,g,k,h):
 A=1+la;G=1+ga;L=la-ga;B=l*(G+L/n);t=1/(1/v+(k+h)/l);f=(g-k)/n
 C=B+t*(G+L*f);b=A*t/C if g>k else 0.;J=A*t-A*A*f*t*t/C
 a=np.ones(n);a[k:g]=1-b;cov=t*np.outer(a,a)
 for j in range(k,g):cov[j,j]+=b*b*l
 return dict(t=t,b=b,J=J,cov=cov)

def raw_production(n,v,l,la,ga,g,k,h):
 d=1+n+h;omega=np.diag([v]+[l]*(n+h));Q=(1+ga)/n*np.eye(n)+(la-ga)/n**2*np.ones((n,n));pub=[]
 for j in list(range(1,1+k))+list(range(1+n,1+n+h)):
  row=np.zeros(d);row[0]=1;row[j]=-1;pub.append(row)
 pub=np.array(pub).reshape(k+h,d);infos=[]
 for j in range(n):
  if k<=j<g:
   row=np.zeros(d);row[0]=-1;row[1+j]=1;infos.append(np.vstack([pub,row]))
  else:infos.append(pub.copy())
 idx=[(j,a) for j,obs in enumerate(infos) for a in range(len(obs))];H=np.zeros((len(idx),len(idx)));grad=np.zeros(len(idx));e0=np.eye(1,d,0)[0]
 for x,(j,a) in enumerate(idx):
  grad[x]=Q[j].sum()*(infos[j][a]@omega@e0)
  for y,(i,b) in enumerate(idx):H[x,y]=Q[j,i]*(infos[j][a]@omega@infos[i][b])
 sol=np.linalg.solve(H,-grad) if len(idx) else np.zeros(0);M=np.tile(e0,(n,1))
 for z,(j,a) in zip(sol,idx):M[j]+=z*infos[j][a]
 return M@omega@M.T,float(np.trace(Q@M@omega@M.T))
prod_gap=0.
for nn in [1,2,4]:
 for gg in range(nn+1):
  for kk in range(gg+1):
   for hh in [0,1,2]:
    for aa,ga in [(0,0),(4,.2),(.1,5),(2,2),(30,0)]:
     z=production(nn,1,1,aa,ga,gg,kk,hh);cv,cost=raw_production(nn,1,1,aa,ga,gg,kk,hh)
     prod_gap=max(prod_gap,np.max(abs(cv-z['cov'])),abs(cost-z['J']))
     assert np.allclose(cv,z['cov'],atol=1e-9);assert abs(cost-z['J'])<1e-9
# Production procurement comparison: all costs real and counted once.
n=4;la=4.;ga=.2;kap=.5;cr=.12;ce=.30;v=l=1.
prows=[]
for g in range(n+1):
 for k in range(g+1):
  for h in range(int(np.floor((1+la)*v/ce))+1):
   z=production(n,v,l,la,ga,g,k,h);cost=kap*g/n+cr*k+ce*h
   prows.append(dict(g=g,k=k,h=h,private_weight=z['b'],J=z['J'],production_cost=kap*g/n,report_cost=cr*k,external_cost=ce*h,total=z['J']+cost))
save('endogenous_production.csv',prows)
pbest=min(prows,key=lambda x:x['total'])
# Voluntary acquisition: local scores and a binary verifiable source cost.
# delta(v)=v^2/(v+l); optimal private posterior when acquired.
def effort_outcome(v,kap,n=4,l=1,la=4,ga=.2):
 delta=v*v/(v+l);acq=delta>kap;b=v/(v+l) if acq else 0.;a=1-b
 mse=a*a*v+b*b*l;agg=a*a*v+b*b*l/n;disp=mse-agg
 resource=kap if acq else 0.
 return dict(v=v,private_gain=delta,acquisition=int(acq),J=mse+la*agg+ga*disp,real_cost=resource,total=mse+la*agg+ga*disp+resource)
erows=[effort_outcome(v,kap) for v in [1.001,1.000001,.999999,.999,.95]]
save('voluntary_acquisition.csv',erows)
v0=(kap+np.sqrt(kap*kap+4*kap))/2;b0=v0/(v0+1);disp0=b0*b0*(1-1/n);jump=la*kap+(la-ga)*disp0
assert abs(v0-1)<1e-12;assert abs(jump-2.7125)<1e-12
prod_summary=dict(max_direct_matrix_error=prod_gap,global_production_design=pbest,voluntary_threshold=v0,welfare_jump_at_improvement=jump,diagnostic_first_source_gain=(1+la)*v*v/(v+l),diagnostic_source_cost=ce)
(OUT/'production_validation.json').write_text(json.dumps(prod_summary,indent=2));print(json.dumps(prod_summary,indent=2))

# Independently check the reuse-premium algebra against optimized covariance costs.
premium_gap=0.
for nn in [2,4,6]:
 for total in [1,2,4]:
  for kk in range(1,min(nn,total)+1):
   aa,gg=4.,.2;A=1+aa;G=1+gg;L=aa-gg;B=1*(G+L/nn);t=1/(1+total);f=1-kk/nn;C=B+G*t
   premium=A*A*t*t*C*(kk/nn)/((C+L*t*f)*(B+A*t))
   Q,O,*_,M=matrices(nn,1,1,aa,gg,kk,total-kk)
   raw_reuse=np.trace(Q@M@O@M.T)
   Q,O,*_,M=matrices(nn,1,1,aa,gg,0,total)
   raw_fresh=np.trace(Q@M@O@M.T)
   premium_gap=max(premium_gap,abs(premium-(raw_reuse-raw_fresh)))
   assert abs(premium-(raw_reuse-raw_fresh))<1e-10
# Private acquisition outcome independently evaluated from raw primitive covariance.
private_gap=0.
for vv in [.25,.999999,1.000001,2.]:
 z=effort_outcome(vv,.5);bb=vv/(vv+1) if z['acquisition'] else 0.
 M=np.zeros((4,5));M[:,0]=1-bb
 for j in range(4):M[j,j+1]=bb
 Q=1.2/4*np.eye(4)+3.8/16*np.ones((4,4));O=np.diag([vv]+[1]*4)
 val=np.trace(Q@M@O@M.T)+.5*z['acquisition']
 private_gap=max(private_gap,abs(val-z['total']));assert abs(val-z['total'])<1e-10
extra=dict(max_reuse_premium_matrix_error=premium_gap,max_voluntary_acquisition_matrix_error=private_gap,passed=True)
(OUT/'extra_validation.json').write_text(json.dumps(extra,indent=2));print(json.dumps(extra,indent=2))
