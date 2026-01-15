prices = [
    [5, 9, 2, 4, 3],
    [6, 7, 1, 8, 2]
]
totals = []
for i in range(len(prices)):
    total = 0
    for j in range(len(prices[i])):
        total += prices[i][j]
    totals.append(total)
    print(f"Item {i + 1} - Total: {total}$")
max_total = max(totals)
min_total = min(totals)
difference = max_total - min_total
highest_item = totals.index(max_total) + 1
print("\nHighest Total:", max_total, "$ | Item:", highest_item)
print("Difference:", difference, "$")
