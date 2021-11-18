# Election_Analysis

# Stock Analysis

## Background


## Overview of Project



### Purpose


## Analysis And Challenges

## Methodology: Analytics Paradigm

#### 1. Decomposing the Ask
To get the codes working faster and more elegantly with less traversal of the dataset.

#### 2. Identify the Datasource
Same dataset is used.

#### 3. Define Strategy & Metrics
Look at the current code and visualise the calls and routines to refine and reduce data calls.
Store data into arrays.

#### 4. Data Retrieval Plan
Use stock analysis dataset in Excel

#### 5. Assemble & Clean the Data
Excel VBA scripting

#### 6. Analyse for Trends
Compare timer from old codes with new codes

#### 7. Acknowledging Limitations
* Unable test out the new codes with a much larger dataset for a dry-run.
* Using VBA, the scripts will run in real-time.

#### 8. Making the Call:
The "Proper" Conclusion is indicated below on [Results](#results)

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

### Refactoring Code


## Appendix
```

```
