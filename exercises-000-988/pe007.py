place = 2
counter = 0
num = 4

while True:
    for i in range(2, num):
        if place == 10001:
            break

        if num % i != 0:
            counter += 1
            
            if counter == num - 2:
                counter = 0
                place += 1
                num += 1

        else:
            num += 1
            break
    
    if place == 10001:
        break

print(num - 1)
