n = 2
def climbingStairs(n):
    if n < 0: return -1
    if n == 0: return 0
    if n == 1: return 1
    res = [0] * (n+1)
    res[0] = 0
    res[1] = 1
    res[2] = 2
    for i in range(3,(n+1)):
        res[i] = res[i-1] + res[i-2]
    return res[n]
print(climbingStairs(n))

'''
where to stuck:
如何简历foreach(methods) 和 subelements 的关系
'''
