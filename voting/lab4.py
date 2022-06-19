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

class VoteQuestion:
    # default constructor
    questionLines = []
    choices = []
    rateChanges = []

    # output
    change_point_mule = 0;

    def showQuestion(self):
        q = ""
        for tq in self.questionLines:
            q = q + tq + "\r\n"
        rc = show_questions(q, self.choices, self.rateChanges)
        self.change_point_mule = rc

class StateVoteQuestions:
    voteQuestions = []

    # input
    initial_mule_point=50
    initial_mammoth_point = 50

    # output
    mule_point = 0;
    mammoth_point= 0;

    def showAllQuestions(self):
        self.mule_point = self.initial_mule_point
        self.mammoth_point = self.initial_mammoth_point

        for q in self.voteQuestions:
            q.showQuestion()
            self.mule_point = self.mule_point + q.change_point_mule
            self.mammoth_point = self.mammoth_point - q.change_point_mule


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    question = [
    "A new party that stresses education",
    "is dismayed by the lack of focus on schooling",
    "in both groups, but they are",
    "hated more by Mammoths",
    "What do you do?"];
    choices = ["Denounce Them(type 1)", "Win them over(type 2)", "or Ignore them(type 3)"]
    changes = [-5,5,0]

    q_state1 = VoteQuestion()
    q_state1.questionLines = question;
    q_state1.choices = choices
    q_state1.rateChanges = changes;

    question2 = [
    "You are throwing an event and need to provide food",
    "Who do you ask to cater?"];
    choices2 = ["Local farmers(type 1)", "Taco Bell(type 2)", "Your mom(type 3)"]
    changes2 = [-5,5,0]

    q_state2 = VoteQuestion()
    q_state2.questionLines = question2;
    q_state2.choices = choices2
    q_state2.rateChanges = changes2;

    question3 = [
    "Obesity is at an all time high",
    "What do you do?"];
    choices3 = ["Promote veganism(type 1)", "Green Food day(type 2)", "Build more gyms(type 3)"]
    changes3 = [-5,5,0]

    q_state3 = VoteQuestion()
    q_state3.questionLines = question3;
    q_state3.choices = choices3
    q_state3.rateChanges = changes3;

    state_vq = StateVoteQuestions()
    state_vq.voteQuestions = [q_state1,q_state2,q_state3]
    state_vq.showAllQuestions()

    print("Now your mule score is: "  , state_vq.mule_point);
    print("Now your mammoth score is: ", state_vq.mammoth_point);
