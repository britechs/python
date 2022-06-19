
def newliebniz(c,d):
    print("A new party that stresses education")
    print(" is dismayed by the lack of focus on schooling")
    print("in both groups, but they are")
    print("hated more by Mammoths")
    print("What do you do?")
    j = str(input("Denounce Them(type 1), Win them over(type 2), or Ignore them(type 3)"))
    if j == "1":
        c = c - 5
        d = d + 5
        print("New Poll: ")
        print("Mules: " + str(c))
        print("Mammoths: " + str(d))
    elif j == "2":
        c = c + 5
        d = d - 5
        print("New Poll: ")
        print("Mules: " + str(c))
        print("Mammoths: " + str(d))
    elif j == "3":
        print("New Poll: ")
        print("Mules: " + str(c))
        print("Mammoths: " + str(d))
    print("You are throwing an event and need to provide food")
    print("Who do you ask to cater?")
    k = str(input("Local farmers(type 1), Taco Bell(type 2), Your mom(type 3)"))
    if k == "1":
        c = c - 5
        d = d + 5
        print("New Poll: ")
        print("Mules: " + str(c))
        print("Mammoths: " + str(d))
    elif k == "2":
        c = c + 5
        d = d - 5
        print("New Poll: ")
        print("Mules: " + str(c))
        print("Mammoths: " + str(d))
    elif k == "3":
        print("New Poll: ")
        print("Mules: " + str(c))
        print("Mammoths: " + str(d))
    print("Obesity is at an all time high")
    print("What do you do?")
    l = str(input("Promote veganism(type 1), Green Food day(type 2), Build more gyms(type 3)"))
    if l == "1":
        c = c - 5
        d = d + 5
        print("Final Poll: ")
        print("Mules: " + str(c))
        print("Mammoths: " + str(d))
    elif l == "2":
        c = c + 5
        d = d - 5
        print("Final Poll: ")
        print("Mules: " + str(c))
        print("Mammoths: " + str(d))
    elif l == "3":
        print("Final Poll: ")
        print("Mules: " + str(c))
        print("Mammoths: " + str(d))
    return (c,d)
def Rollerton(a,b):
    print("Trade is a major issue for residents.")
    print("Should Calculandia import seeds or steel?")
    m = str(input("Seeds(type 1), Steel(type 2), or Books(type 3): "))
    if m == "1":
        a = a + 5
        b = b - 5
        print("New Poll: ")
        print("Mules: " + str(a))
        print("Mammoths: " + str(b))
    elif m == "2":
        a = a - 5
        b = b + 5
        print("New Poll: ")
        print("Mules: " + str(a))
        print("Mammoths: " + str(b))
    elif m == "3":
        print("New Poll: ")
        print("Mules: " + str(a))
        print("Mammoths: " + str(b))
    print("Integrand National Park slammed Derivative Apartment")
    print("for building too close to them. THey think the towers are disrupting the natural scenery")
    print("Who do you side with?")
    o = str(input("Integrand Park(type 1), Derivative Apartment(type 2), Stay out of it(type 3)"))
    if o == "1":
        a = a + 5
        b = b - 5
        print("New Poll: ")
        print("Mules: " + str(a))
        print("Mammoths: " + str(b))
    elif o == "2":
        a = a - 5
        b = b + 5
        print("New Poll: ")
        print("Mules: " + str(a))
        print("Mammoths: " + str(b))
    elif o == "3":
        print("Mules: " + str(a))
        print("Mammoths: " + str(b))
    print("In a live press conference for the GreenEarth foundation,")
    print("a reporter asks you for your stance on shark-finning")
    print("What do you say?: ")
    n = str(input("Poaching is good(type 1), Save the sharks(type 2), Remain neutral(type 3): "))
    if n == "1":
        a = a + 5
        b = b - 5
        print("Final Poll: ")
        print("Mules: " + str(a))
        print("Mammoths: " + str(b))
    elif n == "2":
        a = a - 5
        b = b + 5
        print("Final Poll: ")
        print("Mules: " + str(a))
        print("Mammoths: " + str(b))
    elif n == "3":
        print("Final Poll: ")
        print("Mules: " + str(a))
        print("Mammoths: " + str(b))
    return (a,b)
def EulersCreek(e,f,g):
    print(" You need to pick a symbol for your campaign.")
    print("What do you pick? ")
    p = str(input("Mule(type 1), Mammoth(type 2), Cow(type 3)"))
    if p == "3":
        if g == "1":
            e = e + 5
            f = f - 5
        elif g == "2":
            e = e - 5
            f = f - 5
    print("New Poll: ")
    print("Mules: " + str(e))
    print("Mammoths: " + str(f))
    print("You've been given a speech. Which location do you pick?")
    q = str(input("A park(type 1), a bridge(type 2), the city hall(type 3)"))
    if q == "3":
        if g == "1":
            e = e + 5
            f = f - 5
        elif g == "2":
            e = e - 5
            f = f - 5
    print("New Poll: ")
    print("Mules: " + str(e))
    print("Mammoths: " + str(f))
    print("A reporter asks you what your favorite area of the state is in an interview")
    print("What do you say?")
    r = str(input("The beach(type 1), The capital city(type 2), Your neighborhood(type 3)"))
    if r == "3":
        if g == "1":
            e = e + 5
            f = f - 5
        elif g == "2":
            e = e - 5
            f = f - 5
    print("Final Poll: ")
    print("Mules: " + str(e))
    print("Mammoths: " + str(f))
    return (e,f,g)
def main():
    A = 55
    B = 45
    C = 45
    D = 55
    E = 50
    F = 50
    i = 1

    print("Welcome to Calculandia. You are about to enter the race for the presidency")
    print("You'll be asked questions that affect polling numbers.")
    print("You need to win over 50 percent of votes in two states to win")
    print("There are two parties you can run for")
    print("Mules favor nature and the environment?: ")
    print("mammoths favor expansion")
    print("Which party would you like to pick?")
    G = str(input("Type 1 for Mules, 2 for mammoth: "))
    print("There are three states in Calculandia")
    #Make it a menu
    print("Current polling nunmbers")
    print("NEW LIEBNIZ:")
    print("Mules: 45")
    print("Mammoths: 55")
    print("New Liebniz is a growing industrial city.")
    print("Residents take pride in their bustling, towering skyscrapers and tend to prefer the policy of the mammoths.")
    print("ROLLERTON: ")
    print("Mules: 55")
    print("Mammoths: 45")
    print("Rollerton is a suburban state that basks in green countryside.")
    print("Although Rollerton has a lack of tall buildings, residents love the natural feel of the state and prefer the policy of the Mules. ")
    print("EULER'S CREEK: ")
    print("Mules: 50")
    print("Mammoths: 50")
    print("Euler's Creek residents hate the partisan politics today and prefer candidates that have unique solutions to the problems they face.")
    while i <= 3:
        h = str(input("Pick a state to campaign in: type 1 for New Liebniz, 2 for Rollerton, 3 for Euler's Creek: "))
        if h == "1":
            (C,D)=newliebniz(C,D)
        elif h == "2":
            (A,B)=Rollerton(A,B)
        elif h == "3":
            (E,F,G)=EulersCreek(E,F,G)

        i = i + 1
    print("The campaign is over! ")
    print("Here are the final results!")
    print(" In New Liebniz: ")
    print("Mules: " + str(C))
    print("Mammoths: " + str(D))
    print("In Rollerton: ")
    print("Mules: " + str(A))
    print("Mammoths: " + str(B))
    print("In Euler's Creek: ")
    print("Mules: " + str(E))
    print("Mammoths: " + str(F))
    wincount = 0
    if G == "1":
        if A > B:
            wincount = wincount + 1
        if C > D:
            wincount = wincount + 1
        if E > F:
            wincount = wincount + 1
    elif G == "2":
        if A < B:
            wincount = wincount + 1
        if C < D:
             wincount = wincount + 1
        if E < F:
            wincount = wincount + 1
    if wincount >= 2:
        print("Congratulations! You are the next president of Calculandia!")
    else:
        print("Unfortunately, you lost. Better luck next time!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = 50
    b = 50
    (a,b)=newliebniz(a,b)
    print(a,b)




