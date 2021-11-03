from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"username",
        "message":"New user - Username: ",
    }
]


def add_user(*args):
    infos = prompt(user_questions)
    
    # Parses the input
    username = infos.get('username')
    
    # Creates the line to add to the csv file
    data = [username]
    
    # Writes the informations on external file : expense_report.csv
    with open('users.csv', 'a', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    
    print("User : ", username, " Added !")
    
    return True