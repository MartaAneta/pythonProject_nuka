import numpy
import stats as stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
speed1 = [99,86,87,88,86,103,87,94,78,77,85,86]

x1 = numpy.median(speed1)

x = numpy.mean(speed)
y = numpy.median(speed)
z = stats.mode(speed)
x2 = numpy.std(speed)

print(x2)
print(x)
print(x1)
print(z)
print(y)