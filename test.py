n = 0
k = 0
nums = []
while not n in range(1, 1001) or not k in range(1, 10**4 + 1):
    n, k = (int(i) for i in input('input n and k: ').split())

while len(nums) != n:
    nums = []
    number = str(input(f'input {n} numbers: '))
    nums = number.split()


first_sum = sum(map(int, nums))


changes = []

for num in nums:
    replaced_num = num.replace(num[0], '9')
    changes.append(int(replaced_num) - int(num))

count = 0
while count < k:
    elem = changes.index(max(changes))
    nums[elem] = nums[elem].replace(nums[elem][0], '9')
    changes[elem] = 0
    count = count + 1

print(sum(map(int, nums)) - first_sum)








    



