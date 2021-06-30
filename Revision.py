# def lowercase(function):
#     def wrapper():
#         func = function()
#         s = func.lower()
#         return s
#     return wrapper
#
# @lowercase
# def hello():
#     return "HELLO WORLD"
# print(hello())

# def fib(n):
#     p, q = 0, 1
#     while p < n:
#         yield p
#         p, q = q, p+q
# x = fib(10)
# for i in fib(10):
#     print(i)

# import calendar
# y = 2000
# m = 3
# print(calendar.month(y, m))

# import datetime
# x = datetime.datetime.now()
# print(x)


# class Solution:
#    def solve(self, L):
#        k = 0
#        if len(L) == 0:
#            return []
#
#        for i in range(len(L)):
#            if L[i] != 0:
#                L[k] = L[i]
#                k+=1
#        for j in range(k, len(L)):
#            L[j] = 0
#        return L
#
# ob = Solution()
# L = [2,0,1,4,0,5,6,4,0,1,7]
# print(ob.solve(L))


def moveEnd(arr):
    k = 0
    if len(arr) == 0:
        return []

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[k] = arr[i]
            k += 1
    for j in range(k, len(arr)):
        arr[j] = 0
    return arr

if __name__ == '__main__':
    arr = [2,0,1,4,0,5,6,4,0,1,7]
    print(moveEnd(arr))