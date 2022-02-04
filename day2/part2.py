f = open('day2/input.txt')
# f = open('day2/example.txt')

lines = f.readlines()
lines = map(lambda x: x.strip(), lines)
f.close()

aim = hpos = depth = 0

for line in lines:
    action, amount = line.split()
    amount = int(amount)
    if action == "forward":
        hpos += amount
        depth += aim * amount
    elif action == "down":
        aim += amount
    elif action == "up":
        aim -= amount

print(hpos, depth, hpos * depth)
