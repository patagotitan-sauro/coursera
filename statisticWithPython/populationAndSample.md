# POPULATION AND SAMPLES
## Target Popultion 
### How to make inferatial statement about a population?
1. Conducting a Population Census
2. Probability Sampling (you have probabilities of selection)
3. Non-Probability Sampling

### Why Probability Sampling?
```text 
The known probability of selection for all units allows us to make unbiased
statements about both population features and the uncertainty in survey estimates.
```
1. Simple Random Sampling (SRS); e
2. Complex sampling for larger populations: stratification, cluster sampling and weighting.
- key benefits 

### Sampling distribution
```text
methods for making population inferences based on analyses of data from different types of samples.
``` 

### Simple Random Sampling (SRS)

1. Equal probability of Selection
```text
p = n / N

-> When we compute the estimatives of means, proportions and totals based on SRS are unbiased.

-> With replacement or without replacement

-> i.i.d Data: Independent and identically distribuited Data.
```
- very expensive. Rarely conducted in practice.

### Complex Probability Sampling

- complex: anything more complicated than SRS.
1. Certain key features
- Population divided into different `strata`, and part of sample is allocataded to each stratum; -> ensures sample represantation from each stratum, and reduces variance of survey estimates (`stratification`)
- `Clusters` of populations units (e.g., counties) are randomly sampled first (with known probability) with strata, to save costs of data collection (collect data from cases close to each other geographically)
- `Unit randomly sampled from within clusters`, according to some probability of selection, and measured.

```text 
A Unit's probability of selection is determined by:
- Number of clusters sampled from each stratum
- Total number of clusters in population in each stratum
- Number of units ultimately sampled from each cluster
- Total number of units in population in each cluster
```

- Example of complex sample design 
- Most important: `probability sampling` provides a `statistical basis for making inferences` about certain quantities in larger populations.


### Non-Probability Sampling

#### What defines a non-probability sample?

I. Features of Non-Probability Samples:
- probabilities of selection `can't be determined` for samples units 
- `Non random selection` individual units
- Samples can be divided in to groups (strata) or clusters, but `clusters not randomly sampled` in earlier stage
- Data collection often very cheap

#### So what is the problem?
- sample units `not selected at random` --> strong risk of `sampling bias`
(e.g., people actually interested in visiting particular web site)
- Sample units `not generally representative` of larger target population of interest
- `Big data` (e.g., information from millions of tweets) often from non-probability samples

#### So can we do?
- Many data sets arise from non-probability samples `... can we say anything about larger population?`
- Two possible approaches:
1. Pseudo-randomization
2. Calibration

#### Population Inference Approaches

1. Pseudo-Randomization Approach
```text
(i) Combine non-probability sample with probability sample that collected similar
(ii) Estimate probability of being included in non-probability sample as a function of auxiliary information available
(iii) Treat estimated probabilities of selection as "known" for the non-probability 
```
2. Calibration Approach
```text
(i) Compute weights for responding units in non-probability sample that allow weight sampled to mirror a known population.
(ii) Limitation: if weighting factor not related to variables of interest will not reduce possible sampling bias.
```

#### What's next
- Sampling distribution and sampling variance ~ how to estimate features of these distributions based on only one probability sample.
- Examples of making population inferences based on type of sample selected
-   Introduce model-based approaches to analyzing data