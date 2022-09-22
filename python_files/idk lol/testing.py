from asyncio import constants


def accumilator(start, stop, step):

    total = 0

    for i in range(start, stop, step):
        total += i

    return total


t = accumilator(0, 100, 5)
print(t)