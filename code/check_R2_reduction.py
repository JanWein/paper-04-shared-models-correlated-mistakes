#!/usr/bin/env python3
"""Exact R2 checks. Python standard library only. No import of manuscript code."""
from fractions import Fraction as F
from pathlib import Path
import json
from itertools import product
ROOT=Path(__file__).resolve().parents[1]

def original(n,v,ell,la,ga,g,k,h):
    A=1+la; G=1+ga; L=la-ga
    B=ell*(G+L/n); t=1/(1/v+F(k+h,1)/ell); f=F(g-k,n)
    return A*t-A*A*f*t*t/(B+t*(G+L*f))

def reduced(n,v,ell,la,ga,r,m):
    # Independent count expression, eliminating posterior t by multiplication.
    A=1+la; G=1+ga; L=la-ga; precision=1/v+F(m,1)/ell
    B=ell*(G+L/n)
    return A/precision - A*A*F(r,n)/(precision*(B*precision+G+L*F(r,n)))

def argmin(rows):
    val=min(x[0] for x in rows)
    return val,{x[1] for x in rows if x[0]==val}

def endpoints(n,r,m,d):
    K=min(m,n-r)
    return [0] if d>0 else [K] if d<0 else list(range(K+1))

counts={'parameter_cases':0,'count_pairs':0,'composition_comparisons':0,
        'original_global_designs':0,'reduced_global_pairs':0,'global_tied_cases':0}
regimes=[(F(4),F(1,5)),(F(1),F(1)),(F(0),F(2))]
noise=[(F(1),F(1)),(F(2,3),F(3,2))]
# Cost entries defined per n so one regime is exactly the equality case.
for n,(v,ell),(la,ga) in product([1,2,4],noise,regimes):
    costsets=[(F(1,2),F(3,25),F(3,10)),
              (F(1,2),F(3,25),F(1,5)),
              (F(1,2),F(3,25),F(1,2*n)+F(3,25)),
              (F(0),F(1,5),F(1,4)),
              (F(1,2),F(0),F(1,4)),
              (F(0),F(0),F(1,4))]
    for kap,cr,ce in costsets:
        counts['parameter_cases']+=1
        H=int((1+la)*v/ce); d=kap/n+cr-ce
        orig=[]; red=[]
        for g in range(n+1):
            for k in range(g+1):
                for h in range(H+1):
                    counts['original_global_designs']+=1
                    orig.append((original(n,v,ell,la,ga,g,k,h)+kap*g/n+cr*k+ce*h,(g,k,h)))
        for r in range(n+1):
            for m in range(n+H+1):
                counts['count_pairs']+=1; counts['reduced_global_pairs']+=1
                base=reduced(n,v,ell,la,ga,r,m)
                rows=[]
                for k in range(min(m,n-r)+1):
                    counts['composition_comparisons']+=1
                    g=r+k; h=m-k
                    assert original(n,v,ell,la,ga,g,k,h)==base
                    resource=kap*g/n+cr*k+ce*h
                    assert resource==kap*r/n+ce*m+d*k
                    rows.append((base+resource,k))
                val,ks=argmin(rows)
                predicted=set(endpoints(n,r,m,d))
                assert ks==predicted, (n,r,m,d,ks,predicted)
                assert val==base+kap*r/n+ce*m+min(F(0),d)*min(m,n-r)
                for k in predicted:
                    red.append((val,(r+k,k,m-k)))
        vo,so=argmin(orig); vr,sr=argmin(red)
        assert vo==vr and so==sr,(n,v,ell,la,ga,kap,cr,ce,vo,vr,so,sr)
        counts['global_tied_cases']+=len(so)>1

n=4; v=ell=F(1); la=F(4); ga=F(1,5); kap=F(1,2); cr=F(3,25)
examples=[]
for ce in [F(1,5),F(3,10),F(49,200)]:
    r=m=2; d=kap/n+cr-ce
    examples.append({'c_E':str(ce),'d':str(d),'N':r+m,'m':m,
        'J':str(reduced(n,v,ell,la,ga,r,m)),
        'optimal_k':endpoints(n,r,m,d),
        'totals':{str(k):str(original(n,v,ell,la,ga,r+k,k,m-k)+kap*(r+k)/n+cr*k+ce*(m-k)) for k in range(3)}})
ce=F(3,10); H=int((1+la)*v/ce)
value,winners=argmin([(original(n,v,ell,la,ga,g,k,h)+kap*g/n+cr*k+ce*h,(g,k,h)) for g in range(n+1) for k in range(g+1) for h in range(H+1)])
assert winners=={(4,0,1)} and value==F(1819,930)
result={'all_checks_passed':True,**counts,'arithmetic':'exact fractions, no floating tolerance',
        'composition_examples':examples,'production_example':{'minimum':str(value),'decimal':float(value),'winners':sorted(winners)},
        'scope':'finite deterministic model checks; synthetic, no empirical observations'}
(ROOT/'results'/'R2_reduction_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
