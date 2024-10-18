# PERSONAL FINANACE TRACKER
#### Video Demo:  https://youtu.be/WBmuwTaDfuY
#### Description:
The Finance Tracker is a comprehensive command-line application developed in Python, designed to help users manage their financial transactions effectively. This tool allows users to add, remove, list, filter, import, and export transactions with ease, providing a versatile solution for tracking income and expenses.

The application begins by displaying a stylized title using pyfiglet and offers a main menu with various options. Users can add new transactions by inputting the date, amount, category (income or expense), and description. The date input is validated to ensure it follows the correct format and logical constraints, while the amount and category are also checked for correctness.

Removing transactions is straightforward; users are presented with a list of all transactions and can specify the index of the transaction they wish to delete. Listing transactions is highly flexible, allowing users to view all transactions, filter by income or expense, or specify a date range for filtering.

The Finance Tracker also supports importing transactions from CSV files, making it easy to integrate with other financial tools or historical data. Exporting transactions is equally versatile, with options to export data in either CSV or JSON format, facilitating data sharing and backup.

The application leverages several Python libraries for its functionality:

- json and csv for data handling.
- pyfiglet for creating ASCII art text.
- tabulate for displaying data in a readable tabular format.
- os and sys for system operations.
- re for regular expression operations.
- tqdm for progress bars during data import/export.
- time for managing sleep intervals.
- datetime for date manipulation.
Error handling and input validation are integral parts of the script, ensuring a smooth user experience. The main menu is designed to be intuitive, allowing users to navigate through options with ease. The Finance Tracker's modular design makes it easy to extend or modify catering to a wide range of personal finance management needs.

Overall, the Finance Tracker is a powerful tool for anyone looking to keep a detailed and organized record of their financial transactions, offering a blend of simplicity, flexibility, and comprehensive functionality.
