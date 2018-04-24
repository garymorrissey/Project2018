# Gary Morrissey, 20-April-2018
# Analysis of the Iris Flower Data Set
# Adapted from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/ 

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
minfirst_column = numpy.min(data[:,0]) # Min value of the Petal Length
meanfirst_column = numpy.mean(data[:,0]) 
print('The mean Petal Length of the three species in the dataset in cm is', meanfirst_column) # Print the average of column 1 - Petal Length
print('The maximum value of the Petal Length in cm is', maxfirst_column) # Print the max value in the Petal Length column
print('The minimum value of the Petal Length in cm is', minfirst_column) # Print the min value in the Petal Length column

# Petal Width
data = numpy.genfromtxt('Data/iris.csv', delimiter=',') # Repeated genfromtxt
second_column = data[:,1] # Generating an array for column 2
maxsecond_column = numpy.max(data[:,1]) # Max value of the Petal Width
minsecond_column = numpy.min(data[:,1]) # Min value of the Petal Width
meansecond_column = numpy.mean(data[:,1])
print('The mean Petal Width of the three species in the dataset in cm is', meansecond_column) # Print the average of column 2 - Petal Width
print('The maximum value of the Petal Width in cm is', maxsecond_column) # Print the max value in the Petal Width column
print('The minimum value of the Petal Width in cm is', minsecond_column) # Print the min value in the Petal Width column

# Sepal Length
data = numpy.genfromtxt('Data/iris.csv', delimiter=',') # Repeated genfromtxt
third_column = data[:,2] # Generating an array for column 3
maxthird_column = numpy.max(data[:,2]) # Max value of the Sepal Length
minthird_column = numpy.min(data[:,2]) # Min value of the Sepal Length
meanthird_column = numpy.mean(data[:,2])
print('The mean Sepal Length of the three species in the dataset in cm is', meanthird_column) # Print the average of column 3 - Sepal Length
print('The maximum value of the Sepal Length in cm is', maxthird_column) # Print the max value in the Sepal Length column
print('The minimum value of the Sepal Length in cm is', minthird_column) # Print the min value in the Sepal Length column

# Sepal Width
data = numpy.genfromtxt('Data/iris.csv', delimiter=',') # Repeated genfromtxt
fourth_column = data[:,3] # Generating an array for column 4
maxfourth_column = numpy.max(data[:,3]) # Max value of the Sepal Width
minfourth_column = numpy.min(data[:,3]) # Min value of the Sepal Width
meanfourth_column = numpy.mean(data[:,3])
print('The mean Sepal Width of the three species in the dataset in cm is', meanfourth_column) # Print the average of column 4 - Sepal Width
print('The maximum value of the Sepal Width in cm is', maxfourth_column) # Print the max value in the Sepal Width column
print('The minimum value of the Sepal Width in cm is', minfourth_column) # Print the min value in the Sepal Width column
