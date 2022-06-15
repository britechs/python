def print_result(winstates:int):
    if(winstates>=2):
        print(f'You have won, {winstates}')  # Press Ctrl+F8 to toggle the breakpoint.
    else:
        print("You lost")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_result(2)
    print_result(1)