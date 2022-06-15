def isNotValid(answer, choiceslen):
    if answer.isdigit():
        ino = int(answer)
        if ino<=0 or ino>choiceslen:
            return True
        return False
    return True

def show_questions(q, choices, rate_change):
    print(q)
    for c in choices:
        print(c)
    answer = input("Please enter your choice")
    while isNotValid(answer, len(choices)):
        answer = input("Please enter your choice")

    indno = int(answer)
    return rate_change[indno-1]

def print_result(winstates:int):
    if winstates>=2:
        print(f'You have won, {winstates} states')  # Press Ctrl+F8 to toggle the breakpoint.
    else:
        print("You lost")

def checkResults(rates):
    winstates=0
    for r in rates:
        if r>50:
            winstates+=1

    print_result(winstates)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = show_questions("Park choice",['1.A',"2.B","3.C"],[0,5,-5])
    print(a);

