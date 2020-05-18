# Summary
This repo contains work involved in comparing COVID Tracking Project data to the CDC COVID tracker data.

## Data
We are using CDC data current to 3pm EST 5/16, saved to https://github.com/covidtrackingproject/cdc-comparison/blob/master/cdc.csv.
Note that the freshness of testing data differs from that of the cases/deaths data:
- Testing data timestamp: May 13 2020 12:00AM
- Positives/deaths data timestamp: May 16 2020 5:45PM.

For that reason, we compare the CDC testing data to CTP data published on May 14 (which reflects May 13). For the positives/deaths 
data comparison, we use CTP data published on May 16.

The main data file created in this repo and used for most plots and analyses is: https://github.com/COVID19Tracking/cdc-comparison/blob/master/merged_data_for_analysis.csv.

The only data point not directly capture in the main data file is whether a state reports testing counts in specimens, cases, or both.
We store that data in: https://github.com/COVID19Tracking/cdc-comparison/blob/master/ctp_514_specimen_tests.csv.

## Analysis
The main analysis is done in a Jupyter notebook: https://github.com/COVID19Tracking/cdc-comparison/blob/master/CDC%20vs%20CTP%20comparison.ipynb.
