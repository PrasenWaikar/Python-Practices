scores = {'Alice': 99, 'Bob': 87, 'Clara': 91}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(sorted_scores)  # {'Alice': 99, 'Clara': 91, 'Bob': 87}
