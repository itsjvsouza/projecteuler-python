counter = 0
num = 4
primes_sum = 5

while True:
    for i in range(2, num):
        if num == 1999999:
            break

        if num % i != 0:
            counter += 1
            
            if counter == num - 2:
                primes_sum += num
                counter = 0
                num += 1

        else:
            num += 1
            break
    
    if num == 1999999:
        break

print(primes_sum)
