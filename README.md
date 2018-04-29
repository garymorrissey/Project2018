# The Iris Flower Data Set

The Iris flower data set is a specific set of information which was compiled by [Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher), a British statistician and biologist, in the 1930's. Anders Hald states in his 'A History of Mathematical Statistics' that: 

> much of Fishers work single-handedly created the foundations for modern statistical science. 

This work stems from his collaboration with [Edgar Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson), an American botanist, and the compilation of a set of data which aims to demonstrate statistical methods of classification. The data set consists of 50 samples from each of three species or Iris flower - Iris Setosa, Iris Virginica and Iris Veriscolor. For the data set, four specific features were measured from each sample;

- Petal length
- Petal width
- Sepal length
- Sepal width

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

The Iris Flower Data Set is compiled is an easy to read and from the data we aim to calculate the following:

- Mean
- Mode
- Median
- Range
- Maximum value of each column 
- Minimum value of each column

In order to investigate the data set, we are using the python programming language and will run a number of different algorithms to claculate the results outlined above.   

## Investigation Results

Calculation|Column|Result|
------------|------------|------------|
**Mean**|**Petal Length**|**5.84333333333cm**|
||**Petal Width**|**3.054cm**|
||**Sepal Length**|**3.75866666667cm**|
||**Sepal Width**|**1.19866666667cm**|
**Mode**|**Petal Length**|**5.0cm**|
||**Petal Width**|**3.0cm**|
||**Sepal Length**|**1.5cm**|
||**Sepal Width**|**0.2cm**|
**Median**|
**Range**|
**Maximum value of each column**|**Petal Length**|**7.9cm**|
||**Petal Width**|**4.4cm**|
||**Sepal Length**|**6.9cm**|
||**Sepal Width**|**2.5cm**|
**Minimum value of each column**|**Petal Length**|**0.1cm**|
||**Petal Width**|**2.0cm**|
||**Sepal Length**|**1.0cm**|
||**Sepal Width**|**0.1cm**|


## References
[1] https://shapeofdata.wordpress.com/2013/10/01/case-study-1-iris
[2] https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
[3] https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching
[4] https://www.techopedia.com/definition/32880/iris-flower-data-set
[5] http://patrickhoey.com/downloads/Computer_Science/0_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf
[6] https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342

