def divisible_by_3_and_4(N):
    for i in range(0, N+1):
        if i%3==0 and i%4==0:
            yield i
N = int(input("Enter a number N: "))
divisible_numbers=(str(num) for num in divisible_by_3_and_4(N))
print(", ".join(divisible_numbers))