sum = 0
num = 1
prev_num = 0
current_num = 0

while num < 4000000:

    if num % 2 != 0:
        sum += num
    
    current_num = num
    num += prev_num
    prev_num = current_num

print(sum)