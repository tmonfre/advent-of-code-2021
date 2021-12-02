input = open("./day2/input.txt", "r")
rows = []

for line in input:
    (command, amount) = line.strip('\n').split(" ")
    rows.append((command, int(amount)))

input.close()

## PART 1

position = 0
depth = 0

for (command, amount) in rows:
    if command == "forward":
        position += amount
    elif command == "down":
        depth += amount
    elif command == "up":
        depth -= amount
    
print(position * depth)

## PART 2

position = 0
depth = 0
aim = 0

for (command, amount) in rows:
    if command == "forward":
        position += amount
        depth += (aim * amount)
    elif command == "down":
        aim += amount
    elif command == "up":
        aim -= amount
    
print(position * depth)
