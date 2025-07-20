limit = 10

num = 1
sum = 1

numbers = '1'

while sum < limit:
    num += 1
    sum += num
    numbers += f' + {num}'
print(f'The consequtive sum: {numbers} = {sum}')