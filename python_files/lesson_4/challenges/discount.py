import random

items = []
for i in range(3):
    ammount = float(input(f'input the ammount of item {i}: '))
    items.append(ammount)

print("_______RECIPT_______")

for n in items:

    line = str(n).ljust(10)
    line += str(round(n*1.05, 2)).rjust(10)

    print(line)

discount = random.randrange(10, 50, 10) / 100

print("____________________")
print('total: {}'.format(round(sum(items)*1.05, 2)))
print('todays discount: {}%'.format(discount * 100))
print('final price: {}'.format(round(sum(items)*1.05*discount, 2)))
print("_______RECIPT_______")
