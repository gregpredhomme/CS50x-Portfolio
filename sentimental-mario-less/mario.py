from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height < 9 and height > 0:
        break

counter = 1
for i in range(height):
    print(" " * (height - counter) + "#" * counter)
    counter += 1



