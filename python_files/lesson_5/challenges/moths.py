
months = [
    'jan',
    'feb',
    'mar',
    'apr',
    'may',
    'jun',
    'jul',
    'aug',
    'sept',
    'oct',
    'nov',
    'dec'
]

for i in range(len(months)): print(f'{ i }: { months[i] }')
user_months = int(input('please enter in the index of your birth month: '))

if user_months > len(months) or user_months < 0: print('invalid input!'); exit()

if user_months < 9: print('your birthday has passed!')
elif user_months == 9: print('your bith day is this month!')
else: print(f'hey your birthday is only: { user_months - 9 } months away!')
