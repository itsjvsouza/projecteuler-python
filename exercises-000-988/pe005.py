num = 2521
counter = 0

while True:
    for i in range(1, 21):
        if num % i == 0:
            counter += 1

            if counter == 20:
                break
        else:
            counter = 0
            num += 1
            break

    if counter == 20:
        print(num)
        break    
