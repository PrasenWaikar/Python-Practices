scores = {'Alice': 99, 'Bob': 87, 'Clara': 91}
high_scores = {k: v for k, v in scores.items() if v > 90}
print(high_scores)  # {'Alice': 99, 'Clara': 91}
