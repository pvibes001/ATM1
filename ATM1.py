import re,random,string
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
pass_reg_ex = '^[a-zA-Z]+[0-9]$'
def login():
    try:
        cycle = True
        user_input = input("Do you have an account? (yes/y)/(no/n) : ").lower()
        while cycle:
            if user_input == "yes" or user_input == "no" or user_input == "y" or user_input == "n":
                cycle = False
                return user_input
            else:
                user_input = input("Do you have an account? (yes/y)/(no/n) : ").lower()
    except:
        return "Something went wrong\nTry running the program again"

def check(email):
    return re.search(regex,email)
def check_password(password):
    return re.search(pass_reg_ex,password)

def password_generator():
    return random.randrange(30500)
def signup():
    try:
        first_name = input("Enter your first name : ")
        last_name = input("Enter your last name : ")
        other_names = input("Other names? y/n : ")
        if other_names == "y":
            other_names = input("Type in your other names : ").strip().split()
            email = input("Enter your email address : ")
            while not(check(email)):
                email = input("Enter your email address : ")
            password = password_generator()
            return first_name,last_name,other_names,email,password
        else:
            email = input("Enter your email address : ")
            while not(check(email)):
                email = input("Enter your email address : ")
            password = password_generator()
            return first_name,last_name,email,password
    except:
        return "Something went wrong\nTry running the program again"
def change_password(original):
    count = 0
    while not check_password(original):
        if count < 1:
            original = input("Enter your new passord :(mixture of numbers and letters) ")
            count += 1
        else:
            original = input("Enter your new passord :(Please note: a mixture of numbers and letters is required!) ")
            count += 1
    return original

print(change_password("asdfghj"))
