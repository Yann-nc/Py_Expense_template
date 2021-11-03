from PyInquirer import prompt
import csv
import sys

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
    {
        "type":"input",
        "name":"spendees",
        "message":"New Expense - Spendees: ",
    },

]

def new_expense(*args):
    infos = prompt(expense_questions)
    
    # Parses the input
    amount = infos.get('amount')
    label = infos.get('label')
    spender = infos.get('spender')
    spendee_list = infos.get('spendees')
    # print("Spendees : ", spendee_list, file=sys.stderr)
    spendees = list(csv.reader([spendee_list]))[0]
    # print("Spendees : ", spendees, file=sys.stderr)
    
    # Checks
    ## Check if spender exists (if it's an existing user)
    ### Put all the users in a set 
    users = { '' }
    users.clear()

    with open("users.csv", "r") as file:
        for line in file:
            line = line[:-1]
            users.add(line)

    # print("Users : ", users, file=sys.stderr)
    
    if (spender not in users):
        print("You can't add an expense from an unknown user !")
        return False
    
    ## Check if Spender is amongst Spendee
    
    if (spender not in spendees):
        print("Spender : ", spender, file=sys.stderr)
        print("Spendees : ", spendees, file=sys.stderr)
        print("The spender has to be amongst the spendees")
        return False
    
    ## Check if all spendees are users
    for spender_ in spendees:
        if (spender_ not in users):
            print("Users : ", users, file=sys.stderr)
            print("Spendees : ", spendees, file=sys.stderr)
            print("All the spendees have to be users", file=sys.stderr)
            return False
    
    # Creates the line to add to the csv file
    data = [ amount, label, spender, spendee_list]
    
    # Writes the informations on external file : expense_report.csv
    with open('expense_report.csv', 'a', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    
    print("Expense Added ! -> ", spender, " payed ", amount, " for : ", label)
    
    return True
