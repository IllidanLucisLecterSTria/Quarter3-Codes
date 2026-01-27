prices = [
    [5, 9, 2, 4, 3],
    [6, 7, 1, 8, 2]
]
row_number = 1
for row in prices:
    print("Item", row_number, "prices:", row)
    total = sum(row)
    average = total / len(row)
    print("Total price:", total)
    print("Average price:", average)
    print()
    row_number += 1
max_price = prices[0][0]
for row in prices:
    for price in row:
        if price > max_price:
            max_price = price
print("Highest price in the dataset:", max_price)

#Using a 2D array helped me organize grocery prices by item and by store. Each row stored all prices for one item, which made it easy to calculate totals and averages. The array also allowed me to loop through the data instead of writing repetitive code.
#Calculating the total and average for each row was easy because Python provides built-in functions like sum() and len(), which are very useful when calculating for totals and averages. Printing each row using a loop was also very simple and clear. Finding the maximum value was a bit difficult for me at first because it required using nested loops.
