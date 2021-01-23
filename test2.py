l = 0
r = 0
count = 0

while not 1 <= l or not r <= 10 ** 18:
    l, r = (int(i) for i in input('input l and r: ').split())

if r < l:
    print(0)

for i in range(l, r + 1):
    if str(i) == len(str(i)) * str(i)[0]:
        count = count + 1
        l = l + 1

print(count)
