# The Iris Flower Data Set

The Iris flower data set is a specific set of information which was compiled by [Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher), a British statistician and biologist, in the 1930's. Anders Hald states in his 'A History of Mathematical Statistics' that: 

> much of Fishers work single-handedly created the foundations for modern statistical science. 

This work stems from his collaboration with [Edgar Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson), an American botanist, and the compilation of a set of data which aims to demonstrate statistical methods of classification. The data set consists of 50 samples from each of three species or Iris flower - Iris Setosa, Iris Virginica and Iris Veriscolor. For the data set, four specific features were measured from each sample;

- Sepal length
- Sepal width
- Petal length
- Petal width

On the back of their data, Fisher developed a linear discriminant model to distinguish the species from each other. This function analysis is now widely used in statistics, pattern recognition and machine learning to find a linear combination of features that essentially seperates classes of objects or events. According to Patrick Hoey is his paper on Statistical Analysis of the Iris Flower Dataset; 

> The goal of a discriminant analysis is to produce a simple function that, given the four measurements, will classify a flower correctly. 

## Data Analysis and the Iris Data Set

Fishers Iris Data Set is widely believed to be a great starting point into the world of Analysis and Machine Learning. According to [machinelearningmastery.com](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/) there are a number of reasons for this:

- It only has 4 attributes and 150 rows, meaning the data is small but not trivial
- The data is real data, but of good quality
- Discriminating between three species of Iris from their measurements is simple but challenging
- Attributes are numeric so you need to learn how to load and and handle the data

## Investigation of the Data Set and Python

The purpose of investigating a data set is to use summary statistics and visualisations to better understand the data presented, to find clues about the data and its quality and to formulate assumptions of our analysis. According to [datascienceguide.github](https://datascienceguide.github.io/exploratory-data-analysis) the goal should be to create a figure which anyone can look at in a few seconds and understand what is going on. 

The Irish Flower Data Set is compiled is an easy to read and from the data we aim to calculate the following:

- Mean
- Mode
- Median
- Range
- Maximum and Minimum values of each column

## Investigation Results

Calculation|Column|Result(cm)|Comment
------------|------------|------------|------------
**Mean**|**Petal Length**|**5.84333333333**|
||**Petal Width**|**3.054**|
||**Sepal Length**|**3.75866666667**|
||**Sepal Width**|**1.19866666667**|
**Mode**|**Petal Length**|**5.0**|
||**Petal Width**|**3.0**|
||**Sepal Length**|**1.5**|
||**Sepal Width**|**0.2**|
**Median**
**Range**
**Maximum Value of each column**|**Petal Length**|**7.9**|
||**Petal Width**|**4.4**|
||**Sepal Length**|**6.9**|
||**Sepal Width**|**2.5**|
**Minimum value of each column**|**Petal Length**|**0.1**|
||**Petal Width**|**2.0**|
||**Sepal Length**|**1.0**|
||**Sepal Width**|**0.1**|
