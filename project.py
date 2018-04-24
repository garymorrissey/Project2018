# Gary Morrissey, 20-April-2018
# Analysis of the Iris Flower Data Set

print("Petal Length", "Petal Width", "Sepal Length", "Sepal Width")  # Column headings

with open ("Data/iris.csv") as f: # Link the csv file
    for line in f:
        print('{:^12} {:^12} {:^12} {:^12}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))

# Calculating the mean from each column
# Petal Length
import numpy
data = numpy.genfromtxt('Data/iris.csv', delimiter=',') # Used genfromtxt to load the data from a text file
first_column = data[:,0] # Generating an array for column 1
maxfirst_column = numpy.max(data[:,0]) # Max value of the Petal Length
meanfirst_column = numpy.mean(data[:,0]) 
print('The mean petal length of the three species in the dataset in cm is', meanfirst_column) # Print the average of column 1 - Petal Length
print('The maximum value of the Petal length in cm is', maxfirst_column)

# Petal Width
data = numpy.genfromtxt('Data/iris.csv', delimiter=',') # Repeated genfromtxt
second_column = data[:,1] # Generating an array for column 2
maxsecond_column = numpy.max(data[:,1]) # Max value of the Petal Width
meansecond_column = numpy.mean(data[:,1])
print('The mean petal width of the three species in the dataset in cm is', meansecond_column) # Print the average of column 2 - Petal Width
print('The maximum value of the Petal width in cm is', maxsecond_column)

# Sepal Length
data = numpy.genfromtxt('Data/iris.csv', delimiter=',') # Repeated genfromtxt
third_column = data[:,2] # Generating an array for column 3
maxthird_column = numpy.max(data[:,2]) # Max value of the Sepal Length
meanthird_column = numpy.mean(data[:,2])
print('The mean sepal length of the three species in the dataset in cm is', meanthird_column) # Print the average of column 3 - Sepal Length
print('The maximum value of the Sepal length in cm is', maxthird_column)

# Sepal Width
data = numpy.genfromtxt('Data/iris.csv', delimiter=',') # Repeated genfromtxt
fourth_column = data[:,3] # Generating an array for column 4
maxfourth_column = numpy.max(data[:,3]) # Max value of the Sepal Width
meanfourth_column = numpy.mean(data[:,3])
print('The mean sepal width of the three species in the dataset in cm is', meanfourth_column) # Print the average of column 4 - Sepal Width
print('The maximum value of the Sepal width in cm is', maxfourth_column)
