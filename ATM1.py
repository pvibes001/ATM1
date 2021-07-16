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
    x = random.randint(6,12)
    seed = list(chr(x) for x in list(x for x in range(200) if x in range(48,58) or x in range(65,91) or x in range(97,123)))
    return "".join([random.choice(seed) for x in range(x)])
def signup():
    try:
        first_name = input("Enter your first name : ")

        last_name = input("Enter your last name : ")
        other_names = input("Other names? y/n : ").lower()
        if other_names == "y":
            other_names = input("Type in your other names : ").strip().split()
            email = input("Enter your email address : ")
            while not(check(email)):
                email = input("Enter your email address : ")
            password = password_generator()
            return last_name,first_name,other_names,email,password
        elif other_names == "n":
            email = input("Enter your email address : ")
            while not(check(email)):
                email = input("Enter your email address : ")
            password = password_generator()
            return last_name,first_name,email, + password
        else:
            raise TypeError("Invalid Input\nRestart the program and type in correct input")
    except TypeError:
        return "Something went wrong\nTry running the program again"
    except Exception as e:
        return e("Something went wrong on our end\nPlease bear with us as we fix it as soon as possible")
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
def account_details_gen():
    card_number = random.randint(1000000000000000,9000000000000000)
    while not(ans == "y")
    bank_pin = random.randint(1000,9999)
def account_opener(bvn=True):
    if bvn:
        pass

print(signup())
