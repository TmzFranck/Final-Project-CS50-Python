import json
import csv
from pyfiglet import Figlet
from tabulate import tabulate
import os
import re
from tqdm import tqdm
import time
import sys
from datetime import datetime

all_transactions = []

def filter_transaction_incone_expense(transactions, income_expense):
    filter_transactions = [transaction for transaction in transactions if transaction["category"] == income_expense]
    filter_transactions.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))
    return filter_transactions

def check_date(date):
    matches = re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", date)
    if not matches:
        return False
    else:
        if int(matches.group(2)) > 12 or int(matches.group(2)) == 0:
            return False
        elif int(matches.group(3)) > 31 or int(matches.group(3)) == 0:
            return False
    return True




def add_transaction(date, amount, category, description, transactions):
    transaction = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }
    transactions.append(transaction)
    transactions.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))



def filter_transaction_date(start_date, end_date, transactions):
    filter_transactions = list(filter(lambda x: x["date"] >= start_date and x["date"] <= end_date, transactions))
    filter_transactions.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))
    return filter_transactions



def remove_transaction(id, transactions):
    transactions.pop(id)


def import_data(file_name, transactions):
        with open (f"{file_name}.csv", 'r') as file:
                reader = csv.DictReader(file)
                transaction =  [row for row in reader]
        for i in transaction:
            transactions.append(i)
        transactions.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))



def export_all_data(file_name, format, transactions):
    if format == "csv":
        with open(f"{file_name}.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'amount', 'category', 'description'])
            writer.writeheader()
            for transaction in transactions:
                writer.writerow(transaction)
    elif format == "json":
        with open(f"{file_name}.json", "w") as file:
            json.dump(transactions, file)
    else:
        raise ValueError("Wrong extension file")



def main():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        f = Figlet(font='slant')
        print(f.renderText('Finance Tracker'))
        while True:
            output = [
                {"id" : "1",
                "choice" : "Add transaction"},
                {"id" : "2",
                "choice" : "Remove transaction"},
                {"id" : "3",
                "choice" : "List transactions"},
                {"id" : "4",
                "choice" : "Import transaction"},
                {"id" : "5",
                "choice" : "Export transaction"},
                {"id" : "0",
                "choice" : "Quit"},
            ]

            print(tabulate(output, headers="keys", tablefmt="heavy_grid"))

            choice = input('Enter your choice: ')

            if matches := re.search(r"^([0-9]{1})$", choice):
                if matches.group(1) == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    date = input("Enter the date (YYYY-MM-DD): ")

                    while not check_date(date):
                        print("Invalid date. Please try again, Date format is YYYY-MM-DD")
                        date = input("Enter the date (YYYY-MM-DD): ")

                    amount = input("Enter the amount: ")
                    while not re.search(r"^([0-9]*)(\.?[0-9]+)$", amount):
                        print("Invalid amount. Please try again.")
                        amount = input("Enter the amount: ")

                    category = input("Enter the caregory (income or expense): ")
                    while not category in ("income", "expense"):
                        print("Invalid category. Please try again. Valid categories are income and expense.")
                        category = input("Enter the caregory (income or expense): ")


                    description = input("Enter the description: ")

                    add_transaction(date, amount, category, description, all_transactions)
                    print("================================transaction added successfully.=============================================")

                elif matches.group(1) == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if len(all_transactions) == 0:
                        print("No transactions to remove.")
                        continue
                    else:
                        print("all transactions: ")
                        print(tabulate(all_transactions, headers="keys", tablefmt="heavy_grid"))
                        while True:
                            try:
                                index = int(input(f"Enter the index of the transaction you want to remove (0 - {len(all_transactions) - 1}): "))
                                break
                            except ValueError:
                                continue

                        remove_transaction(index, all_transactions)
                        print("============================Transaction removed successfully.====================================")

                elif matches.group(1) == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    choices = input("list transactions by income(I), expense(E) or filter transactions by date(D) or list all transactions(A) (choice: I, E, D, A): ")
                    while not choices in ("I", "E", "D", "A"):
                        choices = input("choice: I, E, D or A: ")

                    if choices == "I":
                        filter_transactions = filter_transaction_incone_expense(all_transactions, "income")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(tabulate(filter_transactions, headers="keys", tablefmt="heavy_grid"))
                        print("================================================================")
                    elif choices == "E":
                        filter_transactions = filter_transaction_incone_expense(all_transactions, "expense")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(tabulate(filter_transactions, headers="keys", tablefmt="heavy_grid"))
                        print("================================================================")
                    elif choices == "D":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        start_date = input("Enter the start date (YYYY-MM-DD): ")
                        while not re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", start_date):
                            print("Invalid date. Please try again, Date format is YYYY-MM-DD: ")
                            start_date = input("Enter the start date (YYYY-MM-DD): ")

                        end_date = input("Enter the end date (YYYY-MM-DD): ")
                        while not re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", end_date):
                            print("Invalid date. Please try again, Date format is YYYY-MM-DD: ")
                            end_date = input("Enter the end date (YYYY-MM-DD): ")
                        filter_transactions = filter_transaction_date(start_date, end_date, all_transactions)
                        print(tabulate(filter_transactions, headers="keys", tablefmt="heavy_grid"))
                        print("================================================================")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if len(all_transactions) == 0:
                            print("No transactions.")
                        else:
                            print(tabulate(all_transactions, headers="keys", tablefmt="heavy_grid"))
                        print("================================================================")



                elif matches.group(1) == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    file_name = input("Enter the file name without extensions: ")
                    import_data(file_name, all_transactions)
                    for _ in tqdm (range (101), desc="Loading…", ascii=False, ncols=75):
                        time.sleep(0.01)

                    print("Complete.")

                elif matches.group(1) == "5":
                    file_name = input("Enter the file name without extensions: ")
                    format = input("Enter the file extensions (json or csv): ")
                    while not format in ("json", "csv"):
                        format = input("json or csv")

                    export_all_data(file_name, format, all_transactions)
                    for _ in tqdm (range (101), desc="Loading…", ascii=False, ncols=75):
                        time.sleep(0.01)

                    print("Complete.")
                elif matches.group(1) == "0":
                    sys.exit("Close.................")

            else:
                print("invalid Input")
                continue

    except (KeyboardInterrupt, EOFError):
        sys.exit('\nClose.......')



if __name__ == "__main__":
    main()
