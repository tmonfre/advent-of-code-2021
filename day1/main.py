input = open("./day1/input.txt", "r")
rows = []

for line in input:
    rows.append(int(line.strip('\n')))

input.close()

## HELPERS

def num_increasing_intervals(values):
    sum = 0

    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            sum += 1
    
    return sum

## PART 1

print(num_increasing_intervals(rows))

## PART 2

accum_sums = []

for i in range(len(rows) - 2):
    accum_sums.append(rows[i] + rows[i+1] + rows[i+2])

print(num_increasing_intervals(accum_sums))
