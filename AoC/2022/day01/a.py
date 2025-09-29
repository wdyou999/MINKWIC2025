# Find largest sum of numbers, one per line, separated by a blank line

fname = "test.txt"
#fname = "input.txt"
fil=open(fname,'r')

sum = 0
largest = 0
for f in fil:
    f = f.strip()
    if len(f) == 0:
        # New line - check for largest
        if sum > largest:
            largest = sum
    else:
        # Number - add to current sum
        sum += int(f)

print('Part a', largest)
# Something is wrong - this value it too high
    
