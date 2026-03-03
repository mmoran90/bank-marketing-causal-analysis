Overview

This project estimates the causal effect of marketing contact on customer subscription to a term deposit using observational data.

Rather than relying on naive correlations, the analysis implements a full propensity score weighting framework to adjust for selection bias.

Objective

Determine whether being contacted by the bank increases the probability that a customer subscribes.

Methodology

1. Leakage Removal

Removed duration (post-treatment variable).

Removed macroeconomic and campaign timing variables that caused near-deterministic treatment assignment.

Ensured valid overlap between treated and control groups.

2. Propensity Score Modeling

Logistic regression with regularization.

Estimated probability of treatment given customer characteristics.

Verified healthy overlap distribution.

3. Stabilized Inverse Probability Weighting (IPW)

Constructed stabilized weights.

Confirmed stable weight distribution (no extreme explosions).

4. Covariate Balance Diagnostics

Post-weight Standardized Mean Difference (SMD):

Max SMD = 0.042

Indicates strong covariate balance.

Results

Naive effect: ~9.5 percentage points

Causal (IPW-adjusted) effect: ~5.3 percentage points

After adjusting for confounders, marketing contact increases subscription probability by approximately 5 percentage points.

The naive estimate overstated the impact due to selection bias.

What This Demonstrates

Proper handling of leakage

Recognition and correction of overlap violations

Implementation of stabilized IPW

Balance diagnostics to validate causal adjustment

Clear distinction between correlation and causation

This project showcases applied causal inference beyond standard predictive modeling.
