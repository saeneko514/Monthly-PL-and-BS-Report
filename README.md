# Monthly PL and BS Report Generator

This project automates the generation of monthly Profit & Loss (PL) and Balance Sheet (BS) reports from journal entry data in CSV format.  
The output is an Excel workbook containing separate sheets for each month's PL and BS summaries.

## Features

- Reads journal entries CSV with columns: Date, Account, Debit, Credit, Description, Month
- Automatically groups data by month
- Calculates net amounts for PL accounts and balances for BS accounts
- Exports monthly PL and BS reports to an Excel file with separate sheets
- Easily customizable account categories for PL and BS

## Requirements

- Python 3.x
- pandas
- openpyxl

Install dependencies using pip:

```bash
pip install pandas openpyxl


## Usage
1. Prepare your journal entries CSV file with the following columns:

Date (YYYY-MM-DD)
Account
Debit
Credit
Description
Month (optional, will be auto-generated if missing)

2. Run the script:
python main.py

3. Check the generated Excel file monthly_PL_and_BS.xlsx in the project directory.

## Customization
Modify the pl_accounts and bs_accounts lists in the script to match your chart of accounts.
Adjust the grouping or calculations as needed for your specific accounting policies.
