from ast import parse

f = open('input.txt')
lines = f.readlines()
lines = map(lambda x: x.strip(), lines)
f.close()

prev_sum = 999999999999
window = []
result = 0

for line in lines:
    window = window[-2::] + [int(line)]
    if len(window) < 3:
        continue
    print(window)
    current = sum(window)
    if current > prev_sum:
        result += 1
    prev_sum = current

print(result)
