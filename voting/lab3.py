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

def updateN(a,b):
    a=a+10
    b=b-10


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #a = show_questions("Park choice",['1.A',"2.B","3.C"],[0,5,-5])
    #print(a);
    #a=10;
    #b=20;
    #updateN(a,b);
    #print(a,b)
    initial_points=50;

    question = """
    A new party that stresses education
    is dismayed by the lack of focus on schooling
    in both groups, but they are
    hated more by Mammoths
    What do you do?""";
    choices = ["Denounce Them(type 1)", "Win them over(type 2)", "or Ignore them(type 3)"]
    changes = [-5,5,0]
    all_changes = show_questions(question, choices, changes)
    print("Now your score is: " + str(initial_points + all_changes));

    question = """
    You are throwing an event and need to provide food
    Who do you ask to cater?""";
    choices = ["Local farmers(type 1)", "Taco Bell(type 2)", "Your mom(type 3)"]
    changes = [-5,5,0]
    all_changes = all_changes + show_questions(question, choices, changes)
    print("Now your mule score is: " + str(initial_points + all_changes));
    print("Now your mamoth score is: " + str(initial_points - all_changes));

    question = """
    Obesity is at an all time high
    What do you do?""";
    choices = ["Promote veganism(type 1)", "Green Food day(type 2)", "Build more gyms(type 3)"]
    changes = [-5,5,0]
    all_changes =  all_changes + show_questions(question, choices, changes)
    print("Now your score is: " + str(initial_points + all_changes));
    print("Now your mamoth score is: " + str(initial_points - all_changes));
