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
    checkResults([40,50,60])
    checkResults([55,60])
