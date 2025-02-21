def even_numbers(N):
    for i in range(0, N+1, 2):
        yield i
N=int(input("Enter a number N: "))
even_numbers=(str(num) for num in even_numbers(N))
print(", ".join(even_numbers))