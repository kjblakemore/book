# Q: What is big data?

* Find FOUR really big datasets. They should be sufficiently different. Cite your sources.
* Discuss and determine a ranking in terms of "bigness".

I ranked the following four data sets based on veracity and complexity.  These metrics are inversely related, the less veracious data is, the more complex the analysis will be.

## Rank 1: [1000 Genomes](http://www.1000genomes.org/home)
Data sets of human genomes from population-scale sequencing.

This data set is ranked "biggest" in terms of veracity and complexity, because of its magnitude (3 billion DNA base pairs per genome) and its heterogeneity.  

## Rank 2: [Email](https://sites.google.com/site/emailresearchorg/datasets)

A list of email data sets collected by Google.

The veracity of email derives from the difficulty in selecting email features for analysis.  The feature selection for email analysis is more difficult than that of the remaining two data sets.

## Rank 3: [Coupon](https://www.kaggle.com/c/coupon-purchase-prediction)

Data sets for a Kaggle competition to predict user coupon purchases based on past purchase and browsing history.

The veracity of this data set is due to its size, (approximately one year of history for 22,873 users), large set of disparate features (some of which are irrelevant) and its lack of fit into traditional machine learning algorithms.  To develop a predictive algorithm for this data, it is likely that some type of reduction of the features would be needed. 

## Rank 4: [Neural](http://datasets.codeneuro.org/)

Curated neural data sets.  

The neural data set that I am familiar with is the Ahren's Lab Direction Selectivity Experiment.  In this experiment neuron firing of larval zebrafish is measured using light-sheet imaging.  Each sample is a coordinate location, followed by a time series of intensity measures.  The data is not complex, but it is very large, requiring a reduction, such as principal component analysis, in order to visualize the results.