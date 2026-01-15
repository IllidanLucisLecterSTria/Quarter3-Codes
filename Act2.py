prices = [
    [5, 9, 2, 4, 3],
    [6, 7, 1, 8, 2]
]
for i in range(len(prices)):
    total = 0
    for j in range(len(prices[i])):
        total += prices[i][j]
    avg = total / len(prices[i])
    print("Item", i + 1,
          "- Total:", total,"$",
          "| Average:", avg,"$")
#It was like in a table, I could easily analyze the data I'm seeing.
#It was also already organized, all I had to was to make a strip of code that gets the total and average price of each row or the items, from different stores.
#I guess the hardest part of summarizing the data was the arrangement of the output.
