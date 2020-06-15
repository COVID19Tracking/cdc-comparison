# CDC vs CRDT Racial Data Comparison

Insights doc compiled [here](https://docs.google.com/document/d/1wFatuW4fUDCJqGub1cb8CD6o72LL7Ct77348Feg8h7w/edit?usp=sharing)

The Covid Racial Data Tracker team wants to keep a pulse on the quality of CDC data and the CDC's data collection strategy. We *believe* the CDC is using detailed demographics from death certificates to update their numbers, though those reported values are subject to long reporting lags. We might be able to glean insights from their reports nonetheless.

I asked Alice Goldfarb what the goal of this analysis should be. Her reply was:

"If what they’re reporting is woefully behind or different from what is publicly available from the states, we want to point that out. It’s the CDC, after all, why wouldn’t they have the most authoritative numbers?

If it seems like they’re getting much much better data (for death certificate pipeline reasons) and could provide a really thorough overview that we couldn’t, we might not collect as often, and do more work on analyzing the data. I think if there is data being made public through the CDC but not on state pages, it’s an argument we can use with those states that they should report it  directly.

And at least for me, a lot of the choices we made were the least worse choice at the time, and if there was a compelling reason to change how we did something, we would - and seeing the differences between what they do and what we do might point out some of those. It may also be that it’s such a mess we can’t learn much from what they have, but I’d be totally interested in getting nudged to do things differently.
There’s probably some other stuff, but that’s off the top of my head.

And I think when we started wondering, it was really a comparison in broad strokes - do they report for cases? do they report race and ethnicity? are they getting data from the states or does it look like it’s a different route because the numbers are way different? Do we have about the same percentage of unknowns?"


## Relevant Slack Threads

https://covid-tracking.slack.com/archives/C0136TL83RR/p1592070877059200


## Datasets

Currently, I'm analyzing [CDC reported deaths](https://data.cdc.gov/NCHS/Deaths-involving-coronavirus-disease-2019-COVID-19/ks3g-spdg) since this is the only COVID data I was able to find with demographics

If anyone finds datasets for cases or tests with demographics, please add!


Other datasets of potential interest are:

[Conditions contributing to COVID death by age group (US-level)](https://data.cdc.gov/NCHS/Conditions-contributing-to-deaths-involving-corona/hk9y-quqm)
Prevalence of chronic conditions by race, age group (state-level)](https://chronicdata.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-CDI-/g4ie-h725)
[Prevalence of health conditions in 500 major cities (city-level)](https://chronicdata.cdc.gov/500-Cities/500-Cities-Local-Data-for-Better-Health-2019-relea/6vp6-wxuq)
[Death counts by place of death (state-level)](https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-Place-of-Deat/uggs-hy5q)
[Prevalence of obesity within target groups; age, income, education, race (state-level)](https://chronicdata.cdc.gov/Behavioral-Risk-Factors/BRFSS-Table-of-Overweight-and-Obesity-BMI-/fqb7-mgjf)

