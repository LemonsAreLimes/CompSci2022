def RRSP(startingAmmount=None, investTime=None, yearlyDeposit=False):

    total = startingAmmount    

    for i in range(0, investTime):
        total *= 1.05

        if yearlyDeposit:
            total += yearlyDeposit

    return round(total, 2)

x = RRSP(100, 5, 10)
print(x)