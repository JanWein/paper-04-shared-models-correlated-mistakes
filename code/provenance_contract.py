#!/usr/bin/env python3
"""R3 finite binary implementation model. Exact rational IC and welfare checks.
No network, private data, or nonstandard dependencies. See README for scope.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,csv
ROOT=Path(__file__).resolve().parents[1]
Q0=F(4,5); Q=F(13,20); PI=F(1,2)
CL=F(1,50); CH=F(11,20); AL=F(3,5); AH=F(9,10)
BONUSES=[F(1,2),F(1)]; STATES=[-1,1]; RHO=F(3,10)

def distribution(q0,q):
    return [(th,c,x,F(1,2)*(q0 if c==th else 1-q0)*(q if x==th else 1-q))
            for th,c,x in product(STATES,repeat=3)]

def strategies():
    # Per observed C choose no effort and one report, or effort and two reports.
    opts=[(False,(r,r)) for r in STATES]+[(True,rs) for rs in product(STATES,repeat=2)]
    return list(product(opts,repeat=2)) # 36 contingent effort/report plans
PLANS=strategies()

def raw_utility(plan,cost,w,aA,aD,q0=Q0,q=Q):
    u=F(0)
    for th,c,x,pr in distribution(q0,q):
        e,rs=plan[STATES.index(c)]; r=rs[STATES.index(x)]
        aud=aA if r==c else aD
        valid=e and r==x
        pay=w*(r==th)*(1 if valid else 1-aud)
        u+=pr*(pay-cost*e)
    return u

def best_plans(cost,w,aA,aD,q0=Q0,q=Q):
    vals=[raw_utility(s,cost,w,aA,aD,q0,q) for s in PLANS]
    best=max(F(0),max(vals))
    return best,[s for s,u in zip(PLANS,vals) if u==best]

def prediction(cost,w,aA,aD,q0=Q0,q=Q):
    # Independent scalar envelope, including below-truth-floor audits.
    V=q*q0+max(q*(1-q0),(1-aA)*(1-q)*q0)
    M=max(q0*(1-aA),(1-q0)*(1-aD))
    return max(F(0),w*V-cost,w*M)

def predicted_plans(cost,w,aA,aD,q0=Q0,q=Q):
    V=q*q0+max(q*(1-q0),(1-aA)*(1-q)*q0)
    M=max(q0*(1-aA),(1-q0)*(1-aD))
    u=max(w*V-cost,w*M)
    options=[]
    for c in STATES:
        local=[]
        if w*M==u:
            for r in STATES:
                val=w*(q0 if r==c else 1-q0)*(1-(aA if r==c else aD))
                if val==u:local.append((False,(r,r)))
        if w*V-cost==u:
            tv=q*(1-q0);fv=(1-aA)*(1-q)*q0
            for rs in product(STATES,repeat=2):
                if rs[STATES.index(c)]!=c:continue
                rr=rs[STATES.index(-c)]
                if (rr==-c and tv>=fv) or (rr==c and fv>=tv):local.append((True,rs))
        options.append(local)
    return set(product(*options))

def h_gain(p,s,q0=Q0,q=Q):
    mu=2*q0-1; t=q*q0+(1-q)*(1-q0)
    delta=q+q0-1-mu*t; z=1-t if s==1 else t
    return p*delta*delta/(z*(1-p*z))

def joint(p,s,q0=Q0,q=Q):
    # Joint distribution of payoff-relevant observables. Production flag hidden.
    out={}
    for th,c,x,pr in distribution(q0,q):
        for e,pe in [(True,p),(False,1-p)]:
            r=x if e else s*c
            out[th,c,r]=out.get((th,c,r),F(0))+pr*pe
    return {k:v for k,v in out.items() if v}

def solve_linear(H,b):
    N=len(b); A=[list(row)+[bb] for row,bb in zip(H,b)]
    for j in range(N):
        pivot=next(i for i in range(j,N) if A[i][j])
        A[j],A[pivot]=A[pivot],A[j]; z=A[j][j];A[j]=[x/z for x in A[j]]
        for i in range(N):
            if i!=j:
                z=A[i][j];A[i]=[x-z*y for x,y in zip(A[i],A[j])]
    return [row[-1] for row in A]

def raw_actions(p,s,A,G,mode,q0=Q0,q=Q):
    # Direct optimization over every decision at every raw information atom.
    P=joint(p,s,q0,q); L=A-G
    Qmat=[[G/F(2)+L/F(4),L/F(4)],[L/F(4),G/F(2)+L/F(4)]]
    def key(i,c,r): return (i,c,r if (mode=='pooled' or i==0) else 0)
    keys=sorted({key(i,c,r) for th,c,r in P for i in range(2)})
    idx={v:i for i,v in enumerate(keys)}; N=len(keys)
    H=[[F(0) for _ in keys] for _ in keys]; b=[F(0) for _ in keys]
    for (th,c,r),pr in P.items():
        for i in range(2):
            ii=idx[key(i,c,r)];b[ii]+=pr*(A/F(2))*th
            for j in range(2):H[ii][idx[key(j,c,r)]]+=pr*Qmat[i][j]
    d=solve_linear(H,b);loss=F(0)
    for (th,c,r),pr in P.items():
        e=[d[idx[key(i,c,r)]]-th for i in range(2)]
        loss+=pr*sum(Qmat[i][j]*e[i]*e[j] for i in range(2) for j in range(2))
    return loss

def contracts():
    yield ('none',F(0),F(0),F(0),'none')
    for w in BONUSES:
        yield ('flat',w,F(0),F(0),'flat')
        yield ('U0',w,F(0),F(0),'score')
        yield ('P',w,F(0),F(0),'incremental')
        for a in [AL,AH]:
            yield ('U'+str(a),w,a,a,'score')
            yield ('A'+str(a),w,a,F(0),'score')

def incremental_utility(plan,cost,w):
    u=F(0)
    for th,c,x,pr in distribution(Q0,Q):
        e,rs=plan[STATES.index(c)];r=rs[STATES.index(x)]
        u+=pr*(w*(RHO if r==c else 1)*(r==th)-cost*e)
    return u

def ledger(A,G,daudit,bcast,cl=CL,ch=CH,pi=PI):
    rows=[];V0=1-(2*Q0-1)**2
    for name,w,aA,aD,kind in contracts():
        for mode in (['targeted'] if kind=='none' else ['targeted','pooled']):
            if kind in ['none','flat']:
                p=F(0);s=1;C=F(0);aud=F(0);trans=w if kind=='flat' else F(0)
            elif kind=='incremental':
                DP=Q*(1-Q0)-(1-Q)*Q0*RHO
                el=cl<w*DP;eh=ch<w*DP
                assert cl!=w*DP and ch!=w*DP
                p=pi*el+(1-pi)*eh; C=pi*cl*el+(1-pi)*ch*eh
                s=1;aud=F(0)
                trans=w*(p*Q*(Q0*RHO+1-Q0)+(1-p)*Q0*RHO)
            else:
                # Strict witnesses; threshold ties separately checked below.
                M=max(Q0*(1-aA),(1-Q0)*(1-aD));D=Q-M
                if aA==0:p=F(0);C=F(0)
                else:
                    el=cl<w*D;eh=ch<w*D
                    assert cl!=w*D and ch!=w*D
                    p=pi*el+(1-pi)*eh;C=pi*cl*el+(1-pi)*ch*eh
                s=1 if Q0*(1-aA)>(1-Q0)*(1-aD) else -1
                t=Q*Q0+(1-Q)*(1-Q0)
                ar=p*(t*aA+(1-t)*aD)+(1-p)*(aA if s==1 else aD)
                aud=ar
                trans=w*(p*Q+(1-p)*M)
            H=h_gain(p,s);K=A if mode=='pooled' else A*A/(A+G)
            J=A*V0-K*H
            comm=bcast if mode=='pooled' else F(0)
            total=J+C+daudit*aud+comm
            rows.append(dict(contract=name,bonus=w,mode=mode,p=p,shirk_sign=s,H=H,J=J,
                             production=C,audit_rate=aud,audit_cost=daudit*aud,
                             communication=comm,transfer=trans,total=total))
    return rows

def direct_accounting(name,w,aA,aD,kind):
    prod=aud=pay=F(0)
    if kind=='none':return prod,aud,pay
    for cost,pt in [(CL,PI),(CH,1-PI)]:
        if kind=='flat':
            plan=tuple((False,(c,c)) for c in STATES)
        elif kind=='incremental':
            vals=[incremental_utility(z,cost,w) for z in PLANS]
            plans=[z for z,v in zip(PLANS,vals) if v==max(vals)]
            assert len(plans)==1
            plan=plans[0]
        else:
            _,plans=best_plans(cost,w,aA,aD)
            assert len(plans)==1
            plan=plans[0]
        for th,c,x,pr in distribution(Q0,Q):
            e,rs=plan[STATES.index(c)];r=rs[STATES.index(x)]
            ap=aA if r==c else aD
            prod+=pt*pr*cost*e;aud+=pt*pr*ap
            if kind=='flat':pay+=pt*pr*w
            elif kind=='incremental':pay+=pt*pr*w*(RHO if r==c else 1)*(r==th)
            else:pay+=pt*pr*w*(r==th)*(1 if e and r==x else 1-ap)
    return prod,aud,pay

def certify():
    count=0;ties=0
    # Full raw-plan verification, including effort ties, report ties and C-dependent plans.
    for q0,q in [(Q0,Q),(F(3,4),F(3,5))]:
        aT=(q0-q)/((1-q)*q0)
        for aA,aD,w in product([F(0),AL,AH,aT],[F(0),AL,AH],BONUSES):
            V=q*q0+max(q*(1-q0),(1-aA)*(1-q)*q0)
            M=max(q0*(1-aA),(1-q0)*(1-aD))
            costs={CL,CH,F(1),max(F(0),w*(V-M))}
            for c in costs:
                u,plans=best_plans(c,w,aA,aD,q0,q)
                assert u==prediction(c,w,aA,aD,q0,q)
                assert set(plans)==predicted_plans(c,w,aA,aD,q0,q), (c,w,aA,aD,plans)
                assert all(raw_utility(plan,c,w,aA,aD,q0,q)==u for plan in plans)
                count+=1;ties+=len(plans)>1
    incremental_cases=0
    DP=Q*(1-Q0)-(1-Q)*Q0*RHO
    for w in BONUSES:
        for cost in [CL,CH,F(1),F(0),w*DP]:
            vals=[incremental_utility(z,cost,w) for z in PLANS]
            expected=max(w*Q0*RHO,w*Q*(Q0*RHO+1-Q0)-cost)
            assert max(vals)==expected
            choices=[]
            for c in STATES:
                opts=[]
                if cost>=w*DP:opts.append((False,(c,c)))
                if cost<=w*DP:opts.append((True,tuple(STATES)))
                choices.append(opts)
            assert {z for z,u in zip(PLANS,vals) if u==expected}==set(product(*choices))
            incremental_cases+=1
    # Broader no-audit menu bound: min(EA,-ED) <= cap*(1-q0)*(2q-1).
    # Verify its attaining pair and raw IC envelope, not an assumed accuracy reward.
    bound=(1-Q0)*(2*Q-1)
    dC=(1-Q0)/Q0;dN=-F(1)
    EA=Q*Q0*dC+(1-Q)*(1-Q0)*dN
    ED=(1-Q)*Q0*dC+Q*(1-Q0)*dN
    assert EA==-ED==bound==F(3,50)
    assert CH>bound and CL<DP<F(3,50)
    # Independent LP vertex check from raw conditional state/event probabilities.
    from itertools import combinations
    ea=[F(0),F(0)];ed=[F(0),F(0)]
    for th,c,x,pr in distribution(Q0,Q):
        if c==1:(ea if x==1 else ed)[0 if th==1 else 1]+=2*pr
    constraints=[([F(1),F(0),F(0)],F(1)),([-F(1),F(0),F(0)],F(1)),
                 ([F(0),F(1),F(0)],F(1)),([F(0),-F(1),F(0)],F(1)),
                 ([-ea[0],-ea[1],F(1)],F(0)),([ed[0],ed[1],F(1)],F(0))]
    vertices=[]
    for ids in combinations(range(6),3):
        try:v=solve_linear([constraints[i][0] for i in ids],[constraints[i][1] for i in ids])
        except StopIteration:continue
        if all(sum(a*b for a,b in zip(row,v))<=rhs for row,rhs in constraints):vertices.append(v)
    assert max(v[2] for v in vertices)==bound
    matrix=0
    for p,s,A,G,mode in product([F(0),F(1,4),F(1,2),F(1)],[1,-1],
                               [F(1),F(5),F(20)],[F(1),F(3),F(25)],['targeted','pooled']):
        expected=A*(1-(2*Q0-1)**2)-(A if mode=='pooled' else A*A/(A+G))*h_gain(p,s)
        assert raw_actions(p,s,A,G,mode)==expected
        matrix+=1
    A=F(20);D=F(11,50);B=F(27,1000)
    Cm=F(1,100);Cf=F(57,200)+AH*D
    P=A*h_gain(F(1),1)-Cf-B
    gam=A*A*h_gain(PI,1)/(P+Cm)-A-1
    assert gam==F(196839,335861)
    witnesses=[];allrows=[]
    for gamma in [F(0),gam,F(1)]:
        rows=ledger(A,1+gamma,D,B);val=min(r['total'] for r in rows)
        winners=[r for r in rows if r['total']==val]
        modes={(r['contract'],r['mode']) for r in winners}
        if gamma==0:assert modes=={('P','targeted')}
        elif gamma==1:assert modes=={('U9/10','pooled')}
        else:assert modes=={('P','targeted'),('U9/10','pooled')}
        # Every row's action loss independently matches full raw information optimization.
        for r in rows:
            assert r['J']==raw_actions(r['p'],r['shirk_sign'],A,1+gamma,r['mode'])
            spec=next(c for c in contracts() if c[0]==r['contract'] and c[1]==r['bonus'])
            prod,aud,pay=direct_accounting(*spec)
            assert (prod,aud,pay)==(r['production'],r['audit_rate'],r['transfer'])
        witnesses.append({'gamma':str(gamma),'minimum':str(val),'decimal':float(val),
                          'winners':[{k:str(r[k]) for k in ['contract','bonus','mode','p','transfer']} for r in winners]})
        for r in rows: allrows.append({'gamma':str(gamma),**{k:str(v) for k,v in r.items()}})
    # Analytic all-gamma certificate: targeted incremental contract dominates all targeted
    # modes at gamma=0 and at K=0, hence throughout 0<=K<=400/21 by affinity.
    for G in [F(1),None]:
        for r in ledger(A,F(1),D,B):
            score=(A*A/(A+1) if G is not None else F(0))*r['H']-r['production']-r['audit_cost']
            if r['mode']=='targeted':
                leader=(A*A/(A+1) if G is not None else F(0))*h_gain(PI,1)-Cm
                # The null has zero cost and overtakes at K near zero; it is below
                # positive pooled leader everywhere, so exclude it here.
                if r['p']>0:assert leader>=score
    pooled=ledger(A,F(1),D,B)
    pooled_save=max(A*(1-(2*Q0-1)**2)-r['total'] for r in pooled if r['mode']=='pooled')
    assert pooled_save==P and P>0
    # Contractible-source benchmark: decline is visible, so information gain p*H(1).
    fb=[]
    for p,C in [(F(0),F(0)),(PI,PI*CL),(F(1),PI*CL+(1-PI)*CH)]:
        for mode in ['targeted','pooled']:
            K=A if mode=='pooled' else A*A/(A+1)
            total=A*(1-(2*Q0-1)**2)-K*p*h_gain(F(1),1)+C+(B if mode=='pooled' else 0)
            fb.append((total,p,mode))
    bestfb=min(fb)
    assert bestfb[1:]==(F(1),'pooled')
    # Positive-cost null region: both types above all score effort thresholds.
    nullrows=ledger(A,F(1),D,B,cl=F(3,5),ch=F(4,5))
    nv=min(r['total'] for r in nullrows);assert nv==A*F(16,25)
    assert all(r['p']==0 for r in nullrows)
    result={'all_checks_passed':True,'raw_strategy_cases':count,'strategy_count_per_type':len(PLANS),
            'cases_with_multiple_best_plans':ties,'incremental_score_IC_cases':incremental_cases,'general_no_audit_incentive_bound':str(bound),'exact_raw_team_optimizations':matrix+len(allrows),'raw_cost_audit_transfer_checks':len(allrows),
            'gamma_switch':str(gam),'gamma_switch_decimal':float(gam),'witnesses':witnesses,
            'contractible_optimum_at_gamma0':{'value':str(bestfb[0]),'decimal':float(bestfb[0]),'production_probability':str(bestfb[1]),'mode':bestfb[2]},
            'flat_report_resource_loss':str(A*F(16,25)),
            'scope':'synthetic binary model; bounded finite contract class; no empirical data'}
    out=ROOT/'results';out.mkdir(exist_ok=True)
    (out/'R3_contract_validation.json').write_text(json.dumps(result,indent=2)+'\n')
    with (out/'R3_contract_ledger.csv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=allrows[0].keys());writer.writeheader();writer.writerows(allrows)
    print(json.dumps(result,indent=2))
if __name__=='__main__':certify()
