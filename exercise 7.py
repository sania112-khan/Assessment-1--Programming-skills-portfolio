# Loop 1: Count up from 0 to 50 in increments of 1
print("Loop 1: Counting up from 0 to 50")
for i in range(0, 51, 1):      # range(start, stop, step) → goes from 0 to 50 increasing by 1
    print(i)                  # print each value of i

print("--------------------------------")  # separator line

# Loop 2: Count down from 50 to 0 in decrements of 1
print("Loop 2: Counting down from 50 to 0")
for i in range(50, -1, -1):    # start at 50, go down to 0 (stop at -1 so 0 is included)
    print(i)

print("--------------------------------")

# Loop 3: Count up from 30 to 50 in increments of 1
print("Loop 3: Counting up from 30 to 50")
for i in range(30, 51):        # start at 30, go to 50 (default step = 1)
    print(i)

print("--------------------------------")

# Loop 4: Count down from 50 to 10 in decrements of 2
print("Loop 4: Counting down from 50 to 10 in steps of 2")
for i in range(50, 9, -2):     # go from 50 to 10 (stop at 9 so 10 is included), step -2
    print(i)

print("--------------------------------")

# Loop 5: Count up from 100 to 200 in increments of 5
print("Loop 5: Counting up from 100 to 200 in steps of 5")
for i in range(100, 201, 5):   # from 100 to 200 increasing by 5 each time
    print(i)
