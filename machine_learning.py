import numpy
import stats as stats
import numpy
import matplotlib.pyplot as plt

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
speed1 = [99,86,87,88,86,103,87,94,78,77,85,86]

x1 = numpy.median(speed1)

x = numpy.mean(speed)
y = numpy.median(speed)
z = stats.mode(speed)
x2 = numpy.std(speed)
x3 = numpy.var(speed)
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x4 = numpy.percentile(ages, 75)#What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.

print(x4)

print(x2)
print(x)
print(x1)
print(z)
print(y)
x6 = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x6, 5)
x7 = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x7, 100)
plt.show()