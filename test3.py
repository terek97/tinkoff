def input_height():
    global nums
    while len(nums) != n:
        number = input(f'input {n} numbers: ')
        nums = number.split()


def result():
    global nums
    even = 0
    odd = 0
    for num in nums:
        if int(num) % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    if even > odd or odd - even > 1:
        return '-1 -1'

    errors_count = 0
    errors = {}

    for num in nums:
        (nums.index(num) + 1) % 2
        if (nums.index(num) + 1) % 2 == 0 and not int(num) % 2 == 0:
            errors_count = errors_count + 1
            errors[num] = nums.index(num)

        if not (nums.index(num) + 1) % 2 == 0 and int(num) % 2 == 0:
            errors_count = errors_count + 1
            errors[num] = nums.index(num)

    if len(errors) != 2:
        return '-1 -1'
    else:
        keys = list(errors.keys())
        values = list(errors.values())
        return f'{keys[1]} {keys[0]}'


n = 0
nums = []

while not n in range(2, 1001):
    n = int(input('input n: '))

input_height()

for num in nums:
    if not int(num) in range(1, 10 ** 9 + 1):
        nums = []
        input_height()

print(result())
