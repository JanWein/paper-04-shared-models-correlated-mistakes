---
abstract: |
  A challenge report need not contain independently produced information. We solve a two-source implementation problem with hidden production, costly observation, bounded payments and provenance audits. The operating objective combines local error, aggregate mismatch and coordination loss. Unaudited accuracy rewards induce copying; selective audits can induce low-cost production while nonproducers fabricate opposition. Optimizing the stated contract and report-use menu yields a strict coordination-dependent switch from targeted use with partial production to pooled use with uniform audits and full production. A broader bounded-payment result excludes full production under unaudited outcome-only contracts at the witness. Complete incentive constraints and exact synthetic checks support the result. The contribution is restricted implementation and information architecture, not unrestricted contract optimality.
author:
- Dr. Jan-Hendrik Weinert
date: 19 October 2026
title: "Shared Models, Correlated Mistakes: Hidden Production and Provenance Audits"
---

**Keywords:** organizational information design; information acquisition; forecast reuse; hidden production; provenance audits; coordination; information contracts.

# 1. Introduction

A firm adopting a shared forecasting system has at least two ways to improve it. It can collect forecasts already produced by operating units, or it can commission new assessments. The distinction is easily lost when both are summarized by the precision of headquarters' corrected forecast. Yet an existing operating forecast is already influencing a local decision. Communicating it changes who knows it; purchasing a fresh source changes the information available to the organization. Equal precision at the center need not imply equal economic value across these designs.

This paper solves that distinction in a finite Gaussian team. Headquarters can pay to report any number of operating forecasts and can buy new independent observations of the same target. Complete pooling is feasible and explicitly priced. Operating decisions minimize local error, convex aggregate mismatch, and real coordination costs. The model also allows headquarters to choose how many operating sources to produce in the first place. The resulting design problem has a finite global solution, rather than a comparison that excludes ordinary pooling by assumption.

A collected operating signal remains statistically independent of other primitive source noises, but the public posterior residual is correlated with that unit's raw local error. Treating it as an external diagnostic observation double-counts information. Once the local signal is public, it carries no residual private innovation for its reporting unit. That unit should use the public posterior. A unit whose forecast was not collected retains a nonzero adjustment based on its private innovation. The earlier uniform-rule result therefore becomes a two-role result when information sets differ endogenously.

The contractible benchmark has a useful equivalence. If $N=g+h$ is the total number of distinct observations and $m=k+h$ the public count, optimized Gaussian operating loss depends on $(N,m)$ alone. The reuse label has no additional effect. Endogenous contractible production then reduces composition to an affine endpoint choice. These valid results are retained, but they do not supply the paper's additional economic mechanism.

The implementation extension asks what survives when report delivery cannot certify source production. A forecaster sees a common forecast and can buy a distinct but less accurate observation. Paying only for an accurate binary report rewards copying the stronger common signal. Provenance audits can instead reward production and faithful raw-source reporting, but selective checking opens a different deviation: a nonproducer can invent opposition to avoid checking. Headquarters must incorporate this behavior into both the report likelihood and the operating architecture.

We solve a finite class with two bonus levels, an incremental-information score, two positive audit rates, uniform or agreement-only audits, and targeted or pooled report use by two operating controllers. There are only two primitive sources and one strategic supplier with two cost types. The supplier can reject, copy, fabricate, randomize, or acquire and selectively misreport. The exact optimal design changes with the real cost of coordinating the controllers: increasing that cost can raise both the fraction of genuine independent production and the audit rate while expanding report use. All supplier incentives are strict on either side of the demonstrated switch. Cost-boundary and architecture ties are separately characterized.

The fixed-information solution method, ensembling, generic acquisition incentives and report-sensitive checking are established. The bounded increment is the joint implementation switch when origin is hidden, a weaker but informative source must be reported faithfully, selective checks change the direction of fabrication, and report distribution affects organizational coordination. We solve that adjacent constraint rather than claim general originality for auditing or scoring rules. Stronger technologies, arbitrary payment schedules and unrestricted communication remain outside the result.

# 2. Closest results and priority boundaries

Hedden and Raghavan (2026), *Algorithmic Monoculture and Its Critics*, is the closest conceptual competitor. We checked the publisher's published PDF, especially Section 4.1, pages 6-8, and its conclusion. It explicitly explains ensemble replication and recognizes the cost of collecting dispersed assessments. We therefore claim neither the possibility of a uniform ensemble nor the observation that collecting information is costly. The count-equivalent procurement menu is a retained benchmark. Section 8 adds a restricted hidden-production implementation problem; it does not attribute a new ensemble principle to that extension. Their published article first appeared on 25 September 2026; the April arXiv version is a distinct earlier version.

The closest mathematical predecessor located is Afshari and Mahajan (2017), *Static Teams with Common Information*. Their Theorem 1 supplies optimal Gaussian rules with common and local observations; Section 3 studies distributed estimation. Our fixed-information action problem falls within that framework. The linearity and common-information method are inherited. Theorem 1 below is an explicit specialization of their Theorem 1, not an independent fixed-information contribution. The further source-selection problem prices production and communication. The count equivalence and affine composition reduction describe that particular endogenous menu; they do not imply a new fixed-information solution method. We do not claim a new theorem establishing affine optimality for general static teams.

Radner (1962) is the foundational team-decision reference. Morris and Shin (2007) study precision versus common understanding in communication; their published model has a real disagreement cost. Colombo, Femminis, and Pavan (2014) study information acquisition and the welfare consequences of public information. The possibility that public information changes private information production is therefore established. Our binary acquisition calculation isolates its resource implication for the present cost map; the generic crowding-out mechanism is not novel. Crowding out and the count reduction are secondary benchmarks; the additional implementation comparison is in Section 8.

The closest contracting precedents are more demanding comparators for the extension. Papireddygari and Waggoner (2022), Section 2.1 and Proposition 1, map acquisition and hidden-action contracting to scoring rules. The incentive constraints here specialize standard expected-utility comparisons; an accuracy bonus for one raw bit is deliberately a restricted report space, not a new proper scoring rule. Their EC 2022 publication is distinguished from the inspected June 2022 arXiv revision. Clark and Reggiani's inspected 2021 working paper characterizes information-acquisition contracts with liability limits; it supplies a broader contracting perspective, not our finite architecture classification.

Zarkoob, Fu, and Leyton-Brown's final AAMAS 2020 article already optimizes report-sensitive spot checking with costly signals and reporting deviations. Its first page explicitly supersedes the 2019 extended abstract. Gao, Wright, and Leyton-Brown (2019) likewise study information effort and checking against trusted evaluations; we inspected the publisher record and the 2020 proceedings extended abstract, not an unverified replacement for the journal text. Wang, An, and Jiang (2018) already combine heterogeneous effort incentives, checking and aggregation, with observable effort under a check. Neither report-dependent auditing nor verified effort is claimed new here.

Cacciamani, Castiglioni, and Gatti's ICLR 2024 work jointly optimizes acquisition, elicitation and decisions. The final proceedings record is verified; the inspected full formal text is its July 2023 preprint, including Section 2's effort/report deviation constraints. Our contract problem maps to that general principal-agent logic after adding an audit outcome to the observable event. The added finite object is the coordination-driven choice of a costly report-use channel when an available common source is stronger than the raw source and fabricated opposition is possible. We do not infer that a general algorithmic framework cannot encode this example, or claim an unstudied general audit mechanism. The source ledger specifies inspected versions and the exact scope of this bounded comparison.

Bates and Granger (1969) and Rice (1978) are background for forecast combination and quadratic information value. The earlier symmetric uniform-weight and external-assessment-count formulas are retained only as benchmarks in Appendix A. They are not the article's primary novelty claim.

The current economic competitors also matter. Sheng's July 2026 working paper, inspected in author-hosted full text, models common lineage and cross-bank costs not fully priced by financing contracts. We internalize the modeled operating costs inside one organization and choose the source and reporting architecture. Kleinberg and Raghavan (2021) and the April 2026 working paper by Robert Kleinberg, Sinanaj, and Tardos study ranking and matching externalities. Ballestero et al. (2026) study human and LLM coordination games. These are not estimates of our procurement mechanism. The two 2026 papers in that sentence retain working-paper status rather than being silently upgraded to publications.

Yang's SSRN record, *Accurate but Correlated*, is dated 17 August 2026, posted 19 August. The accessible record and abstract discuss aggregate forecast covariance and market volatility. Full-text retrieval remains blocked, so its formal-results comparison remains unresolved. We make no priority claim against uninspected results. The separate source ledger records exact links, versions, sections inspected, and access limits.

# 3. Organization, information production, and feasible collection

## 3.1 Target, primitive sources, and timing

Condition on a shared forecast $s$, interpreted as a public reference level. The unknown normalized target is $\theta=s-U$, where $U\sim N(0,v)$ and $v>0$. The prior is proper conditional on $s$; no improper prior is needed. Unit $j$ can acquire a source yielding $x_j=\theta+\epsilon_j$, where $\epsilon_j\sim N(0,\ell)$ and $\ell>0$. A fresh diagnostic source yields $z_h=\theta+\nu_h$ with the same variance for the main comparison. All primitive source noises and $U$ are mutually independent.

The source is an observation technology, such as a separately purchased survey or data inspection, not an assessor's claimed independence. Production requires a costly, verifiable source operation. Its result is locked before the common forecast is displayed to the producer. Conditional independence is a technological assumption about distinct observations of the same target. Locking and blinding prevent replacement by the displayed common output; they do not eliminate a shared blind spot in the source technology.

Headquarters chooses a set of $g$ operating sources to produce, collects $k\leq g$ of those forecasts, and can produce and collect $h\geq0$ fresh diagnostic sources. By symmetry relabel the reporters $1,\ldots,k$ and the acquiring nonreporters $k+1,\ldots,g$. Other units have only public information. Existing-forecast collection is the special case $g=n$, where production costs have already been incurred and are sunk for the collection comparison.

The timing is: commit to source and reporting choices and payments; acquire and lock selected observations; report the paid subset; broadcast the common information; choose all operating actions simultaneously; observe the target and settle losses. Communication costs are paid before action. Late forecasts cannot diagnose the same decision episode in this model. Acquisition and collection are selected ex ante, not adaptively after inspecting unusually favorable reports.

Public information $\mathcal C$ includes $s$, the selected identities, and

$$D_i=s-x_i=U-\epsilon_i\quad(i\leq k),\qquad
E_a=s-z_a=U-\nu_a\quad(1\leq a\leq h). \tag{1}$$

Each nonreporting acquiring unit also observes its own $x_j$. Reporters' local forecasts are already in $\mathcal C$. Paying to collect all $n$ forecasts is feasible; ordinary pooling is not prohibited.

A common broadcast infrastructure is already present. Its fixed cost is common across the compared designs and omitted. The per-report cost $c_R$ includes extracting, validating, transmitting, and returning usable information in time. The external price $c_E$ includes producing a genuinely new source and communicating it. If broadcast capacity, privacy, or source delays differ by design, their incremental costs must be added; they are not presumed zero in applications.

## 3.2 Loss and resource costs

Let $d_j$ be action, $e_j=d_j-\theta$, $S=n^{-1}\sum_j e_j$, and $\bar d=n^{-1}\sum d_j$. The operating loss is

$$\mathcal L=\frac1n\sum_j e_j^2+\lambda S^2+
\frac\gamma n\sum_j(d_j-\bar d)^2,\qquad\lambda,\gamma\geq0. \tag{2}$$

Local mistakes require adjustment; aggregate mismatch strains a shared resource; dispersed plans incur real coordination costs. All units share the normalized target after known local offsets are removed. A capacity loss $(S-K)_+^2$ is evaluated separately under an explicit additional cost coefficient in Section 9.

Write $A=1+\lambda$, $G=1+\gamma$, $L=\lambda-\gamma$, and

$$B=\ell\left(G+\frac{L}{n}\right)>0,\qquad
Q=\frac Gn I+\frac L{n^2}\mathbf1\mathbf1'. \tag{3}$$

Then $\mathcal L=e'Qe$. Its eigenvalues are $G/n$ on the disagreement subspace and $A/n$ on the common subspace, so it is strictly convex even if $L<0$.

Producing an operating source uses resources $\kappa/n$ in the normalized objective. The factor $1/n$ reflects the normalization of local losses; $\kappa$ is the source's unit-level cost. The total resource objective is

$$W(g,k,h)=J(g,k,h)+\kappa g/n+c_R k+c_E h,\quad
J=E[\mathcal L]. \tag{4}$$

The source-production stage can be implemented by a procurement contract for a verifiable observation operation with known reservation cost. A supplier with utility payment minus cost accepts at payment equal to cost, with a stated accept-at-indifference convention. No unmodeled independence bonus or unobservable effort is assumed enforceable. Transfers reimburse the resource cost; they are not counted a second time. If neither production nor provenance can be verified, this implementation fails and a moral-hazard mechanism would be needed. The separate voluntary-acquisition benchmark below does not assume such a procurement contract.

# 4. Posterior dependence and optimal operating roles

## 4.1 Joint posterior, not an independent-diagnostic substitution

**Lemma 1 (source overlap).** Let $m=k+h$ denote the number of public observations and

$$t_m=\left(v^{-1}+m/\ell\right)^{-1},\qquad
\widehat U=\frac{t_m}{\ell}\left(\sum_{i=1}^kD_i+\sum_{a=1}^hE_a\right),
\qquad \widehat\theta=s-\widehat U. \tag{5}$$

The residual $R=\widehat\theta-\theta=U-\widehat U$ is independent of $\mathcal C$ and has variance $t_m$. For each reporting operating unit,

$$\operatorname{Cov}(R,\epsilon_i)=t_m,\qquad
E[\epsilon_i\mid\mathcal C]=\widehat U-D_i. \tag{6}$$

Conditional on $\mathcal C$, the residuals of $U$, all reporting $\epsilon_i$, and all reported external $\nu_a$ are the *same* random variable $R$. Their joint conditional covariance block is $t_m\mathbf1\mathbf1'$. Nonreporters' unreported source noises retain variance $\ell$ and are independent of this block.

*Proof.* The Gaussian likelihood is proportional to $\exp[-\{U^2/v+\sum(D_i-U)^2/\ell+\sum(E_a-U)^2/\ell\}/2]$. Completing the square gives (5) and posterior variance $t_m$. Gaussian posterior residuals are independent of the observations. Since $\epsilon_i=U-D_i$, subtracting its conditional mean leaves $U-\widehat U=R$. The same identity holds for external source residuals. Unreported primitive noises do not enter the likelihood. Finally $\operatorname{Cov}(R,\epsilon_i)=E[\operatorname{Cov}(R,\epsilon_i\mid\mathcal C)]=t_m$. $\square$

The posterior variance in (5) equals the variance obtained from $m$ fresh sources, but the joint error structure differs. Reporting does not destroy information. It changes whether a later local adjustment contains a new observation. Equating (5) with an independent residual at every operating unit would use the wrong joint posterior.

## 4.2 A solved team problem

Set $r=g-k$ and $f=r/n$. When $r>0$, define

$$C_f=B+t_m(G+Lf),\qquad b_f=\frac{At_m}{C_f}. \tag{7}$$

**Theorem 1 (two operating roles).** Among all square-integrable decision rules adapted to the stated information sets, the unique optimal actions, up to almost-sure equality, are

$$d_i=\widehat\theta\quad(i\leq k\text{ or }i>g),$$ $$d_j=\widehat\theta+b_f(x_j-\widehat\theta)
\quad(k<j\leq g). \tag{8}$$

For $r=0$ all actions equal $\widehat\theta$. The optimized operating loss is

$$J(g,k,h)=At_m-\frac{A^2 f t_m^2}{B+t_m(G+Lf)}. \tag{9}$$

When all operating sources exist, $g=n$, the nonreporters' weight simplifies to

$$b_{k,h}=\frac{Av}{B+v(A+kG+h B/\ell)},\quad k<n, \tag{10}$$

and lies strictly between zero and one. Reporters have zero additional local weight. In the general source-production problem $b_f$ may exceed one; it is a valid team-optimal response that partly offsets public-only units' aggregate exposure, not a convex-combination restriction silently imposed on (8).

*Proof.* Condition on $\mathcal C$ and center actions at $\widehat\theta$. Nonreporting acquired innovations are $y_j=x_j-\widehat\theta=\epsilon_j-R$. They satisfy $\operatorname{Var}(y_j)=\ell+t_m$, $\operatorname{Cov}(y_i,y_j)=t_m$ for distinct private units, and $E[R\mid y_j]=-t_m y_j/(\ell+t_m)$. A public-only unit has no residual innovation after conditioning.

The first-order condition for any unit with information $\mathcal I_j$ is

$$E[Ge_j+LS\mid\mathcal I_j]=0. \tag{11}$$

For a public-only unit, the proposed rule has conditional mean error and conditional mean aggregate error both zero, satisfying (11). For a private unit under (8),

$$E[e_j\mid y_j]=\left(b-\frac{t_m}{\ell+t_m}\right)y_j,$$ $$E[S\mid y_j]=\left[-\frac{t_m}{\ell+t_m}
+\frac b n\left\{1+\frac{(r-1)t_m}{\ell+t_m}\right\}\right]y_j.$$

Substitution into (11) yields $b\{B+t_m(G+Lf)\}=At_m$, proving (7). These first-order conditions suffice globally: for any square-integrable admissible perturbation $z_j$, measurability and (11) make $E[z'Qe]=0$. The excess expected loss is exactly $E[z'Qz]\geq0$, strictly positive for a nonzero perturbation since $Q$ is positive definite. Thus the result is not restricted to linear candidate rules.

Under (8), average marginal error is $t_m(1-2fb+fb^2)+f\ell b^2$ and aggregate second moment is $t_m(1-fb)^2+f\ell b^2/n$. Subtracting gives dispersion. Combining terms in (2) gives $At_m-2Af t_m b+fC_fb^2$; minimizing proves (9). For $g=n$, substitute $f=1-k/n$ and (5) into (7) to obtain (10). Its denominator exceeds its numerator by $B+kvG+hvB/\ell>0$. $\square$

A reporter does not ignore its forecast: that forecast already enters $\widehat\theta$. Repeating it as if independent is the error. With $k=0$ and $g=n$, every unit has the same role and the uniform blending benchmark is recovered. For $0<k<n$, equal primitive source quality no longer implies equal optimal rules because reporting creates unequal information sets.

## 4.3 Complete error covariance

**Corollary 1.** Let $P$ be the public-only units and $N$ the acquired nonreporters. With $a=1-b_f$,

$$\operatorname{Cov}(e_i,e_j)=
\begin{cases}
t_m,&i,j\in P,\\
a t_m,&i\in P,j\in N\text{ or conversely},\\
a^2t_m+\ell b_f^2\mathbf1\{i=j\},&i,j\in N.
\end{cases} \tag{12}$$

All errors have unconditional mean zero. The aggregate variance is

$$V_S=t_m(1-fb_f)^2+\frac{f\ell b_f^2}{n}. \tag{13}$$

*Proof.* Public-only errors equal $R$. Private-unit errors equal $aR+b_f\epsilon_j$, where the unreported $\epsilon_j$ are independent of $R$ and each other. Expanding products yields (12); summing with weights $1/n$ yields (13). $\square$

Equation (12) is not obtained by declaring the corrected forecast independent of reporting units' old signals. The full posterior block in Lemma 1 explains why those old signals no longer supply a private adjustment. When $b_f>1$, some public-private error covariances are negative. This can hedge aggregate mismatch, but is not claimed to arise under unequal exposure or in real firms.

# 5. Information-count equivalence and exact procurement

## 5.1 The same information stock has the same operating value

**Theorem 2 (information-count equivalence).** Define $N=g+h$, $m=k+h$, and $r=N-m=g-k$. For every feasible source design,

$$J(g,k,h)=\overline J(r,m)
=At_m-\frac{A^2(r/n)t_m^2}{B+t_m\{G+L(r/n)\}}. \tag{C1}$$

Consequently any two designs with the same $(N,m)$ have the same optimized operating loss. Their optimal error covariance matrices agree up to permutation of units. Neither the reuse label nor $k$ separately enters the operating optimum. Costs can differ.

*Proof.* The equalities defining $r,m$ substituted into (9) prove (C1). For a direct information-set argument, the public experiment contains $m$ distinct conditionally independent equal-noise observations of the target. Exactly $r$ units possess one additional distinct private observation each; the other $n-r$ units have only public information. A reporter's old observation is already public and supplies no additional innovation. A nonacquiring unit has the same public information as a reporter. Relabeling the public primitive noises and permuting the $r$ private units therefore gives the same joint distribution of all payoff-relevant information sets. Equation (7) gives the same private weight, and (12) gives the same covariance after that permutation. When $m=0$ or $r=0$ the corresponding block is empty, so the argument includes both boundaries. $\square$

This is equivalence of optimized operating experiments, not equality of physical source assignments or expenditures. It relies on equal precision, independent primitive noises, symmetric exposure and costs, and the stated public release before action. No unequal-exposure or correlated-source version is asserted.

## 5.2 Fixed-production collection compares different information stocks

For the collection problem with all operating sources already produced, write $J_R(k,h)=J(n,k,h)$. Fix $m=k+h$, let $t=t_m$, $f=1-k/n$, and $C=B+Gt$.

**Proposition 2 (fixed-production premium and curvature).** The operating-loss premium for reporting $k$ operating forecasts instead of acquiring $m$ fresh public observations is

$$\Delta_{k,m}=J_R(k,m-k)-J_R(0,m)
=\frac{A^2t^2 C(k/n)}{(C+Ltf)(B+At)}. \tag{14}$$

It is strictly positive for $k>0$. Reuse is cheaper in total at fixed $m$ if and only if

$$k(c_E-c_R)>\Delta_{k,m}. \tag{15}$$

In a continuous relaxation of $k\in[0,\min(n,m)]$, the operating loss is increasing in $k$ and has curvature with the sign of $L=\lambda-\gamma$. For $L>0$ and $\delta_c=c_E-c_R>0$, its cost-adjusted minimizer is the projection of

$$k^c=n\left[1+\frac C{Lt}-\frac A L\sqrt{\frac C{n\delta_c}}\right] \tag{16}$$

onto that interval. The integer optimum is among the floor and ceiling of the projected point. If $L\leq0$, an endpoint minimizes the cost-adjusted criterion, except possible ties; if $\delta_c\leq0$, fresh information ($k=0$) weakly dominates reuse at fixed $m$.

*Proof.* From (9), subtract the case $f=1$. The numerator after combining fractions is $C(1-f)$, giving (14), and adding the cost difference gives (15). Derivatives with respect to $k$ are

$$\frac{dJ_R}{dk}=\frac{A^2t^2C}{n(C+Ltf)^2}>0,\qquad
\frac{d^2J_R}{dk^2}=\frac{2A^2t^3CL}{n^2(C+Ltf)^3}. \tag{17}$$

All denominators are positive since $B>0$ and $G+Lf$ is between $A$ and $G$. Subtract $\delta_c$ from the first derivative and solve for zero to obtain (16). Convexity gives the nearest-integer rule when $L>0$; concavity or linearity gives endpoints when $L\leq0$. For $\delta_c\leq0$, both the operating and cost changes favor zero reuse. $\square$

In (14), the first organization has $N=n+m-k$ distinct observations, whereas the fresh-source comparator has $N=n+m$. Both have $m$ public observations. The premium thus compares different total primitive information stocks. For designs holding both $N$ and $m$ fixed, Theorem 2 instead gives zero operating-loss difference. It is an opportunity cost of not adding a new observation under fixed operating production, not an intrinsic penalty for sharing the same information. It is not a claim that sharing makes the organization worse than keeping the *same* observation private. Indeed, more common information weakly improves the optimum when costs are ignored: headquarters can instruct units to retain the previous mapping if necessary.

## 5.3 Finite bounds for both procurement menus

**Proposition 3 (finite search bounds).** For $c_R,c_E>0$ and $g=n$ with source-production costs sunk, a global minimizer of $J_R(k,h)+c_Rk+c_Eh$ exists. It can be found by examining only

$$0\leq m\leq \left\lfloor\frac{J_R(0,0)}{\min(c_R,c_E)}\right\rfloor,
\quad 0\leq k\leq\min(n,m),\quad h=m-k. \tag{18}$$

At each $m$, Proposition 2 reduces the composition search to at most two candidates or endpoints. Complete pooling is the feasible point $(k,h)=(n,0)$ with

$$J_R(n,0)+nc_R=A\left(v^{-1}+n/\ell\right)^{-1}+nc_R. \tag{19}$$

For endogenous production, $\kappa\geq0$, $c_R\geq0$, and $c_E>0$, a global minimizer of (4) is found by examining $0\leq g\leq n$, $0\leq k\leq g$, and

$$0\leq h\leq\left\lfloor Av/c_E\right\rfloor. \tag{20}$$

*Proof.* Zero collection costs $J_R(0,0)$ in the first problem. Any candidate with more total observations than (18) has collection costs alone exceeding that benchmark and cannot improve it, since operating loss is nonnegative. There are finitely many remaining points. Equation (19) follows from $f=0$. In the production problem, doing nothing has loss $Av$. A design with $hc_E>Av$ cannot improve it, irrespective of its other nonnegative costs. There are finitely many remaining $(g,k,h)$, each with solved operating loss (9), proving (20). $\square$

The collection search includes hybrid designs. Proposition 2 conditions on $g=n$ and fixed $m$; its curvature reflects the changing private count $r=n-k$. The endogenous-production reduction below instead holds $r,m$ fixed, so its composition problem has zero curvature.

## 5.4 Endogenous production: an endpoint rule and a two-count search

**Theorem 3 (exact procurement reduction, including ties).** Assume $v,\ell>0$, $\kappa,c_R\geq0$, and $c_E>0$. For integers $0\leq r\leq n$, $m\geq0$, let

$$K(r,m)=\min(m,n-r),\qquad d=\kappa/n+c_R-c_E. \tag{C2}$$

Every feasible design with those counts has the unique representation

$$g=r+k,\quad h=m-k,\quad k\in\{0,\ldots,K(r,m)\},$$ $$W=\overline J(r,m)+\kappa r/n+c_E m+dk. \tag{C3}$$

At fixed counts the complete minimizing set is

$$\mathcal K^*(r,m)=
\begin{cases}
\{0\},&d>0,\\
\{K(r,m)\},&d<0,\\
\{0,1,\ldots,K(r,m)\},&d=0.
\end{cases} \tag{C4}$$

For $K=0$ these sets coincide. Thus global procurement minimizes

$$V(r,m)=\overline J(r,m)+\kappa r/n+c_E m
+\min(0,d)K(r,m) \tag{C5}$$

over $r=0,\ldots,n$ and $m=0,\ldots,n+\lfloor Av/c_E\rfloor$. Every globally optimal original design is recovered from every minimizing pair and every $k\in\mathcal K^*(r,m)$ by (C3); there are no other global minimizers. If $c_* =\min(c_E,\kappa/n+c_R)>0$, the additional bound $m\leq\lfloor Av/c_*\rfloor$ can tighten the search.

*Proof.* For any original design $r=g-k\geq0$ and $m=k+h\geq0$. The restrictions $h\geq0$ and $g\leq n$ give $k\leq m$ and $k\leq n-r$. Conversely each integer in that interval gives a feasible original design, proving the parametrization. Theorem 2 makes its operating loss constant. Substituting $g=r+k$ and $h=m-k$ into (4) gives (C3). Minimizing this affine expression on consecutive integers gives (C4), including every equality case, and its minimum is (C5).

Doing nothing has value $Av$. Nonnegativity of operating loss and all original cost components means any globally minimizing original design has $h\leq H=\lfloor Av/c_E\rfloor$. Since $k\leq n$, it also has $m=k+h\leq n+H$. Hence no global minimizer lies outside the stated finite reduced domain. The domain may contain endpoint reconstructions with $h>H$; these have cost alone exceeding $Av$ and cannot minimize it. For each pair the endpoint procedure is exact on the original untruncated feasible interval. Its minimum is no greater than the feasible no-source value, so every reduced minimizer is a global original minimizer. Conversely a global original minimizer must minimize composition at its own counts, otherwise changing $k$ would strictly improve it, and must minimize the reduced criterion. This proves the complete correspondence, not only equality of minimum values. Finally original costs equal $\kappa r/n+(\kappa/n+c_R)k+c_Eh\geq c_*m$; when $c_*>0$ the sharper bound follows. The universal bound remains valid when internal production and reporting are both free. $\square$

The sign test compares the full public-source resource price $\kappa/n+c_R$ with $c_E$. If internal public production is cheaper, its capacity $n-r$ is filled before buying external observations; if dearer, no internal public sources are produced at those counts. At equality, intermediate compositions are genuinely tied. This is a conditional endpoint statement: the optimizing private count $r$ itself can leave no internal-public capacity, so cheaper internal reporting does not by itself imply positive reporting in the global optimum.

For a synthetic composition illustration, hold $n=4,r=m=2$, $v=\ell=1$, $\lambda=4$, $\gamma=.2$, $\kappa=.5$, and $c_R=.12$. All $k=0,1,2$ have $N=4$ and identical operating loss. At $c_E=.20$ the unique cost-minimizing composition is $k=0$; at $.30$ it is $k=2$; at $.245$ all three tie. These are fixed-count comparisons, not claims that $(r,m)=(2,2)$ globally wins at those prices.

# 6. An exact policy reversal

The following is an illustrative finite economy, not a calibration. Let $n=4$, $v=\ell=1$, $\lambda=4$, $\gamma=1/5$, and $c_R=3/25$. Then $A=5$, $G=6/5$, $B=43/20$, and $J_R(0,0)=215/143$.

At $c_E=3/10$, the global optimum is one fresh source and no operating reports:

$$W_F=J_R(0,1)+3/10=215/186+3/10=677/465.$$

The best reuse-only design reports three forecasts, costs

$$W_R=J_R(3,0)+9/25=95/86+9/25=3149/2150,$$

and is strictly worse. Complete pooling costs $1+12/25=37/25$, also worse. Thus a fresh source costing 2.5 times as much per report wins after total operating losses and costs are included.

At $c_E=8/25$, the global optimum changes to three operating reports and no fresh source. Reporters use $\widehat\theta$; the fourth unit uses private weight $20/43$. This is a two-role optimum even though units were initially identical. The two procurement modes tie at

$$c_E^*=95/86+9/25-215/186=30866/99975. \tag{21}$$

A finite exact certificate checks all $k=0,\ldots,4$ and $h=0,\ldots,12$ at these three rational costs. Counts with $h\geq13$ cost at least $13(3/10)>J_R(0,0)$; they cannot win. At (21) the only ties are $(0,1)$ and $(3,0)$. Because every candidate cost is affine in $c_E$, inequalities at the endpoints and at (21) establish the stated switch throughout $c_E\in[.30,.32]$, not only at three isolated points. The executable certificate uses rational arithmetic, not a dense numerical sweep. Appendix C gives the verification inequalities and code formulation.

The erroneous independent-diagnostic calculation would replace $J_R(k,0)$ by $J_R(0,k)$. It selects three reused reports with claimed total cost $215/272+9/25\approx1.15044$, rather than their actual cost $1.46465$. At $c_E=.30$, that error reverses the procurement recommendation. The discrepancy is not a rounding issue or a tail extrapolation. It results from counting the local information twice.

A further implication is that posterior precision alone fails to rank the designs. Three reused reports give $t=1/4$, while one fresh report gives $t=1/2$. Despite the more precise public posterior, the former has higher aggregate error variance (.20876 versus .17915) under its optimal operating rules and higher total cost at $c_E=.30$.

Table 1. Synthetic collection comparison at $c_E=.30$. Source-production costs are sunk; policies have different $(N,m)$.

::: center
  Policy                   $k$   $h$       $J$   $J+c_Rk+c_Eh$
  ---------------------- ----- ----- --------- ---------------
  No collection              0     0   1.50350         1.50350
  One fresh source           0     1   1.15591         1.45591
  Three reused reports       3     0   1.10465         1.46465
  Full pooling               4     0   1.00000         1.48000
:::

![Synthetic operating loss and role-dependent marginal errors. These are exact Gaussian-model calculations at fixed operating production, with total information changing across source compositions, not observed organizational outcomes.](results/collection_roles.pdf){width="100%" height="\\textheight"}

# 7. Endogenous independent-source production

## 7.1 Voluntary acquisition and the limits of disclosure timing

Consider a decentralized benchmark in which each operating unit maximizes a local forecasting score, equivalent to minimizing its own expected squared error plus acquisition cost $\kappa$. No unit observes anyone else's source, and there is no reporting. A unit can use the shared forecast without cost, or acquire its independent observation. The shared output is used at the action stage in both cases. The purpose of this benchmark is to identify the acquisition incentive, not to pretend that decentralized scores implement the organization's entire loss function.

**Proposition 4 (acquisition exit).** A unit acquires if and only if

$$\delta(v)=\frac{v^2}{v+\ell}>\kappa. \tag{22}$$

Its action when acquiring is $d_j=s+b_v(x_j-s)$, where $b_v=v/(v+\ell)$. At strict inequalities acquisition choices form the unique equilibrium because no unit's private score depends on another's acquisition. The threshold variance is

$$v_0=\frac{\kappa+\sqrt{\kappa^2+4\kappa\ell}}2. \tag{23}$$

At the threshold, moving from the all-acquire limit to the no-acquisition limit raises the normalized organizational resource objective if and only if

$$\lambda\kappa+(\lambda-\gamma)D_0>0,\qquad
D_0=\frac{v_0^2\ell}{(v_0+\ell)^2}(1-1/n). \tag{24}$$

The jump equals the expression in (24). Thus a marginal improvement of the common model can cause an upward resource-loss jump through voluntary acquisition exit, although common-model improvement with a fixed information technology is beneficial.

*Proof.* Without acquisition, local MSE is $v$. With an acquired Gaussian observation it is $v\ell/(v+\ell)$, so the gain is (22), strictly increasing in $v$. Solving $\delta(v_0)=\kappa$ yields (23). At the threshold, local MSE plus real acquisition cost is $v_0$ under acquisition. Let $D_0$ be cross-unit decision dispersion. Aggregate MSE under acquisition is its marginal MSE minus $D_0$, and the no-acquisition aggregate MSE is $v_0$. Their difference is $\kappa+D_0$. Therefore no-acquisition loss minus acquisition loss, including the normalized cost $\kappa$, is $\lambda(\kappa+D_0)-\gamma D_0$, proving (24). Continuity of each branch gives the one-sided jump. $\square$

This crowding-out result is derived from Bayesian value of information and a discrete acquisition choice, not imposed as a behavioral decline in effort. Its generic mechanism is already present in information-acquisition economics; it serves here as a procurement motivation. Continuous divisible precision could smooth the jump and is outside the binary model.

A disclosure-timing qualification is essential. Since the posterior variance $v$ is independent of the realized Gaussian shared forecast, deciding before rather than after seeing its value does not change (22) if both policies release the forecast before action. Mere blinding has no acquisition-incentive effect in this benchmark. It matters for source provenance and for preventing a supposedly new observation from actually being a copied output. Any additional anchoring or timing effect would require a different production technology and evidence.

## 7.2 Paying for information instead of assuming it survives

The procurement problem (4), solved by Theorems 1-3, chooses $g$ as well as $k,h$. It can pay for operating sources that voluntary local scores would not produce. It can instead purchase a fresh blinded diagnostic source, or pool all produced operating sources at cost $nc_R$. A truly external diagnostician has no local decision that can privately finance its acquisition; its source and reporting costs must therefore be paid explicitly through $c_E$.

An elementary but useful threshold is exact. Starting with no acquired operating sources and no diagnostic source, purchasing one fresh public source and making all units use the public posterior is worthwhile if

$$c_E<A\{v-t_1\}=A\frac{v^2}{v+\ell}. \tag{25}$$

This is a sufficient comparison to doing nothing, not a claim that one source is globally optimal. Its aggregate value can remain large when private local acquisition fails (22). The complete comparison with local production and pooling uses (C5), so no ordinary collection option is omitted.

For $n=4$, $\ell=v=1$, $\lambda=4$, $\gamma=.2$, and $\kappa=.5$, the voluntary threshold is $v_0=1$. Immediately above it, all units acquire; immediately below it, none acquire. The resource-loss jump is $2.7125$ in the limit. At $v=1$, the acquiring branch has limiting total loss $2.2875$ and the no-acquisition branch has loss $5$. Tie-breaking at the threshold itself is immaterial to the two one-sided limits.

With $c_R=.12$, $c_E=.30$, the full source-procurement problem selects $g=4,k=0,h=1$, with total resource loss $1.95591$, including .5 for the four operating sources. A blinded-public-source-only policy ($g=k=0,h=1$) costs $2.8$. Uniform team blending with four produced local sources and no collection costs $2.00350$. Timely complete pooling costs $1.98$, including local production and all reports. This comparison both prices independence and keeps complete pooling feasible. These values are exact-model synthetic comparisons, not estimates of managerial willingness to pay.

If private acquisition is induced by an additional bonus under the *unchanged local-score rule*, a bonus of at least $\max\{0,\kappa-\delta(v)\}$ per operator suffices. That implements acquisition only for that score rule; it does not automatically implement the team-optimal weights. Our central procurement design instead contracts directly for verifiable source production and mandates the solved operating rules. We do not claim an optimal hidden-action contract. Organizational resource losses count source costs once, while bonus payments are transfers and would enter a separate owner cash-flow analysis.

# 8. Hidden production, fabricated opposition, and coordination

## 8.1 A two-source implementation problem

The Gaussian count result takes primitive production as given or contractible. Receiving a report does not establish that its producer bought a distinct observation. We now change the signal technology to a finite binary experiment, retain exactly loss (2) with $n=2$, and make production hidden. Gaussian posterior formulas are not used in this section. There are at most two primitive sources: an incumbent common source and one candidate independent source, not a larger supplier market.

The target is $\theta\in\{-1,1\}$ with equal prior probabilities. Both units and the candidate forecaster observe $C\in\{-1,1\}$, with $P(C=\theta)=q_0$. The forecaster can pay $c$ to produce $X\in\{-1,1\}$, with $P(X=\theta)=q$. Conditional on $\theta$, the source errors are independent. Assume $1/2<q<q_0<1$. A weaker source is deliberately chosen: it adds information, but on disagreement it is a worse stand-alone prediction than $C$. Indeed, $X$ never changes the posterior modal bit away from $C$; it changes confidence in that bit. Such confidence is valuable for the real-valued operating actions under squared loss even though it does not improve a binary accuracy score. The privately observed cost is $c_L$ with probability $\pi$ and $c_H$ otherwise, where $0<c_L<c_H$, $0<\pi<1$. Cost is independent of the target and all signal errors. These are two types of one strategic supplier, not two additional random sources.

The forecaster supplies one bit $R$. Without production it can copy $C$, report $-C$, use a constant, or randomize. After production it can choose any map $(C,X)\mapsto R$, including copying and selective falsification. The report includes no trusted origin field. Headquarters sees $C,R$ before decisions and $\theta$ after decisions. It does not see $c$, the production action, or the locked $X$. Equality $R=C$ is observable and is not assumed proof of copying. Conversely, the equilibrium implications of disagreement are computed, not suppressed.

The forecaster is assigned to unit 1, whose operating controller executes a committed decision map using its permitted inputs. The forecaster's hidden cost, effort choice, and private log cannot be fed directly into that controller. In the **targeted** architecture the controller of unit 1 receives $(C,R)$ and unit 2 receives $C$; in the **pooled** architecture both receive $(C,R)$ at incremental real communication capacity cost $b>0$, committed before the type draw and paid even if that episode adds no information. Headquarters commits to the optimal maps within these information sets. It cannot use its access to $R$ to send a free customized correction to unit 2. That would expand the explicitly priced architecture menu. This is an implementable restriction on channels and controllers, not a claim of optimality among every conceivable communication mechanism. The forecaster chooses reports and production, not operating actions, and receives no unmodeled share of operating gains.

A source device locks the produced bit in a tamper-resistant log inaccessible to operating controllers. An ex post provenance audit costs $d>0$ and verifies both whether the distinct source operation occurred and whether $R$ equals its locked output. A nonproducer cannot forge this log. Simply delivering a bit does not let headquarters read the log without paying for the audit. Audit results arrive after actions, so they discipline incentives but cannot repair that episode's operational information. This technology is stronger than checking agreement with another noisy evaluator; it is a stated costly origin-verification assumption. If logs were freely readable, production would be contractible and this extension would collapse to its benchmark.

Timing is: headquarters commits to a payment/audit rule and channel; the type is privately drawn; the supplier sees $C$, accepts or rejects, chooses production and locks any $X$, and sends $R$; controllers act; the committed audit lottery is executed and the target becomes observable; payment is settled. Only the audit can verify origin. Neither an eventual correct answer nor an eventual wrong answer by itself proves how the report was obtained.

## 8.2 A bounded contract class and its complete IC constraints

Let the feasible bonus grid be $\mathcal B=\{\bar w/2,\bar w\}$, with $\bar w>0$. There are fifteen posted contract options: no purchase; an unaudited flat payment $w$ for either report, for each $w\in\mathcal B$; and six scored options for each $w$: the five audit-score options (no audit, uniform audit probability $\alpha$ or $\beta$, and agreement-only audit probability $\alpha$ or $\beta$), plus the unaudited incremental-information score $P$ defined below. The latter audit $R=C$ and never audit $R\ne C$. A delivered-report option can use either operating channel, giving 29 labeled contract/channel choices including no purchase. Payments are zero, the posted bonus, or its fixed fraction $\rho$, never negative. There are no cost declarations, type-contingent menus, deposits, fines, repeated tasks, or unverifiable promises of independence in this class.

For an audit-score contract, write $a_A$ for the audit probability after agreement and $a_D$ after disagreement. The payment is

$$T=w\,\mathbf1\{R=\theta\}\,
\mathbf1\{\text{not audited, or production and faithful report verified}\}. \tag{I1}$$

Thus an audited correct guess made without production still receives zero. A produced but falsified report loses its payment when audited. The unaudited rule is an accuracy bonus for a binary report, not a strictly proper score eliciting the forecaster's entire posterior. In particular, truthful *raw source reporting* and truthful *posterior forecasting* are different tasks here.

**Theorem 4 (production and report IC).** For $w>0$, define

$$a_T=\frac{q_0-q}{(1-q)q_0},\quad
M=\max\{q_0(1-a_A),(1-q_0)(1-a_D)\},$$ $$V=q q_0+\max\{q(1-q_0),(1-a_A)(1-q)q_0\}. \tag{I2}$$

The maximal no-production payoff is $wM$. The maximal produced payoff before cost is $wV$. Production is optimal precisely when $c\leq w(V-M)$, with both production and no production optimal at equality. Conditional on production, $R=X$ is optimal precisely when $a_A\geq a_T$. It is uniquely optimal at every signal pair when $a_A>a_T$. A truthful independent report is therefore weakly implementable if and only if

$$a_A\geq a_T,\qquad c\leq w(q-M). \tag{I3}$$

Both inequalities strict give strict production and raw-report incentives. At $a_A=a_T$, a producer is indifferent between $R=X$ and $R=C$ on disagreement, and any mixture there is optimal. Without production, copying $C$ is optimal when the first argument of $M$ is larger; reporting $-C$ is optimal when the second is larger; any mixture is optimal at equality. These statements hold conditional on either common bit, so cost- or common-bit-dependent deviations are included. For the positive-audit contracts below $M>0$, participation is strict. At no purchase, rejection and zero-pay participation are equivalent for operations because headquarters ignores the report.

*Proof.* Given $C$, a nonproducer's two report payoffs are $wq_0(1-a_A)$ and $w(1-q_0)(1-a_D)$. Their maximum is $wM$; constants and random reports cannot improve on the better report at each $C$. For a producer with $X=C$, the posterior probability that the common bit is correct is $q q_0/[q q_0+(1-q)(1-q_0)]>1/2$. Truth beats reversing the bit even if the latter is never audited. On $X\ne C$, the raw source's correctness probability is $q(1-q_0)/[q(1-q_0)+(1-q)q_0]$. Reporting that bit gives its correctness probability times $w$; falsely reporting $C$ gives $1-a_A$ times the complementary probability. Comparing them gives $a_A\geq a_T$. Summing the maximizing correct-payment events gives $wV$. Subtract cost and compare with $wM$ and rejection at zero. Since $M>0$ whenever both audit probabilities are below one, participation follows. Every mixed deviation is a convex combination of these conditional pure choices. The equalities give exactly the stated best-response sets. $\square$

This exposes an often omitted deviation. Auditing only agreement makes an invented disagreement attractive once $a_A$ is large enough. The relevant copying alternative is the *maximum* in $M$, not always $C$. Also, raw-source truth requires an audit floor even as production cost tends to zero. That floor arises because the source is weaker than the already visible common forecast.

For the solved finite class impose

$$a_T<\alpha<a_S<\beta<1,\qquad
 a_S=1-\frac{1-q_0}{q_0}. \tag{I4}$$

This domain is nonempty since $q>1/2$ implies $a_T<a_S$. Every positive-audit contract then strictly elicits faithful reporting *conditional on production*. Its production cutoff, no-production report and audit load are fully explicit. Let $p_j=P(c<wD_j)$ and $C_j=E[c\mathbf1\{c<wD_j\}]$ at strict cost inequalities, and $t=P(X=C)=q q_0+(1-q)(1-q_0)$.

::: center
  Contract     $D_j=q-M$           No-production report   Expected audits
  ------------ ------------------- ---------------------- ----------------------
  $A_\alpha$   $q-(1-\alpha)q_0$   $C$                    $\alpha[1-p_j(1-t)]$
  $A_\beta$    $q+q_0-1$           $-C$                   $\beta p_jt$
  $U_\beta$    $q-(1-\beta)q_0$    $C$                    $\beta$
:::

Here $A$ denotes agreement-only audit, not the loss coefficient when used as a contract subscript. $U_\alpha$ has the same production cutoff and reports as $A_\alpha$, but audits with probability $\alpha$ unconditionally. It is strictly more costly whenever production occurs, since genuine disagreements need not be audited for this particular incentive target. With no production it is weakly dominated by no purchase. Unaudited accuracy bonuses and unaudited flat report fees induce no production for every $c>0$: the former cannot improve the most accurate binary forecast $C$, and the latter does not reward production at all. Arbitrary no-production reports under the flat rule add no information conditional on $C$.

A stronger no-audit benchmark is needed before attributing implementation to provenance checks.

**Lemma 2 (bounded unaudited incentives and a feasible incremental score).** Allow *any* menu of payments depending on $(C,R,\theta)$, including arbitrary report spaces, but no origin evidence and payments in $[0,\bar w]$. The maximal gross incentive to acquire $X$ is

$$B_0=\bar w(1-q_0)(2q-1). \tag{S1}$$

Thus a type with $c>B_0$ cannot be induced to produce by any such unaudited contract. This bound is a binary specialization of standard bounded information-elicitation logic, not claimed as a new general scoring-rule theorem.

For the additional feasible contract $P$, fix a fraction $\rho$ satisfying

$$\frac{1-q_0}{q_0}<\rho<\frac{q(1-q_0)}{(1-q)q_0}.$$

Pay $\rho w$ when $R=C=\theta$, $w$ when $R=-C=\theta$, and zero otherwise, without audits. The nonproducer strictly copies $C$; a producer strictly reports $X$ at every signal pair. Production is optimal exactly when

$$c\leq wD_P,\qquad D_P=q(1-q_0)-(1-q)q_0\rho>0. \tag{S2}$$

Equality gives the same effort mixtures as Theorem 4. Expected payments are $w\{p q[q_0\rho+1-q_0]+(1-p)q_0\rho\}$ and real audit cost is zero.

*Proof.* Conditional on $C$, label the two report/payment schedules chosen after $X=C$ and $X=-C$ as $A,D$. Let their payment difference be $d_C,d_N$ in states $\theta=C,-C$, each in $[-\bar w,\bar w]$. Set $E_A=q q_0d_C+(1-q)(1-q_0)d_N$ and $E_D=(1-q)q_0d_C+q(1-q_0)d_N$. Relative to the better prior choice between these two schedules, acquisition gain is $\min(E_A,-E_D)$. Other prior menu choices can only reduce this gain. It is at most the convex combination $(1-q)E_A+q(-E_D)=(1-2q)(1-q_0)d_N\leq B_0$. The bound is attained by schedules paying $(\bar w(1-q_0)/q_0,0)$ and $(0,\bar w)$ in those two states; their prior payoffs tie. This also covers a larger menu by retaining its chosen schedules for the two signal values. For score $P$, the stated strict bounds on $\rho$ make copying uniquely optimal without production and truthful raw reporting uniquely optimal after each source realization. The produced expected payment is $wq[q_0\rho+1-q_0]$ and the copied payment is $wq_0\rho$; subtracting proves (S2). $\square$

Score $P$ can produce genuine independent information without provenance audits. Hence an audit requirement must not be inferred from the failure of an accuracy-only bonus. In the finite optimization below, $P$ is an actual feasible option, not merely an excluded literature benchmark.

The cutoffs are ordered $0<D_{A_\alpha}<D_{A_\beta}<D_{U_\beta}$. Hence there is a region

$$wD_{A_\beta}<c_H<wD_{U_\beta} \tag{I5}$$

in which that bonus cannot induce the high type to produce under agreement-only checking, but uniform checking does. In this region, the extra disagreement audits deter invented opposition. If $c_L>\bar wD_{U_\beta}$, none of the contracts can induce independent production; all informative procurement is impossible within the class. No purchase is then resource-optimal. Unaudited flat and score payments can tie its real resource loss while wasting cash transfers, so they are not falsely labeled welfare losses from production.

## 8.3 Overlap, hidden type, and optimal report use

An unproduced report repeats or reverses a known source. It is not a distinct primitive observation. A produced report is a new draw, but headquarters does not know which type produced it before action. Thus even the distribution of genuine production is insufficient to substitute an expected source count into the Gaussian benchmark.

Write $\mu=2q_0-1$, $V_0=1-\mu^2$, and

$$\Delta=q+q_0-1-\mu t,\qquad
z_+=1-t,\quad z_-=t,$$ $$H_s(p)=\frac{p\Delta^2}{z_s(1-pz_s)},\qquad s\in\{+,-\}. \tag{I6}$$

If production occurs with probability $p$ independently of the common bit, and nonproducers report $sC$, then $H_s(p)$ is the reduction in posterior variance from observing $R$ in addition to $C$. Set $H_s(0)=0$. At $p=1$, $H_+(1)=H_-(1)=H_1>0$. For $0<p<1$, $H_s(p)<pH_1$: unobserved source origin loses information relative to the experiment in which production status is known. This is an origin-observability loss, not a violation of the fixed-information count equivalence.

**Theorem 5 (joint operating and resource value).** Retain $A=1+\lambda$, $G=1+\gamma$, now with $n=2$. Let $\eta=E[\theta\mid C,R]$. The targeted optimum over all permitted action maps is

$$d_1=\mu C+\frac{2A}{A+G}(\eta-\mu C),\qquad d_2=\mu C,$$ $$J_T=AV_0-\frac{A^2}{A+G}H_s(p). \tag{I7}$$

The pooled optimum is $d_1=d_2=\eta$ and $J_P=AV_0-AH_s(p)$. For contract $j$ at bonus $w$, set

$$R_j=C_j+d\,E[\text{audits}\mid j],$$ $$F_{j,T}=\frac{A^2}{A+G}H_{s_j}(p_j)-R_j,\qquad
F_{j,P}=AH_{s_j}(p_j)-R_j-b. \tag{I8}$$

The complete global optimum within the fifteen-option class and two operating channels is obtained by maximizing these savings and zero, retaining every tie. It suffices to compare $P,A_\alpha,A_\beta,U_\beta$ at each feasible bonus and the null/unaudited options, with the cost-tie convention below. In particular, pooling rather than targeted use of a given contract is worthwhile exactly when

$$b<\frac{AG}{A+G}H_{s_j}(p_j), \tag{I9}$$

with both channels optimal at equality. Higher coordination cost increases this pooling gain while decreasing the targeted value of the same report. It does not change the supplier's scoring incentives in (I2).

*Proof.* Conditional on $C$, set $Z=\theta C$ and $B_R=\mathbf1\{R=C\}$. Let $a=P(B_R=1)=pt+(1-p)\mathbf1\{s=+\}$ and $u=E[ZB_R]=p(q+q_0-1)+(1-p)\mu\mathbf1\{s=+\}$. Binary posterior variance reduction is $(u-\mu a)^2/[a(1-a)]$. Since $u-\mu a=p\Delta$, simplifying gives (I6). Its ratio to $pH_1$ is $(1-z_s)/(1-pz_s)<1$ for $0<p<1$.

The conditional mean of $\eta-\mu C$ given $C$ is zero and its second moment is $H_s(p)$. Public-only unit 2's conditional FOC is satisfied by $d_2=\mu C$. The FOC for unit 1 gives $(A+G)(d_1-\mu C)=2A(\eta-\mu C)$. Substituting a general multiplier $v$ into loss (2) gives $AV_0-AvH_s(p)+(A+G)v^2H_s(p)/4$, minimized at (I7). Positive definiteness of $Q$ proves global optimality over all information-adapted maps, not just symmetric candidates. With both inputs public, the conditional target mean minimizes the same loss at identical actions. Add the real production, audit and communication costs to obtain (I8). Theorem 4 exhausts report and effort deviations; $U_\alpha$ and zero-information options are dominated as stated. Each remaining contract has its solved optimal operating map. Taking their finite maximum therefore solves the whole class. Subtraction gives (I9). $\square$

Transfers are not included a second time in $R_j$. Headquarters minimizes total operating plus real production, audit and communication resource loss, including the supplier's cost. The supplier maximizes $E[T]-c\mathbf1\{\text{production}\}$. The per-episode cash payment is bounded by $\bar w$. Expected payments for the audit-score contracts are reported separately (score $P$ has the payment stated in Lemma 2):

$$E[T_j]=w\{p_jq+(1-p_j)M_j\}. \tag{I10}$$

This is a resource-welfare mandate with a payment bound, not a claim that the owner minimizing its own cash outflow chooses the same contract. Among resource ties, minimizing expected transfers is an optional stated secondary criterion.

Cost ties are not silently treated as strict effort. At $c=wD_j$ the supplier may produce with any probability, separately after each value of $C$. Suppose a tied type has cost $c_*$ and production probability can range from $p_0$ to $p_1$. Its resource cost is affine in $p$. Since

$$H_s'(p)=\frac{\Delta^2}{z_s(1-pz_s)^2},\qquad
H_s''(p)=\frac{2\Delta^2}{(1-pz_s)^3}>0, \tag{I11}$$

resource savings are convex in $p$. A welfare-best weak IC recommendation therefore uses an endpoint, so the finite maximum in (I8) checks both endpoint responses at every effort tie. Every minimizing endpoint and every contract/channel tie is retained. All intermediate supplier mixtures remain best responses even when they do not maximize welfare. The main switch below has strict supplier incentives and is unaffected by this selection issue. Appendix G also gives the worst-response calculation if a guarantee across cost-tie equilibria is required.

## 8.4 An exact coordination-driven implementation switch

The following economy is synthetic, with no empirical calibration:

$$q_0=4/5,\ q=13/20,\ \pi=1/2,\ c_L=1/50,\ c_H=11/20,$$ $$\bar w=1,\ \rho=3/10,\ \alpha=3/5,\ \beta=9/10,\ d=11/50,\ b=27/1000,\ \lambda=19. \tag{I12}$$

Here $a_T=15/28<\alpha<a_S=3/4<\beta$. The production cutoffs per unit of bonus are $D_{A_\alpha}=.33$, $D_{A_\beta}=.45$, and $D_{U_\beta}=.57$. With either bonus $.5$ or $1$, agreement-only contracts induce only the low type to produce. With uniform probability $.9$, bonus $1$ induces both types, whereas bonus $.5$ induces only the low type. All participation, effort, and report comparisons in this economy are strict. No type report is solicited; cost truthfulness is not presumed. The two types separate through hidden effort choices under the posted offer.

For $A_\beta$ the high type *does not copy $C$*. It fabricates $-C$ to avoid agreement audits. If $R=C$ in that equilibrium, production is identified; if $R\ne C$, origin is ambiguous. For $A_\alpha$ the implication is reversed: only a producer disagrees, while agreement is ambiguous. Under $U_\beta$ with bonus $1$ both types produce; nevertheless the deviations to either copied or fabricated bits are explicitly deterred. The posterior used in every operating comparison includes these implications. It never assumes that both report categories have indistinguishable origin.

For score $P$, $D_P=.046$; both bonus levels strictly induce only the low type and the high type strictly copies $C$. Here the broad unaudited bound is $B_0=.06<c_H=.55$: no alternative bounded outcome-only scoring menu can induce the high type without additional origin evidence. Its impossibility is therefore not just a consequence of the accuracy-only comparator. The low type, however, can and does produce unaudited.

**Theorem 6 (switch with full-class optimality).** In (I12), for every $\gamma\geq0$, the resource-optimal contract/channel choice is score $P$ with targeted use and either bonus when

$$0\leq\gamma<\gamma^*=\frac{196839}{335861}
\simeq .5860728099, \tag{I13}$$

and $U_\beta$ with bonus $1$ and pooled use when $\gamma>\gamma^*$. At equality those three labeled choices tie and no others do. The lower bonus $.5$ minimizes cash transfers among the two targeted resource ties. Genuine-production probability rises from $1/2$ to $1$, the expected audit rate rises from zero to $.9$, and report use expands from one controller to both. Each strict side persists in an open neighborhood of the other parameters, because the supplier incentives and policy gaps against other architectures are strict.

*Proof.* Exact evaluation of (I6) gives $t=59/100$, $V_0=16/25$, and

$$H_1=2304/60475,\quad H_+(1/2)=768/54325,\quad
H_-(1/2)=768/69325.$$

Score $P$ has real production cost $1/100$ and no audit cost, at either bonus level. $A_\alpha$ produces the same report experiment but adds positive audit cost. $A_\beta$ produces only half the time, has gain $H_-(1/2)<H_+(1/2)$, and adds positive audit cost, so it is dominated under either channel. Uniform audit with half bonus also produces only the low type, with copied reports and positive audit cost, so it is dominated by $P$. $U_\alpha$ is dominated by $A_\alpha$. The remaining full-bonus $U_\beta$ induces both types and costs $57/200+(9/10)(11/50)=483/1000$. Unaudited flat and accuracy-only contracts add no information.

Write $K=400/(21+\gamma)$. Among active targeted choices, $P$ dominates at $K=0$ and $K=400/21$, by direct substitution. Every difference is affine in $K$, proving dominance throughout the interval. The best pooled saving is the full-production option

$$P_F=20H_1-483/1000-27/1000=60951/241900>0,$$

which strictly exceeds the pooled $P$ saving and zero. The global comparison is therefore $K H_+(1/2)-1/100$ versus $P_F$. Solving their equality yields (I13). The targeted saving strictly decreases with $\gamma$, proving the ordering and all policy ties. Strict supplier comparisons and the finite remaining architecture gaps give local persistence. $\square$

At $\gamma=0$ the optimized resource loss is $12.54072118861$; expected transfers under the cash-preferred targeted contract are $263/2000=.1315$. At $\gamma=1$ the pooled full-production optimum costs $12.54803224473$ and transfers $13/20=.65$. The null and every unaudited flat fee have resource loss $12.8$; a flat fee additionally transfers its posted amount without inducing any independent observation. These figures compare endogenous procurement choices at each coordination parameter; their levels across different $\gamma$ are not a welfare experiment holding preferences fixed.

For a contractible-source benchmark, require that production status and faithful output can be verified before action at no audit cost. A posted production-contingent fee $c_L$ selects the low type; a fee $c_H$ selects both, with acceptance at indifference and the low type earning rent in the latter case. Declining the production offer is observable. The low-only experiment therefore has information gain $\pi H_1$, not $H_s(\pi)$. Its real production cost is $\pi c_L$; producing for both costs $\pi c_L+(1-\pi)c_H$. These options and no production exhaust that benchmark's type cutoffs. At the witness, the original bonus grid also implements both selections with production-contingent flat fees: $.5$ selects only the low type and $1$ selects both, with strict participation choices. Thus the reported benchmark comparison does not require a larger payment cap or finer payment grid. Applying the same channel choices and loss yields full production with pooling at $\gamma=0$, resource loss $12.35003224473$. The hidden-production pooled value exceeds this by the real audit cost $.198$. The hidden targeted design has a different source experiment as well as a different channel. We do not subtract its transfers as if they were real audit expenditure.

This is more than an audit inequality appended to an unchanged forecast comparison. Overlap changes the no-production deviation, selective auditing changes its direction, unobserved production changes the report experiment, and coordination changes the value of private versus common action inputs. Their joint optimization produces a strict architecture and implementation switch. The result is bounded by the two bonus levels, two audit protocols and two channels. The feasible score $P$ already rewards correctly reported incremental information without origin checking. Arbitrary full-posterior scoring menus, a reliable free origin signal, continuous audit optimization, strategic operating choices by the forecaster, or early audits could still overturn the finite optimum. Lemma 2 excludes full unaudited production at the witness under any bounded outcome-only menu, but it does not establish that the chosen audit rate or payment schedule is unrestrictedly optimal.

# 9. Downside exposure under the same cost map

## 9.1 What is, and is not, Gaussian

The optimal-policy results in Sections 4-7 assume Gaussian signals; Section 8 uses a separate binary experiment. To stress their deployed linear policies, hold the actions and procurement choices fixed and replace the common residual by

$$U=\eta+b(Z-p),\quad \eta\sim N(0,q),\quad
Z\sim\operatorname{Bernoulli}(p),\quad q+p(1-p)b^2=v. \tag{26}$$

The local and fresh source noises remain independent Gaussian. Formula (5) is then a deployed *Gaussian-designed linear correction*, not the true mixture posterior. Neither its residual independence nor its global Bayesian optimality is asserted under (26). The unconditional quadratic moments remain correct for those linear policies because (26) preserves $v$.

Let $\zeta=(U,\epsilon_1,\ldots,\epsilon_n,\nu_1,\ldots,\nu_h)'$ and write the deployed errors as $e=M\zeta$. The code constructs $M$ independently from both the policy formulas and raw information-set optimization. For $w=\mathbf1/n$, write $c'=w'M$. Conditional on $Z=z$,

$$S\mid Z=z\sim N(\mu_z,\tau^2),\quad
\mu_z=c_0b(z-p),\quad
\tau^2=c_0^2q+\ell\sum_{i>0}c_i^2. \tag{27}$$

Thus the capacity loss $H_K=(S-K)_+^2$ is evaluated directly. Let $q_\alpha$ solve $\sum_zp_z\Phi((q_\alpha-\mu_z)/\tau)=\alpha$ and define

$$T_z(a)=\{(\mu_z-K)^2+\tau^2\}\bar\Phi(u_z)
+\tau\{2(\mu_z-K)+\tau u_z\}\phi(u_z),\quad u_z=(a-\mu_z)/\tau.$$

Then

$$E[H_K]=\sum_zp_zT_z(K),\qquad
\operatorname{ES}_\alpha(H_K)=\frac{\sum_zp_zT_z(\max(K,q_\alpha))}{1-\alpha}. \tag{28}$$

The zero-loss atom is included when the signed-error quantile is below $K$. Appendix D proves the integration identity. Variance alone does not determine (28).

## 9.2 Completed stress comparison

The stress illustration uses the Section 6 four-unit design, $q=.2$, $p=.05$, $b=\sqrt{.8/(.05\cdot.95)}$, $K=.5$, and $\alpha=.975$. At $c_R=.12,c_E=.30$, every policy is assessed under

$$W_4=E[\mathcal L]+c_Rk+c_Eh+4E[H_{.5}]. \tag{29}$$

Operating-source production is sunk in this comparison; adding the common cost .5 when all four sources are newly procured does not change these rankings. Policy-specific external production is already in $c_E$. We do not claim that the Gaussian optimum globally minimizes (29) over all possible nonlinear mixture policies.

Table 2. Direct regime-mixture stress of the same deployed policies, costs, and $K=.5$.

::: center
  Policy                     $V_S$    $E[H]$   $\mathrm{ES}_{.975}(H)$     $W_4$
  ---------------------- --------- --------- ------------------------- ---------
  No collection            0.21268   0.03260                   0.99705   1.63388
  One fresh source         0.17915   0.01755                   0.55257   1.52610
  Three reused reports     0.20876   0.01990                   0.58891   1.54427
  Full pooling             0.20000   0.01680                   0.49719   1.54719
:::

Full pooling has the lowest displayed capacity ES but does not have the lowest displayed total cost. One fresh source has a smaller ES and lower (29) than three reused reports in this particular mixture. These are direct calculations under one stated distribution and one common cost map, across designs with differing information counts; they do not identify an intrinsic reuse effect at fixed $(N,m)$. They are not a general ES ordering, empirical evidence of fragility, or an inference from covariance alone.

# 10. Validation, empirical separation, and identification requirements

The reproduction code uses Python, with all versions and seeds recorded; R and Quarto executables were unavailable in the working environment. The manuscript is rendered with LaTeX. All new formulas were checked against raw covariance-matrix optimization using every permitted public and private signal, with neither exchangeability nor the proposed role rules imposed on that optimization.

Across 570 Gaussian cases, including no reports, all reports, fresh sources, $n=1$, $\lambda=0$, $\gamma=0$, $\lambda=\gamma$, and $\lambda<\gamma$, maximum covariance discrepancy was below $3\times10^{-15}$ and maximum welfare discrepancy below $1.3\times10^{-14}$. Joint posteriors were independently checked by Schur complements. Five hundred composition problems verified the analytic candidate rule against all integer compositions. Additional source-production cases included zero acquired units and private response weights exceeding one. No unequal-exposure optimum is claimed; only the generic weighted second-moment identity in Appendix A uses arbitrary weights.

The R2 count equivalence, affine cost identity, endpoint sets including equality, and global all-minimizer correspondence are separately checked with exact rational arithmetic against full original-variable enumeration; Appendix F reports the executable specification. The exact fixed-production source-choice reversal is also certified with rational arithmetic. Regime-mixture welfare and expected capacity loss were independently checked with 240,000 synthetic draws per displayed policy. Expected-shortfall formulas were checked by direct numerical quadrature, with error below $1.2\times10^{-13}$ in the displayed comparisons. These checks validate derivations and implementation, not the economic assumptions or novelty.

The binary extension has a separate standard-library rational checker. It enumerates all 36 plans per cost type, including common-bit-dependent effort and every produced report map. In 192 IC cases it matches both the optimal value and the entire predicted best-response set; 63 cases have multiple best plans, including effort and report ties. Ten further cases check the incremental score, including its effort ties; a separate raw-probability linear programme checks the broad unaudited incentive bound. Independently solving the raw action quadratic at every information atom gives 231 exact operating comparisons. Actual production costs, audit loads and expected transfers are also checked by direct summation over raw states and best-response plans for all 87 witness ledger rows. The 29 labeled contract/channel options are checked at the two strict switch witnesses and at the exact crossing, with all resource minimizers retained. Affine endpoint certificates prove the classification for every $\gamma\geq0$, not only the displayed witnesses. These are finite binary checks, not additional Gaussian cases or simulations.

The earlier synthetic precision exercise remains unchanged in the supplement. Its nominal Student intervals covered only 47.5% or 88.6% in some rare-shift cases, and 92.4% even with 192 independent episodes in one cell. It is a failed-method warning, not the inferential method of a completed empirical study. No proposed empirical table is populated. The unrun field protocol remains outside the article. Its R2 addendum requires measuring both total primitive and public information, rather than interpreting different information stocks as a reuse penalty.

Identification would require immutable pre-action local forecasts, the reporting subset, source-production assignments and costs, display timestamps, correction inputs, actual action weights, and realized targets. Randomized source-production and reporting assignments must record $N,m,r$ separately. Comparisons at equal $N,m$ test count equivalence; comparisons at fixed $g,m$ instead change $N$ and identify an information-stock margin. Cost variation can test the endpoint choice conditional on counts, including internal capacity $n-r$. To identify provenance rather than assessor count, data-source overlap must be measured before outcomes. Randomized communication-cost subsidies or source budgets would help identify the cost boundary, while a common model-quality change by itself would not identify the acquisition channel. Multiple independent environmental episodes remain necessary for covariance and tail claims. The hidden-production mechanism additionally requires a credible record of actual source operations, audit assignment and cost, payments, locked report contents, and whether report access was targeted or pooled. Correctness alone is insufficient to identify origin. Randomization of audit protocols must track fabricated opposition as well as ordinary copying. No such study was run.

# 11. Conclusion {#interpretation-and-remaining-scientific-limits}

The main design distinction is between adding information and changing its distribution. At fixed total and public counts, the reuse label has no operating value effect. Under fixed operating production, an external observation adds information while an internal report redistributes it, so their equal-public-precision loss difference is a stock comparison. With endogenous production, exact costs choose the composition at an endpoint or make every composition tie; only the private and public counts remain to optimize.

The initially uniform organization can therefore choose specialized roles. A reporting unit acts on the public posterior; an acquiring nonreporter retains a private correction; a unit with no acquired source uses the public posterior as well. These roles arise from the chosen information sets, not an unexplained preference for disagreement. Independence is generated by paid observations under a specified source technology, not by naming a committee.

The standard centralization dominance argument remains intact. With costless timely communication, aligned objectives, and all primitive observations available to headquarters, a center can reproduce every decentralized action map. More information cannot worsen the attainable expected-loss frontier when it can be ignored. Our welfare reversal concerns either a mistaken reuse calculation or acquisition exit under decentralized incentives, not a violation of that dominance principle. The central procurement value is weakly improved by better common information under a fixed feasible source technology: for any fixed feasible linear policy, reducing $v$ lowers its quadratic expected loss because the common-error variance enters with a nonnegative coefficient. Taking the minimum over the same policy and procurement menu preserves this monotonicity.

Material objections remain. Fixed-information rules are special cases of established Gaussian team theory, and generic acquisition crowding out is established. The count equivalence and endpoint reduction are finite consequences of symmetry. The new implementation switch is likewise restricted to a stated finite payment/audit/channel class and may still be judged too narrow for a leading economics journal. Standard moral hazard, scoring and selective checking are inherited; a general priority claim remains unsupported. Source provenance and costs are contractible in Sections 3-7. Section 8 solves hidden effort and strategic reports using an unaudited incremental score or a paid perfect ex post origin audit, with two cost types and the bounded posted-contract menu. It does not solve unverifiable origin without that technology, arbitrary cost-report menus, early audit adaptation, or strategic operating controllers. The normal-quadratic symmetry excludes many operational loss asymmetries. We do not establish robustness to arbitrary regime change, unequal exposures, correlated primitive acquisition technologies, or endogenous model training. Yang's blocked full text remains an unresolved priority check. The completed article supplies precise conditional results and a reproducible finite design solution without claiming that these objections have disappeared.

The implementation mechanism does not replace the count benchmark. Public report equality can identify origin in one equilibrium category and fail to do so in another, while a source audit verifies origin directly at a cost. A single global report count is therefore not a sufficient statistic for this hidden-production experiment. Coordination then changes whether partial production with targeted use or full production with common use justifies the required audits. The main strict switch survives arbitrary supplier tie-breaking because its supplier incentives are strict; weak effort implementation at exact cost thresholds is explicitly less robust.

# References {#references .unnumbered}

Afshari, Mohammad, and Aditya Mahajan. 2017. "Static Teams with Common Information." *IFAC-PapersOnLine* 50(1):11926-11931. DOI:10.1016/j.ifacol.2017.08.1449.

Ballestero, Gonzalo, Hadi Hosseini, Samarth Khanna, and Ran I. Shorrer. 2026. "Strategic Algorithmic Monoculture: Experimental Evidence from Coordination Games." Working paper, arXiv:2604.09502v2, 13 April.

Bates, J. M., and C. W. J. Granger. 1969. "The Combination of Forecasts." *Operational Research Quarterly* 20(4):451-468. DOI:10.1057/jors.1969.103.

Cacciamani, Federico, Matteo Castiglioni, and Nicola Gatti. 2024. "Online Information Acquisition: Hiring Multiple Agents." *ICLR 2024*. Final proceedings record verified; inspected formal text: arXiv:2307.06210v1, 12 July 2023.

Clark, Aubrey, and Giovanni Reggiani. 2021. "Contracts for Acquiring Information." Working paper, arXiv:2103.03911v1, 5 March. No later publication status established here.

Colombo, Luca, Gianluca Femminis, and Alessandro Pavan. 2014. "Information Acquisition and Welfare." *Review of Economic Studies* 81(4):1438-1483. DOI:10.1093/restud/rdu015.

Gao, Xi Alice, James R. Wright, and Kevin Leyton-Brown. 2019. "Incentivizing Evaluation with Peer Prediction and Limited Access to Ground Truth." *Artificial Intelligence* 275:618-638. Journal record and separate IJCAI 2020 extended abstract inspected.

Hedden, Brian, and Manish Raghavan. 2026. "Algorithmic Monoculture and Its Critics." *Philosophical Perspectives*, Early View, 25 September. DOI:10.1111/phpe.70018. Published text distinct from April arXiv version.

Kleinberg, Jon, and Manish Raghavan. 2021. "Algorithmic Monoculture and Social Welfare." *PNAS* 118(22):e2018340118. DOI:10.1073/pnas.2018340118.

Kleinberg, Robert, Erald Sinanaj, and Eva Tardos. 2026. "Price of Anarchy of Algorithmic Monoculture." Working paper, arXiv:2604.00444v1, 1 April; record notes WINE 2025 presentation.

Morris, Stephen, and Hyun Song Shin. 2007. "Optimal Communication." *Journal of the European Economic Association* 5(2-3):594-602. DOI:10.1162/jeea.2007.5.2-3.594.

Papireddygari, Maneesha, and Bo Waggoner. 2022. "Contracts with Information Acquisition, via Scoring Rules." *EC 2022*. DOI:10.1145/3490486.3538261. Inspected full version: arXiv:2204.01773v2, deposited 10 June, title date 13 June.

Radner, Roy. 1962. "Team Decision Problems." *Annals of Mathematical Statistics* 33(3):857-881. DOI:10.1214/aoms/1177704455. Original full text not retrieved; detailed method credited through inspected successors and a complete direct proof.

Rice, Thomas Richard. 1978. "The Value of Data for a Quadratic Decision Problem." *Management Science* 24(10):1055-1063. DOI:10.1287/mnsc.24.10.1055.

Sheng, Dalin. 2026. "Correlated Intelligence: AI Adoption and Systemic Risk." Working paper, July; SSRN 7199458 record lists 2 July.

Wang, Wanyuan, Bo An, and Yichuan Jiang. 2018. "Optimal Spot-Checking for Improving Evaluation Accuracy of Peer Grading Systems." *AAAI* 32(1):833-840. DOI:10.1609/aaai.v32i1.11336.

Yang, Fuli. 2026. "Accurate but Correlated: Common AI Forecast Errors and Endogenous Market Volatility." SSRN 7298579, written 17 August, posted 19 August. Abstract inspected; full text blocked.

Zarkoob, Hedayat, Hu Fu, and Kevin Leyton-Brown. 2020. "Report-Sensitive Spot-Checking in Peer-Grading Systems." *AAMAS 2020*:1593-1601. Final proceedings text, superseding the 2019 extended abstract. Separate 2021 arXiv revision also inspected.

Primary links, inspected sections, version distinctions, and access limits are recorded in the accompanying source ledgers. Metadata-only and abstract-only sources are not treated as inspected full texts.

# Technical appendices

## A. Aggregation identity and inherited benchmarks

For arbitrary weights $w_j$ summing to one and mean errors $\beta_j$,

$$E\left[\left(\sum_jw_je_j\right)^2\right]
=\sum_jw_j^2\operatorname{Var}(e_j)+2\sum_{i<j}w_iw_j\operatorname{Cov}(e_i,e_j)
+\left(\sum_jw_j\beta_j\right)^2.$$

Expanding the square and substituting $E[e_ie_j]=\operatorname{Cov}(e_i,e_j)+\beta_i\beta_j$ proves the identity. It neither specifies a tail distribution nor solves the unequal-exposure design problem.

With no reporting, all operating signals already produced, and rules $d_j=(1-a_j)x_j+a_js$, let $\bar a=n^{-1}\sum a_j$ and $D_a=n^{-1}\sum(a_j-\bar a)^2$. Direct expansion gives

$$J(a_1,\ldots,a_n)-\{Av\bar a^2+B(1-\bar a)^2\}
=\{Gv+B\}D_a.$$

The marginal and aggregate MSE terms use $E[a_j^2]=\bar a^2+D_a$ and $E[(1-a_j)^2]=(1-\bar a)^2+D_a$. Strict convexity gives uniform-rule dominance and $a^*=B/(B+Av)$. These are symmetric no-collection benchmarks. Theorem 1 changes the information sets through collection and therefore does not preserve that conclusion across reporters and nonreporters.

With only fresh public sources ($k=0,g=n$), (9) becomes $ABt_h/(B+At_h)$. Adding per-source cost $c_Eh$ gives the classical Gaussian information-value count problem. It is a special case of the new procurement menu, not the primary contribution.

## B. Posterior covariance and raw matrix optimization

Let $\Omega=\operatorname{diag}(v,\ell,\ldots,\ell)$ be the primitive covariance. Let $H_{\mathcal C}$ select the rows $U-\epsilon_i$ for collected operating sources and $U-\nu_a$ for external sources. The conditional covariance is independently

$$P=\Omega-\Omega H_{\mathcal C}'
(H_{\mathcal C}\Omega H_{\mathcal C}')^{-1}H_{\mathcal C}\Omega.$$

Its block on $U$ and reported source noises is $t_m\mathbf1\mathbf1'$; unreported noises retain independent variance $\ell$. Empty public matrices mean no conditioning. All-report cases contain no private innovation and are handled without inverting a nonexistent private block.

For a second solution, unit $j$ chooses an affine action relative to $s$ using the raw permitted observation rows $O_j$: every public report plus its own $x_j-s=-U+\epsilon_j$ only if acquired and unreported. Write $d_j-s=\beta_j'O_j\zeta$. Its error row is $M_j=e_0'+\beta_j'O_j$. Stack all permitted coefficients and form

$$\mathcal H_{(j,a),(i,b)}=Q_{ji}(O_j\Omega O_i')_{ab},\quad
q_{j,a}=\left(\sum_iQ_{ji}\right)(O_j\Omega e_0)_a.$$

The expected loss is $Av+2q'\beta+\beta'\mathcal H\beta$. Removing exact duplicate observation rows leaves a positive-definite coefficient Hessian. Solving $\mathcal H\beta=-q$ gives the unrestricted affine optimum; Theorem 1's measurable-policy argument establishes global optimality beyond affine rules. Directly comparing $M\Omega M'$ and $\operatorname{tr}(QM\Omega M')$ against (9) and (12) validates the scalar formulas without assuming the proposed two-role form. The code additionally minimizes the raw quadratic numerically in selected cases.

For $v=0$ the target is public, no source has value, and optimal errors vanish; positive-cost procurement is zero. For positive $v,\ell$ the main formulas apply. The limit $\ell\to0$ yields full revelation from one collected precise source but is not evaluated by a singular Gaussian inverse. No theorem assumes $Q$ is entrywise positive; its eigenvalues establish convexity even when $\lambda<\gamma$.

## C. Exact certificate for the reversal

For the rational parameters of Section 6, set $t=1/(1+k+h)$ and $f=(4-k)/4$. Then

$$J_R(k,h)=5t-\frac{25ft^2}{43/20+t(6/5+19f/5)}.$$

Let $\mathcal F=\{(k,h):0\leq k\leq4,0\leq h\leq12\}$. At $c_E=3/10$, rational evaluation verifies

$$J_R(k,h)+3k/25+3h/10\geq677/465,$$

with equality only at $(0,1)$. At $c_E=8/25$, every candidate is at least $3149/2150$, with equality only at $(3,0)$. At $c_E=30866/99975$, those two candidates tie and all other members of $\mathcal F$ are strictly worse. These are exact finite inequalities, not Monte Carlo estimates. The package contains a self-contained rational certificate, the complete numerical design ledger, and the positive gaps to all other candidates. Since $h\geq13$ already costs more than zero collection, this is a global certificate. No unexamined integer counts can alter the result at the stated costs.

## D. Capacity-loss integration proof

For $X\sim N(\mu,\tau^2)$ and $u=(a-\mu)/\tau$, normal tail integration gives $P(X>a)=\bar\Phi(u)$, $E[(X-\mu)1\{X>a\}]=\tau\phi(u)$, and $E[(X-\mu)^2 1\{X>a\}]=\tau^2\{\bar\Phi(u)+u\phi(u)\}$. Expanding $(X-K)^2$ proves $T_z(a)$. Average over the two regimes to obtain (28). Monotonicity of $(S-K)_+^2$ implies that upper-tail capacity losses correspond to $S>\max(K,q_\alpha)$; any remaining probability mass in the ES tail contributes zero. This proves the zero-atom case as well.

Capacity here concerns net signed mismatch. If resources cannot be transferred across units, aggregation would instead require a sum of local positive shortages or simultaneous exceedance counts. The present capacity formula would then be the wrong economic technology. Its applicability must be established before interpreting a fitted tail number.

## E. Information persistence and production feasibility

The same-target requirement is part of the model's feasible source set. A source produced after commitment is infeasible for that decision. If it predicts a different horizon or its common residual has correlation $r$ with the operating residual, it must not enter (5) as the same $U$. For Gaussian diagnostics of an earlier residual $U_0$ with operating residual $U_1$, both variance $v$ and correlation $r$, $m$ equal-noise measurements leave production residual variance

$$v-\frac{r^2v^2}{v+\ell/m}.$$

This follows from the conditional variance of a jointly normal pair and the noisy sample mean. Its limit is $v(1-r^2)$, so assessor count cannot remove a lack of persistence. If diagnostic noises have pairwise correlation $\rho$, their mean has variance $\ell\{\rho+(1-\rho)/m\}$; use this variance in the conditional-update formula. It has a positive floor for $\rho>0$. These are feasibility restrictions and sensitivity calculations, not endogenous claims that a particular organization can create independent or timely data at the stated prices.

The solved procurement model endogenizes whether to pay for feasible observations; it does not endogenize the physical accuracy, independence, or lead time of every possible source. Contractible source production and accurate covariance knowledge are material assumptions. A noncontractible assessor who can secretly copy the public forecast is outside the proof. Blinding is implemented by recording the source result before public display, not by assigning an assessor the title of dissenter.

## F. Exact R2 reduction checks and scope

`code/check_R2_reduction.py` is self-contained Python using rational arithmetic. It evaluates (9) in the original variables independently of (C1), enumerates every feasible composition for each tested count pair, verifies identical operating losses, checks the resource-cost identity, and compares the entire minimizing composition set with (C4). Global checks enumerate all original $(g,k,h)$ with $h\leq\lfloor Av/c_E\rfloor$ and compare both the exact minimum and every minimizing original triple with reconstructions from the reduced domain. This explicitly tests the possibly larger reduced domain, rather than silently imposing an incompatible external-source bound on each composition.

The deterministic grid includes $n=1,2,4$, three loss-weight regimes ($L>0$, $L=0$, $L<0$), two prior/noise combinations, and six cost regimes, including zero production cost, zero reporting cost, both zero, and exact price equality. It includes $r=0$, $r=n$, $m=0$, and $K=0$. The checks pass for 108 parameter cases, 4,397 count pairs, 10,014 composition comparisons, and 8,214 original global designs; 21 cases have multiple global minimizers. Results and exact synthetic composition examples are written to `results/R2_reduction_validation.json`. The previously validated raw covariance-matrix method in Appendix B is preserved; the new reduction checks test the additional algebra and discrete optimizer, not a new Gaussian optimal-policy theorem. No larger team simulation or new empirical result is introduced.

## G. Full binary implementation checks and boundary cases

The one supplier's pure plans allow effort to depend on each realized common bit. Conditional on either $C$, a no-production plan chooses either report; a production plan chooses any of the four maps from $X$ to $R$. There are six choices at each common bit and hence 36 contingent plans. Rejection adds payoff zero. In `code/provenance_contract.py`, direct summation over all $(\theta,C,X)$ computes each plan's expected payment, actual production cost, and audit-loss exposure. A separate implementation of the envelope (I2) and its conditional equality cases predicts the entire best-response set. Ten additional incremental-score cases verify both values and complete best-response sets, including its two effort ties. A raw-probability linear-program vertex check independently reproduces the broad unaudited bound $3/50$. Exact set equality is checked, including asymmetric plans on common-bit states and the report-floor equality $a_A=a_T$. Mixed best responses are precisely convex combinations of these maximizing contingent plans: expected supplier utility is linear in randomization. A positive-cost unaudited flat report contract strictly excludes production but leaves all no-production report maps indifferent. These maps reveal no additional target information conditional on $C$.

For operating validation the code creates the complete joint table $P(\theta,C,R)$, without using (I6). It assigns a free real action to every information atom of every controller, forms the full quadratic from (2), and solves its rational linear system. Positive definiteness on occupied atoms gives its unique action optimum; missing atoms do not require division by zero. This loss is compared exactly with (I7), including $p=0,1$, both no-production report directions, and $\lambda<\gamma$. No Gaussian residual independence is assumed.

For a cost type tied at a contract cutoff, all production probabilities in the indicated interval are supplier best responses, independently conditional on either common bit. Theorem 5's weak implementation criterion minimizes resource loss over those best responses. Since loss is concave in the production fraction, a minimum occurs at an endpoint. If the endpoints tie and strict curvature applies, the interior mixtures have strictly higher loss; we do not incorrectly mark them welfare ties. The score contract still weakly implements the endpoint recommendation. Strict implementation fails at the acquisition equality because declining production remains a best response. Robustness across all such cost-boundary equilibria is not claimed for the weak recommendation.

For completeness, the range of resulting Bayes operating/resource losses can also be evaluated directly. Write the resource loss on a tied interval as $AV_0-BH_s(p)+c_0+h p$, plus any communication cost, where $B=A^2/(A+G)$ or $A$. The slope of real cost is $h=c_*-d\alpha(1-t)$ for $A_\alpha$, $h=c_*+d\beta t$ for $A_\beta$, and $h=c_*$ for $U_\beta$ or the unaudited score $P$. The largest value over the interval is at its lower endpoint if $h\leq0$. If $h>0$, it is at the projection onto the interval of

$$p^{\rm worst}=\frac{1-\sqrt{B\Delta^2/(z_s h)}}{z_s}.$$

This follows by differentiating the concave loss and its strictly decreasing derivative using (I11). It describes the worst equilibrium value when action rules use that equilibrium's correct likelihood. It is not a substitute for a separate unknown-equilibrium minimax communication problem. The main strict-region result needs neither this likelihood selection nor a favorable effort tie.

The exact full-class switch certificate compares all 29 labeled choices at $\gamma=0$, $\gamma=\gamma^*$ and $\gamma=1$. It then verifies the active targeted-policy affine differences at $K=0$ and $K=400/21$ and every pooled-policy gap. These inequalities prove Theorem 6 on the whole half-line. The low-coordination resource-optimal bonus levels both remain in the returned argmin set; the optional cash criterion chooses the half bonus. At $\gamma^*$ the full-bonus pooled contract joins those two targeted contracts. The code also checks the contractible-source benchmark and the positive-cost no-production region. Output files `R3_contract_validation.json` and `R3_contract_ledger.csv` contain all reported rational values and every displayed policy comparison. These computational certificates substantiate the finite proofs, not publication priority or empirical validity.
