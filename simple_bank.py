import time

default_loan_interest=12

my_account={
    'id': 0,
    'name': 'Meci',
    'balance': float(12)
}

accounts=[
    {
        'id' : 123456,
        'name' : 'Irineu',
        'balance' : 201
    },
    {
        'id' : 234567,
        'name' : 'Hundai',
        'balance' : 9345
    },
    {
        'id' : 345678,
        'name' : 'Xorg',
        'balance' : 94345  
    }
]

transactions=[
    {
        'id': 1,
        'ammount': +100,
        'date': time.time
    },
    {
        'id': 2,
        'ammount': -50,
        'date': time.time
    },
    {
        'id': 3,
        'ammount': -10,
        'date': time.time
    }
]

my_loans=[
    {  
        'id': 1,
        'ammount': 50,
        'interest': 12
    },
    {
        'id': 2,
        'ammount': 50,
        'interest': 6
    }
]



def view_transactions():
    print("\n"*100)
    print("Your Balance: ",my_account['balance'],"€")
    print("\n")
    for i in transactions:
        print("###")
        print('Transaction ID: ',i['id'])
        print('Transaction Ammount: ',i['ammount'],"€")
        print('Transaction Date: ',i['date'])
    input("Press Enter To Go Back")

def make_transaction():
    print("\n"*100)
    print("Your Balance: ",my_account['balance'],"€")
    print("\n")
    for i in accounts:
        print("###")
        print("Account Name: ", i['name'])
        print("Account ID: ", i['id'])
        print("Account Balance: ", i['balance'])

    try:
        send_accountint=int(input("ID Of Account To Send: "))
        ammount=float(input("Ammount To Send: "))

        for i in accounts:
            if (i['id'] == send_accountint):
                if (ammount <= my_account['balance']):
                    transactions.append({
                        'id': len(transactions)+1,
                        'ammount': ammount,
                        'date': time.time
                    })
                    i['balance']+=ammount
                    my_account['balance']-=ammount

                else:
                    input("Not Anough Funds\nPress Enter To Continue")
    except Exception as e:
        print("Error Try Agaim")

def make_deposit():
    print("\n"*100)
    print("Your Balance: ",my_account['balance'],"€")
    try:
        my_account['balance']+=float(input("Deposit Ammount: "))
    except Exception as e:
        #"made by andre"
        print("Error Try Again")
        
def make_withdraw():
    print("\n"*100)
    print("Your Balance: ",my_account['balance'],"€")
    try:
        ammount=float(input("Withdraw Ammount: "))
        if (ammount <= my_account['balance']):
            my_account['balance']-=ammount
    except Exception as e:
        print("Error Try Again")

def view_loans():
    print("\n"*100)
    print("Your Balance: ",my_account['balance'],"€")
    print("\n")
    for i in my_loans:
        #"made by andre"
        print("###")
        print('Loan ID: ',i['id'])
        print('Loan Ammount: ',i['ammount'],"€")
        print('Loan Interest: ',i['interest'],"%")
        print('You Will Pay: ',i['ammount']+(i['ammount']*(i['interest']/100)),"€")
    input("Press Enter To Go Back")

def take_loan():
    print("\n"*100)
    print("Your Balance: ",my_account['balance'],"€")
    print("\n")
    try:
        loan=float(input("Loan Ammount: "))
        print('Loan Ammount: ', loan)
        print('Interest: ', default_loan_interest)
        print("Enter To Continue")
        input("")
        my_account['balance']+=loan+(loan*default_loan_interest/100)
        my_loans.append({
            'id': len(my_loans)+1,
            'ammount': loan,
            'interest': 12
        })
    except Exception as e:
        print("Error Try Again")
        inpu("")

def pay_out_loan():
    print("\n"*100)
    print("Your Balance: ",my_account['balance'],"€")
    print("\n")
    for i in my_loans:
        print("###")
        print('Loan ID: ',i['id'])
        print('Loan Ammount: ',i['ammount'],"€")
        print('Loan Interest: ',i['interest'],"%")
        print('You Will Pay: ',i['ammount']+(i['ammount']*(i['interest']/100)),"€")

    try:
        loan_id=int(input("ID Of Loan: "))
        for i in my_loans:
            pay_out=i['ammount']+(i['ammount']*(default_loan_interest/100))
            if (i['id'] == loan_id):
                if (my_account['balance'] >= pay_out):
                    transactions.append({
                        'id': len(transactions),
                        'ammount': -pay_out,
                        'date': time.time
                    })
                    my_loans.pop(i['id']-1)
                    my_account['balance']-=pay_out
                else:
                    input("Not Anough Funds\nPress Enter To Continue")
    except Exception as e:
        print("Error Try Agaim")

def make_paymnent():
    ref=int(input("Reference: "))
    ammount=float(input("Ammount. "))
    if (my_account['balance'] >= ammount):
        my_account['balance']-=ammount
        transactions.append({
            'id': len(transactions),
            'ammount': -ammount,
            'date': time.time
        })

while True:
    print("\n"*100)
    print("### BANK OF THE POOR ###")
    print("Balance: ", my_account['balance'],"€")
    print("###")
    print("1) View Transactions")   
    print("2) Make A Transaction")   
    print("3) Make A Deposit")
    print("4) Make A withdraw")
    print("5) View Loans")
    print("6) Take A Loan")
    print("7) Pay Out Loan")
    print("8) Make Payment")
    print("0) EXIT")
    print("made by andre")
    try:
        match (int(input("Please Pick An Option: "))):
            case (1):
                view_transactions()
            case (2):
                make_transaction()
            case (3):
                make_deposit()
            case (4):
                make_withdraw()
            case (5):
                view_loans()
            case (6):
                take_loan()
            case (7):
                pay_out_loan()
            case (8):
                make_paymnent()
            case (0):
                break
            case (_):
                pass
    except Exception as e:
        pass