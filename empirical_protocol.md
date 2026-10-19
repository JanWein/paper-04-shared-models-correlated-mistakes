> R3 status: prospective and unrun. The hidden-production extension requires observing actual source operations and audit assignment, not inferring independent effort from report delivery or accuracy.

> R2 status: prospective and unrun. The R2 addendum below supersedes any earlier interpretation of a reuse premium as an intrinsic sharing penalty. Comparisons must distinguish total primitive count N from public count m.

# Paper 04: prospective empirical and pre-analysis protocol

Version 2, 17 October 2026. Proposed study, not registered or conducted. No firm or operational sample has agreed to participate. All targets below are planning assumptions, not observations or commitments.

## 1. Research question and estimands before methods

Does pre-decision independent diagnostic information change forecast accuracy, shared informational mistakes, and realized organizational losses when the shared system, authority, and incentives are otherwise held fixed?

The observational unit is a location-target-origin-horizon tuple. A cell is an existing group of locations with its own operational capacity and loss ledger. An episode is a nonoverlapping decision horizon with a completed outcome. Cells are the assignment units and episodes the environmental replication units. Products within a location do not become independent units simply because they have different identifiers.

Primary policy contrast: B versus A. A has existing shared-model access and existing local-signal/override rights. B retains that same access and those rights, and adds blinded independent diagnostic forecasts plus a prespecified central correction. Do not add a new approval hierarchy to B alone. A separate shadow forecast comparison can assess a local-only rule, but this does not identify a causal effect of live adoption.

For policy z define normalized forecast errors e_jct(z) using a frozen positive pre-treatment scale. For each cell and episode define M_ct(z)=sum_j w_j e_jct(z)^2, S_ct(z)=sum_j w_j e_jct(z), and Q_ct(z)=sum_{j!=l} w_j w_l e_jct(z)e_lct(z). The weights are frozen exposure shares, not outcome-derived weights. Q is a cross second moment, not covariance unless bias is zero.

The primary estimands are the average ITT contrast in M and the contrast in the weighted off-diagonal covariance component:

C(z)=sum_{j!=l}w_jw_l {E[e_j(z)e_l(z)]-E[e_j(z)]E[e_l(z)]}.

Expectations refer to a declared target population of cells and episodes. Report the cross second-moment contrast Q separately from C. Estimate policy-specific mean errors and correct for their products; do not set them to zero merely because forecasts were intended to be unbiased. Pairwise moment estimates use independent episode blocks or a prespecified finite-sample bias correction. Heterogeneous cell composition requires within-cell estimation followed by fixed-weight aggregation rather than silently averaging changing sets of pairs.

The economic estimand is the ITT change in the actual cell loss ledger under a cost map approved before unblinding. It includes realized capacity expenditures, spoilage or overcommitment costs, coordination and delay costs, and diagnostic labor costs. If reliable costs cannot be obtained, report forecast distribution effects without a welfare conclusion. A model-implied quadratic objective is a secondary structural exercise, not a measured accounting outcome.

## 2. Feasibility gates

Before registration and assignment:

- Obtain authorized records and documented permission for analysis. No such permission is presently claimed.
- Confirm at least 24 independently assignable operational cells as an initial planning target, with at least 12 per arm, and at least 48 nonoverlapping episodes as an initial minimum planning horizon. These are feasibility screens, not an assertion of adequate power.
- Verify the independence and persistence of diagnostics using blinded pilot forecasts. Assessors must lock their own inputs before seeing the shared forecast. Shared data provenance and training histories must be recorded.
- Demonstrate that the operational budget can net the signed errors used in S. If capacity cannot move between locations, redesign the economic aggregation before assignment.
- Document simultaneous events and rollout scheduling. Adoption selected because of anticipated failures invalidates a naive rollout comparison.
- Re-simulate the actual assignment and inference procedure using blinded pilot moments, episode dependence, missingness, and regime frequencies. Proceed with confirmatory covariance claims only if familywise coverage is at least 94% in the planned stress grid and 80% power is achievable for the prespecified economically material effects below. These are planning criteria, not established guarantees.

If cells share one global capacity ledger or model retraining spreads across arms, identify that interference and randomize at a higher boundary. If only one firm-wide treated organization is available, policy switchback may be feasible only with documented washout and no persistent learning. Otherwise limit the study to descriptive forecast comparisons.

## 3. Assignment, duration, and chronology

Preferred design: matched-pair cell randomization, fixed for the evaluation period. Match on pre-treatment scale, local-signal quality, exposure mix, and baseline forecast error. Assign one cell per pair to B with recorded computer-generated randomization. Preserve allocation concealment until diagnostic staffing must be arranged. Record deviations, not just planned assignment. Do not contact or recruit anyone under the present research task.

Proposed timeline is relative, not a historical event chronology:

| Stage | Proposed timing | Required evidence |
|---|---|---|
| Eligibility and cost-map lock | Before pilot outcome inspection | Inclusion list and operational netting map |
| Blinded pilot | Before registration | Timestamped forecasts, diagnostic provenance, archived inputs |
| Registration and code freeze | Before assignment | Dated protocol, assignment seed, version hash |
| Policy allocation | Date presently unknown | Assignment file and approved deployment record |
| Access and training | Dates presently unknown | Per-unit access and training logs |
| First actual use | Dates presently unknown | Immutable forecast and action timestamps |
| Outcome closure | Fixed horizon after each origin | Target source and revision history |
| Analysis | After frozen stopping point | Locked data extract and deviations log |

Maintain a verified event ledger with event_type, cell_id, scheduled_at, observed_at, timezone, source_document_id, source_hash, model_version, rights_version, and verification_status. Distinguish announcement, access, first observed use, mandatory use, override restriction, model retraining, and system outage. No actual organizational event dates have been verified in this package.

## 4. Outcomes, multiplicity, and economic magnitudes

There are two co-primary forecast outcomes: normalized MSE and the bias-adjusted weighted covariance component. Use two-sided 5% familywise testing with Holm correction across these two contrasts. Report simultaneous uncertainty even when only one contrast is significant. Keep economic loss as a prespecified key secondary outcome and report its confidence interval without promoting it to a new primary outcome after results.

Before unblinding define economically material changes as a 10% reduction in baseline normalized MSE and a covariance increase equal to 10% of baseline aggregate second moment. These are illustrative planning thresholds subject to operational ratification before registration. Absolute thresholds avoid division by a near-zero baseline covariance. The diagnostic policy is economically favored only if expected cost inclusive of diagnostics falls under the approved cost map; significance of covariance alone is not a decision rule.

Primary horizon: one fixed operational commitment horizon, selected before data collection; candidate 28 days for a monthly planning application. All compared forecasts must have the same target, timestamp cutoff, and horizon. Use nonoverlapping episodes for primary inference. Daily overlapping forecasts are secondary and clustered appropriately.

Tail claims are secondary and conditional. Estimate observed capacity exceedance frequencies and losses. Do not estimate 97.5% ES as a confirmatory outcome from 48 episodes: the nominal tail contains approximately 1.2 observations before dependence. Any fitted regime-mixture ES is a labeled stress extrapolation with sensitivity to p, b, q, error skewness, and transferability.

## 5. Analysis and uncertainty

For additive outcomes M, Q, and accounting loss, report matched-pair treatment contrasts, baseline adjustment using only frozen covariates, and the unadjusted contrast. Randomization inference over cell assignments can test the sharp no-effect null for these outcome vectors while preserving all episode dependence. State its null precisely; it does not automatically give an exact interval for a heterogeneous average effect or nonlinear covariance functional.

For C, estimate arm-specific joint moments and marginal means over the same fixed population, and construct the contrast through their functional. Use an episode-block bootstrap or a two-way cell/episode resampling procedure justified by the pilot's dependence model, with a small-cell sensitivity analysis. Report both conditional-on-observed-episodes and superpopulation-across-episodes interpretations. The finite-sample procedure must be simulated before registration using the actual assignment; bootstrap branding is not a coverage guarantee.

Do not treat n(n-1)/2 pairs as independent observations. Pairs sharing a unit and episodes sharing an environmental shock are dependent. Cluster or resample at the documented interference and time boundaries. If independent shock episodes are too few, report identified descriptive moments and uncertainty bounds under explicit assumptions instead of a precise causal fragility conclusion.

Completed precision exercise: code/analyze.py simulates 2,000 replications each at 12, 48, and 192 independent episodes. It is paired shadow forecasting with known zero means, not the proposed randomized field design. At p=.05 its simple Student interval covers the covariance contrast only 47.5%, 88.6%, and 92.4% respectively. These failures reject the use of that interval as the final inferential procedure. Even 192 episodes do not satisfy the 94% stress-grid gate in this illustration. Additional units are no substitute for rare-regime information. A live power claim is deliberately withheld until pilot data and assignment structure exist.

## 6. Mechanisms, interference, and falsifications

Freeze pre-treatment exposure measures: regional/product mix, seasonality, supplier dependence, existing queue size, customer segments, baseline volatility, and capacity transferability. Add realized common target variables only if they are not caused by treatment. Show unadjusted results first. Exposure-adjusted residual covariance is complementary and can remove part of the very mechanism under study if adjustment is excessive.

Measure shared-model exposure through access logs, displayed forecast, actual accepted input, overrides, and the action. Model availability is an ITT treatment; actual use is a mediator. A use-on-outcome regression is not a causal dose-response unless an independent valid instrument and its assumptions are supplied. Do not use endogenous overrides as such an instrument.

Separately record decision authority, incentive schedules, staffing policies, procurement synchronization, and central approval changes. If these differ between arms, the ITT is a policy bundle. A pure model-use interpretation fails. Diagnostics trained on the same hidden bias can fail together; different names or vendors are not sufficient evidence of independent information.

Prespecified heterogeneity: baseline local-signal MSE and dependence on shared-model output, using pre-treatment measures. Limit interactions to these two and report multiplicity-adjusted secondary intervals. Shift episodes must be defined using external observables or an immutable rule set before treatment errors are examined; selecting the worst forecast periods is not a mechanism test.

Falsifications: no effects before access; no response to unavailable future model versions; no parallel discontinuity on an unrelated target without shared inputs; no impossible forecast timestamps; no unexplained change in underlying exposures before action. These tests can uncover failures but do not certify identification.

## 7. Missingness, selection, and measurement error

Eligibility is based on pre-treatment coverage. Log all closures, system outages, missing forecasts, and missing target realizations by arm. A location that fails operationally is not dropped from economic loss. Treat failures and outages as outcomes and bound missing losses under prespecified operational limits. Report complete-case estimates only as sensitivity analyses. Missing-at-random weighting must use pre-treatment and observed predictors, and its assumption must be stated.

Forecasts that can be edited after target realization are ineligible unless immutable versions exist. Underlying demand may be censored by stockouts or actions; sales are not automatically demand. Record stockout indicators and use a prespecified censored-demand model or restrict the claim to observed sales prediction. Compare against an outcome source unaffected by treatment when possible. Error in exposure weights and scales can distort aggregate risk; retain raw-unit results alongside normalized ones.

## 8. Data dictionary

| Field | Unit/type | Definition and timing |
|---|---|---|
| cell_id | String | Existing capacity/budget boundary, frozen before assignment |
| unit_id | String | Stable operating location identifier |
| target_id | String | Same forecast object across compared rules |
| origin_at, cutoff_at | UTC datetime | Forecast origin and maximum permitted input timestamp |
| horizon_end | UTC datetime | Outcome window end; primary windows nonoverlapping |
| assignment | A/B | Assigned policy, recorded before implementation |
| assignment_probability | Probability | Known from matched-pair randomization |
| shared_version | Hash/string | Immutable model, data, and feature version |
| forecast_shared | Target units | Shared prediction locked before action |
| forecast_local | Target units | Independent local assessment locked before shared output where required |
| forecast_diagnostic | Target units | Assessment from blinded diagnostic channel |
| diagnostic_id, provenance | String | Assessor/model lineage and independent input record |
| forecast_used | Target units | Input actually used for action |
| override_allowed, override_used | Boolean | Rights and realized override, stored separately |
| override_reason | Category/text | Contemporaneous reason, not retroactively inferred |
| authority_version | String | Decision-rights and approval policy |
| incentive_version | String | Compensation/target schedule |
| action | Raw resource units | Actual commitment at action_at |
| target_realized | Raw target units | Outcome source with revision status |
| target_censored | Boolean | Stockout or action-dependent observability flag |
| exposure_weight | Nonnegative share | Frozen pre-treatment share within cell |
| normalization_scale | Positive number | Frozen baseline scale; retain raw outcomes |
| local_error, shared_error, used_error | Target units | Locked prediction minus realized target |
| buffer, transferable_capacity | Resource units | Pre-existing constraint and netting feasibility |
| accounting_loss | Currency | Realized ledger loss under approved schedule |
| diagnostic_cost, delay_cost | Currency | Incremental measured resource costs |
| exposure_pre | Vector | Pre-treatment business-condition exposures |
| shift_flag | Boolean | Prespecified external episode definition |
| missing_reason, outage_flag | Category/Boolean | Missingness and operational failure |
| source_id, revision_id | String | Audit trail for every timestamp and value |

## 9. Data-source feasibility assessment

Internal prospective panel: scientifically preferred, presently unavailable. Requires forecast archives, decision records, permission, isolated operational cells, and repeated episodes. There is no claim of access to the user's employer or any private data.

M5 Accuracy: official Kaggle competition page and organizer publication verified. Hierarchical retail sales can support retrospective rolling-origin forecast comparisons subject to current access conditions. Requires user-authorized acquisition under applicable platform terms; this package has not downloaded or accepted anything. It lacks actual shared-model rollout timing, local overrides, decision authority, and an operational cost ledger. It therefore supports benchmarking, not a causal test of organizational adoption or realized tail losses.

No real-data result table is populated. The supplementary template uses explicit NOT ESTIMATED entries. Data access and validity gates must be met before those entries can be replaced.

# R1 addendum: identifying source production and information reuse

This addendum supersedes the old primary live contrast. The prior protocol remains an unrun planning document and is not empirical support for the theoretical article. The legacy Student-interval exercise remains a warning, not a proposed validated inference method. The theoretical article does not depend on completion of this study.

The new mechanism requires a distinction between producing a local forecast and paying to report it. Identify source-operation assignment g, report assignment k, fresh-source assignment h, and their actual costs separately. Equal public posterior variance is not sufficient to identify informational equivalence.

A feasible prospective factorial or multiarm design would randomize at documented operational cells: (A) existing independent local sources with no central collection; (B) a randomized subset of those sources reported before action; (C) newly produced blinded sources with matched target, horizon and intended precision; (D) all existing operating sources collected at recorded cost. A separate randomized source-production budget can compare zero and paid acquisition. Do not claim that a budget assignment assures compliance or genuine independence.

Within report arm B, randomize the reporting identities among equally eligible units before forecasts are generated or inspected. Freeze source quality and exposure strata. Compare reporters' and nonreporters' private innovation weights after a common correction, using immutable action inputs. The model predicts no *additional* private-innovation weight for a reporter once its forecast is included in the public posterior, while a nonreporter can retain one. This is an information-overlap prediction rather than an instruction that reporters should mechanically stop thinking.

Archive the raw common forecast, every locked source, the exact correction function, the identities included in it, and the common posterior or deployed correction version. A forecast reused under a different label is not a fresh source. Measure provider/data lineage and actual observation overlap, not assessor counts. Record if the correction used a sample mean, full vector, or another aggregation.

For acquisition, randomize source-operation reimbursements or access budgets independently of anticipated forecast difficulty. Track purchases/inspections and locked results. A shared-model quality change that simultaneously alters incentives or decision rights cannot identify the acquisition threshold. Blinding alone has no predicted acquisition effect in the Gaussian benchmark when both arms receive the same forecast before action; any measured difference requires an additional behavioral or production mechanism.

Additional dictionary fields: source_acquired (verified Boolean), source_operation_id, source_cost, reporting_assignment, reporting_included, reporting_cost, source_lineage_id, locked_before_display, correction_input_hash, correction_version, residual_common_error, raw_local_error, conditional_local_innovation, forecast_target_match, commitment_deadline, and source_available_at. Freeze evidence of target/horizon match before outcomes.

Primary new estimands: report-assignment ITT on action response and operating loss; fresh-versus-reused-source ITT at prespecified cost and quality bands; source-budget ITT on verified acquisition. Bias-adjusted covariance is secondary unless episode precision gates are met. Inclusion in a corrected forecast is a treatment component, not a post-treatment confounder to remove. An observational action-weight regression does not establish causal learning without randomized inclusion or another justified design.

Source production, dissemination, action adaptation and target realization have distinct timestamps. If action affects the target (including sales censoring), forecast-only and live-policy outcomes have different potential outcomes. Analyze the relevant interference boundary and preserve failures and missing outcomes.

No sample has been recruited, permissions obtained, randomization run, or finite-sample field inference validated. The exact finite Gaussian model and rational policy certificate are the article's completed results; the proposed panel is a separate research program.


# R2 identification correction (prospective; not run)

The R2 paper supersedes any interpretation above implying an intrinsic reuse penalty. Record N=g+h distinct primitive observations, m=k+h public observations, r=N-m private observations, and operating/reporting/external resource prices separately. At fixed N and m the symmetric Gaussian model predicts equal optimized operating loss, regardless of the reuse label. A fixed-g, fixed-m intervention changes N and therefore tests an information-stock margin instead. Label those estimands separately. To test the procurement reduction, vary or measure the full internal public-source price kappa/n+c_R relative to c_E, conditional on r,m and internal capacity n-r. At equality, all feasible compositions are cost ties; observed choices alone do not identify a strict preference. Non-equality deviations can reflect unmeasured costs or violations of symmetric independent equal-precision assumptions. Do not assign them automatically to sharing harm. No experiment, recruitment, spending, or inference has been performed or authorized.


# R3 hidden-production identification addendum (prospective; not run)

Measure the common bit/forecast, raw candidate report, report timestamps, actual source operation and locked output where consented verification permits it, audit assignment and results, real audit cost, transfer schedule, and report access for each operating controller. Report agreement and disagreement separately. In the model, selective checking can induce fabricated opposition without source production, so disagreement alone is not an independence indicator. Conversely, agreement need not indicate copying. The audit technology must establish distinct physical/data production rather than merely report correctness.

A potential study would randomize the audit protocol and report-use channel with explicit authorization and track actual production. Its estimands would include production by cost type where measured, strategic report direction, report likelihood, audit load, operating covariance and real resource costs. It must distinguish a payment transfer from a real source/audit/communication cost and measure coordination costs before interpreting the model's switch. Private cost types cannot simply be assumed observed; no cost report is elicited by the theoretical posted contract. No study, recruitment, spending or outside contact has occurred. The source device and paid log verification are explicit theoretical assumptions, not validated technologies in a participating firm.
