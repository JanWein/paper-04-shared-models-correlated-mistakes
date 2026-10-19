"""Exact finite global certificate. Python standard library only."""
from fractions import Fraction as F
from pathlib import Path
import csv,json
out=Path(__file__).resolve().parents[1]/'results';out.mkdir(exist_ok=True)
def J(k,h):
 t=F(1,1+k+h);f=F(4-k,4)
 return 5*t-25*f*t*t/(F(43,20)+t*(F(6,5)+F(19,5)*f))
threshold=F(95,86)+F(9,25)-F(215,186)
records=[];summ=[]
for ce in [F(3,10),threshold,F(8,25)]:
 rows=[(J(k,h)+F(3,25)*k+ce*h,k,h) for k in range(5) for h in range(13)]
 best=min(z[0] for z in rows);winners=[(k,h) for value,k,h in rows if value==best]
 assert winners==([(0,1)] if ce==F(3,10) else [(3,0)] if ce==F(8,25) else [(0,1),(3,0)])
 strict=min(value-best for value,k,h in rows if value>best)
 summ.append(dict(cE=str(ce),best=str(best),winners=winners,min_strict_gap=str(strict)))
 for value,k,h in rows:records.append(dict(cE=str(ce),k=k,h=h,J=str(J(k,h)),total=str(value),gap_to_best=str(value-best)))
with (out/'exact_certificate.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
(out/'exact_certificate.json').write_text(json.dumps(summ,indent=2));print(json.dumps(summ,indent=2))
