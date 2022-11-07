#This is a ATM app, you log in into a bank account, then you can deposit or withdraw specific amount of money.
print("Welcome to the BANK")
pin = 1234
tries = 3
withdraw_correct_answer = False
account_balance = 1000 #That's your account balance, you cannot withdraw more than that 
wrong_command = True
inputcode = 0

while tries != 0:
    inputcode = input("Please enter your pincode. (It's 1234): ")
    if inputcode == '1234':
        while wrong_command == True:
            choice = input("Do you want to deposit or withdraw? ")
            while choice.lower() == 'deposit':
                deposit_of_user = input("Enter the amount You wish to deposit: ")
                if deposit_of_user.isdigit():
                    print(deposit_of_user, "$ have been deposited to Your bank account!")
                    quit()
                else:
                    print("Enter the correct amount!")
            while choice.lower() == 'withdraw':
                while withdraw_correct_answer == False:
                    withdraw_of_user = input("Enter the amount You wish to withdraw: ")
                    if withdraw_of_user.isdigit():
                        if int(withdraw_of_user) > int(account_balance):
                            print("Not enough funds!")
                        else:
                            print(withdraw_of_user, "$ have been withdrawed from Your bank account!")
                            quit()
                    else:
                        print("Enter the correct amount!")
            else:
                print("I don't understand this command.")  
    else: 
        inputcode != pin
        tries -= 1
        print(f"Wrong pin code, You have {tries} tries left. ")
    
print("You've ran out of tries!")




