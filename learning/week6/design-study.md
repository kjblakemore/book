# Design Pattern Change Study

### Authors

This study was proposed by
* [Karen Blakemore](https://github.com/kjblakemore)
* [Brian McKean](https://github.com/co-bri)
* [Mingqi Lew](https://github.com/Malaokia)
* [Matt Schroeder](https://github.com/mattschroeder97)

### Overview

Our team proposed to study the design of automobiles.  Using the methods described in the paper, "Collect, Decompile, Extract, Stats, and Diff: Mining Design Pattern Changes in Android Apps", by Khalid Alharbi and Tom Yeh, we considered design features of automobiles and how these impacted new car sales over time.

The following sections outline the phases of our proposed analysis.

### Collect

The first step in our analysis involves collection of automobile data from websites such as [Edmunds](http://www.edmunds.com), [Kelley Blue Book](http://www.kbb.com) and the [National Highway Traffic Safety Administration](http://www.nhtsa.gov/).

### Decompile

The decompile phase involves translating the data collected into a format from which the features can be easily extracted.

### Extract

In the extract phase, the following features are extracted from the decompiled data.

* Manufacturer
* Model
* Make
* Year
* Color
* Fuel (gas, electric, hybrid, diesel or alternative)
* Horse Power
* Engine Type
* Body Style
* Miles per gallon
* Drive Train (FWD, AWD, 4WD)
* Safety
* Reliability
* Number of passengers
* Size
* Transmission type (automatic, manual)
* Car Type (SUV, Minivan, Wagon, Crossover, etc.)

### Statistics

During the statistics phase, we will select features of interest and calculate the number of units sold and average sales price for various values of these features.

### Diff

In the last step of our analysis, we consider how the number of units sold and average sales price change over time for the features of interest.


