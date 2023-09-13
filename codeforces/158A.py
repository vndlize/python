n, k = map(int, input().split())
scores = list(map(int, input().split()))
k_score = scores[k - 1]
count = 0
for score in scores:
    if score >= k_score and score > 0:
        count += 1
print(count)
