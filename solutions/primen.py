def prime_nums(n):
    prime_numbers = []
    for i in range(2,n+1):
        count = 0
        for j in range(1,i):
            if (i%j==0):
                count+=1
        if count <=1:
            prime_numbers.append(i)
    return prime_numbers

n = int(input("Enter upper limit "))
print(prime_nums(n))
