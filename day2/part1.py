f = open('day2/input.txt')
# f = open('day2/example.txt')

lines = f.readlines()
lines = map(lambda x: x.strip(), lines)
f.close()

hpos = depth = 0

# part 1
for line in lines:
    action, amount = line.split()
    amount = int(amount)
    if action == "forward":
        hpos += amount
    elif action == "down":
        depth += amount
    elif action == "up":
        depth -= amount

print(hpos, depth, hpos * depth)
