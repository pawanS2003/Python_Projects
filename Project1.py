# --------------While Loop----------------
while (True):
# ------------User Input----------------
    a = int(input("Entar Sr. No. :-"))
    b = input("Enter Student First Name:-")
    b1 = input("Enter Student Last Name:-")
    c = input("Enter Std Subjects :-")
    d = int(input("Entar Class :-"))
    e = input("Enter School Name:-")
# -------------Condition or Break And Continue-----------------
    user_input = input("Do you want to continue? (yes/No) :- ")
    if user_input == "yes":
        continue
    elif user_input == "No":
        print("User has ended the Program")
        break
    else:
        print("Enter Choice as yes or No")
# -------------Condition, Break, Continue and File Hendling-----------------
while (True):
    userchoice = input("Do you want to see the Data? (yes/No) :-")
    if userchoice == "Yes":
        continue
    elif userchoice == "No":
        print("User has ended the Program")
        break
    else:
        print("Enter Choice as yes or No")
        f = open("f:\\Project1.txt", "a")
        f.write(f'\n {a}               {b}                      {b1}                       {c}                  {d}                 {e}')
        f.close()
        # ----------File Reading------------
        frr = open("f:\\Project1.txt", "r")
        rd = frr.read()
        print(rd)
        frr.close()





