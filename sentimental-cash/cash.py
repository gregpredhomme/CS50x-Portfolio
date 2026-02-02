from cs50 import get_float

while True:
    dollars = get_float("Change owed: ")
    if dollars > 0:
        break

coins = round(dollars * 100)

count = 0

count += coins // 25
coins = coins % 25

count += coins // 10
coins = coins % 10

count += coins // 5
coins = coins % 5

count += coins // 1
coins = coins % 1

print(count)
