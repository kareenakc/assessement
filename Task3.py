import random
def main():
    print("Welcome to pop chat\nOne of our operators will be pleased to help you today.")
    operator_names = ["Janice","Candice","Karen","Jennifer","Florence"]
    email_address = input("Please enter your Poppleton email address:")

    if email_check(email_address,domain="pop.ac.uk") == True:
        username = email_address[0:email_address.index('@')]
        print(f"\nHello,{username}! Thank you, and welcome to Pop Chat !")
        print(f"My name is {random.choice(operator_names)}, and it will be my pleasure to help you.")
        choose = [0,0,0,1,2,3,4,5,6,7,8]
        if random.choice(choose) == 0:
            print("Network Error")
        else:
            while True:
                question = input("---->")
                if reply(question) == 0:
                    break 
        print(f"Thank {username}, for using popchat.See you soon!\n")     
    else:
        print("Invalid email id")


def email_check(email_address,domain): 
    """validates an email passed when called"""
    if email_address.index('@')>2 and domain in email_address:
        return True
    else:
        return False

def reply(quest):
    replies =["Mmmm.","Oh, my","Oh,yes"," I see.","Tell me more."]  
    if "wifi" in quest:
        print("WiFi is excellent across the campus.")
    elif "library" in quest:
        print('Sorry!The library is closed today')
    elif "deadline" in quest:
        print("Your deadline has been extended by two working days")
    elif "coffee" in quest:
        print ( "Cafe opens at 7 AM")
    elif "lab" in quest:
        print("Lab are well maintained and open for everyone.")
    elif "exit" in quest or "bye" in quest:
        return 0
    else:
        print(random.choice(replies))

main()