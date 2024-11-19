import statistics
scores = {'Alice': 99, 'Bob': 87, 'Clara': 91}
mean = sum(scores.values()) / len(scores)
median = statistics.median(scores.values())
print(mean, median)
