# Gary Morrissey, 20-April-2018
# Analysis of the Iris Flower Data Set

print("Petal Length", "Petal Width", "Sepal Length", "Sepal Width")  # Column headings

with open ("Data/iris.csv") as f: # Link the csv file
    for line in f:
        print('{:^12} {:^12} {:^12} {:^12}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))

# Calculating the mean from each column
# Petal Length
import numpy
data = numpy.genfromtxt('Data/iris.csv', delimiter=',')
first_column = data[:,0] # Generating an array for column 1
meanfirst_column = numpy.mean(data[:,0]) 
print(meanfirst_column) # Print the average of column 1 - Petal Length

# Petal Width
data = numpy.genfromtxt('Data/iris.csv', delimiter=',')
second_column = first_column = data[:,1]
meansecond_column = numpy.mean(data[:,1])
print(meansecond_column)
