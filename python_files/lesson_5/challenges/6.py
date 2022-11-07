
def highestMark(marks=None):
    if marks==None: return

    highest = 0
    for i in marks:
        if i >= highest: 
            highest = i

    return highest

def average(marks=None):
    if marks==None: return
    
    total = 0
    for i in marks:
        total += i

    return total/len(marks)

def getMarks():
    print('type done when you are finished inputting the marks')

    marks = []
    while True:
        mark = input('input a mark: ')
        if mark == 'done':break
        marks.append(int(mark))

    return marks


def main():
    marks = getMarks()
    avg = average(marks)
    higest = highestMark(marks)

    full_list = [avg, higest]
    full_list.append(marks)

    print(f'the average is: {full_list[0]}')
    print(f'and the highest mark was: {full_list[1]}')

if __name__ == "__main__":
    main()