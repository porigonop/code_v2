score = [1, 5, 9, 8, 1]
max_score = sum(score)
score = list(map(lambda x:x/max_score, score))
print(score)