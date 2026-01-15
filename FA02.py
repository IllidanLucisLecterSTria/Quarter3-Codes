prices = [
    [5, 9, 2, 4, 3],
    [6, 7, 1, 8, 2]
]

#each row represents a specific item
#each column represents a specific store

print(prices[0][2])
prices[0][2] = 8
print(prices[0][2])

#I chose this dataset because I want to try different groceries having different prices on same items.
#I also want to make them either get a discount or increase the price on those items.
#A 2d array helps organize and work with this kind of data since I need to know if the prices updated on different stores.
