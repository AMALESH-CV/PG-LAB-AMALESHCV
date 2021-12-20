# Import statistics Library
import statistics

a=[1, 3, 5, 7, 9, 11, 13]

# Calculate harmonic mean
print(statistics.harmonic_mean(a))


# Calculate average values
print(statistics.mean([1, 3, 5, 7, 9, 11, 13]))

# Calculate middle values
print(statistics.median([1, 3, 5, 7, 9, 11, 13]))

# Calculate the mode
print(statistics.mode(['red', 'green', 'blue', 'red']))
print(statistics.mode([1,2,3,1]))
print(statistics.mode([1, 3, 3, 3, 5, 7, 7, 9, 11]))

# Calculate the variance of an entire population
print(statistics.pvariance([1, 3, 5, 7, 9, 11]))
# Calculate the variance of an entire population
print(statistics.pvariance(a))