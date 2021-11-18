# Election_Analysis

## Background
## Overview of Project
A Colorado Board of Elections employee assigned the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
1. Get a complete list of candidates who received votes.
1. Calculate the total number of votes for each candidate received.
1. Calculate the percentage of votes each candidate won.
1. Determine the winner of the election based on popular vote.
1. Calculate the voter turnout for each county.
1. Calculate the percentage of votes from each county out of the total.
1. Determine the county with the highest turnout.

### Resources
Data Source: election_results.csv
Software: Python 3.9.1, Atom 1.58.0 x 64

------------------
### Purpose
see  [Background 0--> Overview of Project](#background).

## Methodology: Analytics Paradigm

#### 1. Decomposing the Ask
Using election results dataset to determine the 8 questions asked above in [Background 0--> Overview of Project](#background).

#### 2. Identify the Datasource
election_results.csv

#### 3. Define Strategy & Metrics
Using Python to read, compute and format output of the requirements into a txt file.

#### 4. Data Retrieval Plan
Use election_results.csv in Python with ```import csv``` and ```file_to_load = os.path.join("resources", "election_results.csv")```

#### 5. Assemble & Clean the Data
Python scripting

#### 6. Analyse for Trends
8 questions asked above in [Background 0--> Overview of Project](#background).

#### 7. Acknowledging Limitations
* Limitation of personal knowledge in Python programming
* Using Python, the scripts will run in real-time.

#### 8. Making the Call:
The "Proper" Conclusion is indicated below on [Results](#results)

------------------
## Analysis


### Results Analysis

**2018 timer**

>Old Runtime for 2018

![Old Runtime for 2018](resources/2018_timer.png)

>New Runtime for 2018

![New Runtime for 2018](resources/VBA_Challenge_2018.png)

With the new code, our runtime is 0.238 seconds compared to 4.96 seconds.

**2017 timer**

>Old Runtime for 2017

![Old Runtime for 2017](resources/2017_timer.png)

>New Runtime for 2017

![New Runtime for 2017](resources/VBA_Challenge_2017.png)

With the new code, our runtime is 0.261 seconds compared to 5.3 seconds.

We can conclude above that the speed increase for the data are:

**2018-** 20.8 times faster

**2017-** 20.3 times faster

### Code Efficiency Analysis

1. **Storing results in an array & reducing iterations**

In the old code, we have nested for loops code structure:


2. **Changing the initial code base from**

For the full code, see [Appendix](#appendix).

## Results

From [Analysis](#analysis)

## Summary


## Appendix
```

```
