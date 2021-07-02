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


# def moveEnd(arr):
#     k = 0
#     if len(arr) == 0:
#         return []
#
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[k] = arr[i]
#             k += 1
#     for j in range(k, len(arr)):
#         arr[j] = 0
#     return arr
#
# if __name__ == '__main__':
#     arr = [2,0,1,4,0,5,6,4,0,1,7]
#     print(moveEnd(arr))



# def printTwinPrime(n):
    # Create a boolean array "prime[0..n]"
    # and initialize all entries it as
    # true. A value in prime[i] will
    # finally be false if i is Not a prime,
    # else true.
#     prime = [True for i in range(n + 2)]
#     p = 2
#
#     while (p * p <= n + 1):
#
#         # If prime[p] is not changed,
#         # then it is a prime
#         if (prime[p] == True):
#
#             # Update all multiples of p
#             for i in range(p * 2, n + 2, p):
#                 prime[i] = False
#         p += 1
#
#     # check twin prime numbers
#     # display the twin prime numbers
#     for p in range(2, n - 1):
#         if prime[p] and prime[p + 2]:
#             print("(", p, ",", (p + 2), ")", end='')
#
#
# # driver program
# if __name__ == '__main__':
#     # static input
#     n = 25
#
#     # Calling the function
#     printTwinPrime(n)


# import datetime
# now = datetime.datetime.now()
# current_time = now.strftime("%H:%M:%S %p")
# print("Current Time =", current_time)

# def moveEnd(arr, t):
#     k = 0
#     for i in range(len(arr)):
#         if arr[i] != t:
#             arr[k] = arr[i]
#             k += 1
#     for j in range(k, len(arr)):
#         arr[j] = t
#     return arr
#
#
# if __name__ == '__main__':
#     arr = [2,1,2,2,2,3,4,2]
#     t = 2
#     print(moveEnd(arr, t))


def moveEnd(arr, k):
    i = 0
    j = len(arr)-1
    while i < j:
        while i < j and arr[j] == k:
            j-=1

        if arr[i] == k:
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr

if __name__ == '__main__':
    arr = [2,1,2,2,2,3,4,2]
    k = 2
    print(moveEnd(arr, k))

