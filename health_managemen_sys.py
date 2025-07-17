def getdate_time():
    """This function returns time"""
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")

def helper_func():
    """This function asks name and return a number respective to that name"""
    print("enter your name")
    name = input()
    if name == "harry" or name == "Harry":
        return 1
    elif name == "rohan" or name == "Rohan":
        return 2
    elif name == "hammad" or name == "Hammad":
        return 3
    else:
        print("your name is not in our database")
        return None


def log_retrieve_choice():
    """ This function asks user to choose between log and retrieving of user data and return number respectively"""
    print("please enter 1 for log and 2 for retrieving")
    a = int(input())
    if a == 1:
        return a
    elif a == 2:
        return a
    else:
        print("wrong input")

def file_choice():
    """This function helps to choice between the diet and exercise files and return number respectively"""
    print("please enter 1 for exercise and 2 for diet")
    a = int(input())
    if a == 1:
        return a
    elif a == 2:
        return a
    else:
        print("wrong input")




def logger(u_name):
    """This is the logger function which logs user data to files related to individual user and set of files among diet and exercise"""
    f_choice = file_choice()
    time = getdate_time()
    if f_choice == 1:
        if u_name == 1:
            with open("harry_ex.txt", "w") as f:
                print("what exercise have you did today")
                user_input = input()
                f.write("[ "+time+" ] " + user_input + "\n")

        elif u_name == 2:
            with open("rohan_ex.txt", "w") as f:
                print("what exercise have you did today")
                user_input = input()
                f.write("[ "+time+" ] "+ user_input + "\n")

        elif u_name == 3:
            with open("hammad_ex.txt", "w") as f:
                print("what exercise have you did today")
                user_input = input()
                f.write("[ "+time+" ] "+user_input + "\n")

            ###############
    elif f_choice == 2:
        if u_name == 1:
            with open("harry_diet.txt", "w") as f:
                print("what food you ate today")
                user_input = input()
                f.write("[ "+time+" ] "+ user_input + "\n")

        elif u_name == 2:
            with open("rohan_diet.txt", "w") as f:
                print("what food you ate today")
                user_input = input()
                f.write("[ "+time+" ] "+ user_input + "\n")

        elif u_name == 3:
            with open("hammad_diet.txt", "w") as f:
                print("what food you ate today")
                user_input = input()
                f.write("[ "+time+" ] "+ user_input + "\n")

def retrieval(u_name, ftc):
    """This function helps to reads user data from individual user and from either diet of exercise and print result in main console"""
    if ftc == 1:
        if u_name == 1:
            with open("harry_ex.txt", "r") as f:
                    print(f.readline())


        elif u_name == 2:
            with open("rohan_ex.txt", "r") as f:
                    print(f.readline())

        elif u_name == 3:
            with open("hammad_ex.txt", "r") as f:
                    print(f.readline())
    elif ftc == 2:
        if u_name == 1:
            with open("harry_diet.txt", "r") as f:
                    print(f.readline())

        elif u_name == 2:
            with open("rohan_diet.txt", "r") as f:
                    print(f.readline())

        elif u_name == 3:
            with open("hammad_ex.diet", "r") as f:
                    print(f.readline())


def final_func():
    """main function which call all functions and do couplings """
    choice = log_retrieve_choice()
    if(choice == 1):
        name = helper_func()
        logger(name)

    elif(choice == 2):
        filech = file_choice()
        name2 = helper_func()
        retrieval(name2,filech)


final_func()  # entry of the program

