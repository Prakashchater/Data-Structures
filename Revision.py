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

def fib(n):
    p, q = 0, 1
    while p < n:
        yield p
        p, q = q, p+q
x = fib(10)
for i in fib(10):
    print(i)
