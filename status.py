import sys
import csv
from types import new_class

def show_status():
    
    # Loading all the users
    users = {}
    
    with open("users.csv", "r") as file:
        for line in file:
            users.update({line[:-1]: 0})
            
    # print("Users : ", users, file=sys.stderr)
    
    # Taking every line of the expense report into account
    with open("expense_report.csv", "r") as file:
        for row in file:
            expense = list(csv.reader([row]))[0]
            amount = expense[0]
            spender = expense[2]
            spendees = list(csv.reader(expense[3:]))[0]
            # print("Amount : ", amount, " Spender : ", spender," Spendees : ", spendees, file=sys.stderr)
    
            users.update({spender: int(amount) + int(users[spender])})
            
            for spendee in spendees:
                if (spendee != spender):
                    users.update({spendee: int(users[spender]) - (int(amount) / len(spendees))})
    
        print("Users : ", users, file=sys.stderr)
    
    return True