# bank_management_system
balance = 50000  #initial balance
correct_pin = 1234 # correct pin for login

# function for pin
def check_pin(): # create a function to verify user PIN
    pin = int(input("enter pin")) # taking input from user
    if pin == correct_pin: # check PIN matches the correct pin 
        return True # return true if PIN is correct
    else: # execute when PIN is incorrect
        print("incorrect password")
        return False # return false for incorrect PIN 

#function for deposit
def deposit(): #create a function for deposit
    global balance # allow the function to modify the global balance variable
    amount = int(input("enter amount to deposit")) # take deposit from user
    balance = balance+amount # update the balance
    print("Money deposit successfully") # print message
    print("total balance:", balance) # print total balance



#function for withdraw
def withdraw(): #create a function for withdraw
    global balance
    amount = int(input("enter amount to withdraw"))
    if amount <= balance: #if condition apply
        balance = balance-amount # allow the function to modify the global balance variable
        print("please collect your cash") # print message
        print("remaining amount", balance) #show remaining balance
    else:
        print("insufficient amount") # print message



#function to show balance
def show_balance(): #create a function of show balance
    print("current balance:", balance) # print current balance




# main program
if check_pin(): #call the check_pin function. If the user enter the correct PIN (True),the code inside the block run
    print("\n 1. Deposit") # display option 1
    print("\n 2. Withdraw") #display option 2
    print("\n 3. check balance") #display option 3
    choice = int(input("enter your choice"))
    if choice == 1: #  if user chooses option 1
        deposit() # call the deposit function to add money
    elif choice == 2: #if user chooses option 2 
        withdraw() # call the deposit function to withdraw money 
    elif choice == 3: # if user choose the option 3
        show_balance() # call the show display the function
    else: 
        print("invalid choice") 
else: #this else belong to if check_pin
    print("access denied") # runs when the enterd pin is incorrect

print("thank you for using our bank")
