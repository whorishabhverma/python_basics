def fib():
    first,second = 0,1
    while True:
        yield first
        first,second = second,first+second

gen = fib()
# for i in gen:
#     if i>200:
#         break
#     print(i)

n=10
for i in range(10):
    print(next(gen))

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))