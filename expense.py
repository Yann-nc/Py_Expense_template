from PyInquirer import prompt
import csv

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

]



def new_expense(*args):
    infos = prompt(expense_questions)
    
    # Parses the input
    amount = infos.get('amount')
    label = infos.get('label')
    spender = infos.get('spender')
    
    # Creates the line to add to the csv file
    data = [ amount, label, spender]
    
    # Writes the informations on external file : expense_report.csv
    with open('expense_report.csv', 'a', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    
    print(spender, " payed ", amount, " for : ", label)
    print("Expense Added ! -> ", spender, " payed ", amount, " for : ", label)
    
    return True


