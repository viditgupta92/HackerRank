fact = 1
N = int(input())
def factorial(N):
    global fact
    if N == 1:
        return 1
    else:
        return (N * factorial(N-1))
print(factorial(N))