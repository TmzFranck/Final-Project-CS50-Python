import os
from datetime import datetime
import csv
from project import filter_transaction_incone_expense, add_transaction, filter_transaction_date, remove_transaction, import_data, export_all_data, check_date

def test_filter_transaction_incone_expense():
    transactions = [
        {"date" : "2020-02-01",
         "amount": "111.12",
         "category": "expense",
         "description": "restaurant",
         },
         {"date" : "2022-12-01",
         "amount": "50",
         "category": "expense",
         "description": "shopping",
         },
         {"date" : "2020-02-01",
         "amount": "5000",
         "category": "income",
         "description": "salary",
         }
         ]
    filter_transactions = filter_transaction_incone_expense(transactions, "income")
    assert filter_transactions == [{"date" : "2020-02-01",
         "amount": "5000",
         "category": "income",
         "description": "salary",
         }]

    filter_transactions = filter_transaction_incone_expense(transactions, "expense")
    assert filter_transactions == [{"date" : "2020-02-01",
         "amount": "111.12",
         "category": "expense",
         "description": "restaurant",
         },
         {"date" : "2022-12-01",
         "amount": "50",
         "category": "expense",
         "description": "shopping",
         }]




def test_add_transaction():
    transactions = []
    add_transaction("2020-01-01", 1111.2, "income", "salary", transactions)
    add_transaction("2020-02-01", 50, "expense", "restaurant", transactions)
    assert len(transactions) == 2
    assert 50 in [x["amount"] for x in transactions]
    assert 1111.2 in [x["amount"] for x in transactions]



def test_filter_transaction_date():
    transactions = [
        {"date" : "2024-02-01",
         "amount": "111.12",
         "category": "expense",
         "description": "restaurant",
         },
         {"date" : "2010-12-01",
         "amount": "50",
         "category": "expense",
         "description": "shopping",
         },
         {"date" : "2015-02-01",
         "amount": "5000",
         "category": "income",
         "description": "salary",
         }
         ]

    filter_transactions = filter_transaction_date("2015-01-01", "2016-01-01", transactions)
    assert filter_transactions == [{"date" : "2015-02-01",
         "amount": "5000",
         "category": "income",
         "description": "salary",
         }]


def test_remove_transaction():
    transactions = [
        {"date" : "2020-02-01",
         "amount": "111.12",
         "category": "expense",
         "description": "restaurant",
         },
         {"date" : "2022-12-01",
         "amount": "50",
         "category": "expense",
         "description": "shopping",
         },
         {"date" : "2020-02-01",
         "amount": "5000",
         "category": "income",
         "description": "salary",
         }
         ]

    tmp = [
        {"date" : "2020-02-01",
         "amount": "111.12",
         "category": "expense",
         "description": "restaurant",
         },
         {"date" : "2022-12-01",
         "amount": "50",
         "category": "expense",
         "description": "shopping",
         },
         {"date" : "2020-02-01",
         "amount": "5000",
         "category": "income",
         "description": "salary",
         }
         ]
    remove_transaction(0, transactions)
    assert len(transactions) == 2
    assert [i for i in tmp if i not in transactions] == [{"date" : "2020-02-01",
         "amount": "111.12",
         "category": "expense",
         "description": "restaurant",
         }]

def test_import_data():
    transactions = [
        {"date" : "2020-02-01",
         "amount": "111.12",
         "category": "expense",
         "description": "restaurant",
         },
         {"date" : "2022-12-01",
         "amount": "50",
         "category": "expense",
         "description": "shopping",
         },
         {"date" : "2020-02-01",
         "amount": "5000",
         "category": "income",
         "description": "salary",
         }
         ]
    with open("csv_test.csv" ,"w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'amount', 'category', 'description'])
        writer.writeheader()
        for transaction in transactions:
            writer.writerow(transaction)

    extract_transactions = []
    import_data("csv_test", extract_transactions)
    transactions.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))
    extract_transactions.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))

    assert [i for i in transactions if i not in extract_transactions] == []
    os.remove("csv_test.csv")


def test_export_all_data():
    transactions = [
        {"date" : "2020-02-01",
         "amount": "111.12",
         "category": "expense",
         "description": "restaurant",
         },
         {"date" : "2022-12-01",
         "amount": "50",
         "category": "expense",
         "description": "shopping",
         },
         {"date" : "2020-02-01",
         "amount": "5000",
         "category": "income",
         "description": "salary",
         }
         ]
    export_all_data("csv_file", "csv", transactions)
    export_all_data("json_file", "json", transactions)

    assert os.path.exists("csv_file.csv") == True
    assert os.path.exists("json_file.json") == True
    os.remove("csv_file.csv")
    os.remove("json_file.json")

def test_check_date():
    assert check_date("2022-01-01") == True
    assert check_date("2034-22-33") == False
    assert check_date("2022-13-01") == False
    assert check_date("2033-111-01") == False
    assert check_date("ksadfksdf") == False
