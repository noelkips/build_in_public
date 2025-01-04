
# Learn to program 2 tutorial
# Author: Noel Langat
# 100days of code day - 4

# printing a tree based on number rows user entered
height = int(input("Tree height: "))
spaces = height - 1
initial_spaces = spaces
hashes = 1

while height:
    for j in range(spaces):
            print(' ',end="")
    for i in range(hashes):
            print('#',end="")
    print()
    height -= 1
    hashes += 2
    spaces -= 1
for j in range(initial_spaces):
    print(' ',end="")
print("#")
         