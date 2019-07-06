# total = 10
# denominations = [1,2,5,10,20,50,100,200]
# def coin_sum(total, denominations):
#     res = [-1] * (total + 1)
#     res[0] = 0
#     res[1] = 1
#     res[2] = 2
#     for i in range(3, total+1):
#         subres = 0
#         for j in range(len(denominations)):
#             if denominations[j] <= i:
#                 subres += res[denominations[j]]
#             if i % denominations[j] == 0:
#                 subres += 1
#         res[i] = subres
#     return res[total]
# if __name__ == "__main__":
#     print(coin_sum(total, denominations))
def compute():
    TOTAL = 10
    
    # At the start of each loop iteration, ways[i] is the number of ways to use {any copies
    # of the all the coin values seen before this iteration} to form an unordered sum of i
    ways = [1] + [0] * TOTAL
    print(ways)
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for i in range(len(ways) - coin):
            ways[i + coin] += ways[i]
    return str(ways[-1])


if __name__ == "__main__":
    print(compute())