import numpy as np

transactions = np.array([
    [1000, 50, 0],
    [5000, 20, 2],
    [3000, 80, 5]
])
k = 2

mn = transactions.min(axis=0)
mx = transactions.max(axis=0)

risk = []
for i in range(len(transactions)):
    norm_amt = (transactions[i][0] - mn[0]) / (mx[0] - mn[0])
    norm_time = (transactions[i][1] - mn[1]) / (mx[1] - mn[1])
    norm_fail = (transactions[i][2] - mn[2]) / (mx[2] - mn[2])
    
    score = norm_amt * 0.6 + norm_time * 0.3 + norm_fail * 0.1
    risk.append(score)

risk = np.array(risk)
top = np.argsort(risk)[::-1][:k]

print("\nTop Risky Users")
for i in range(k):
    idx = top[i]
    print(i + 1, "User", idx, transactions[idx], "Score =", round(risk[idx], 4))
