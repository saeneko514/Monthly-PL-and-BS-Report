import pandas as pd

# 仕訳データの読み込み
df = pd.read_csv("journal_data.csv", parse_dates=["Date"])

# 月列の追加（例: 2025-01）
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# PL科目とBS科目を定義（必要に応じて追加・変更可能）
pl_accounts = [
    "Sales", "Cost of Goods Sold", "Operating Expenses", "Salaries Expense",
    "Utilities", "Advertising", "Depreciation", "Interest Expense", "Owner's Capital"
]
bs_accounts = [
    "Cash", "Accounts Receivable", "Inventory", "Fixed Assets",
    "Accounts Payable", "Long-term Debt", "Equity"
]

# Excelライターを作成
with pd.ExcelWriter("monthly_PL_and_BS.xlsx", engine="openpyxl") as writer:
    any_written = False  # シートが書き出されたかどうかのフラグ

    for month, data in df.groupby("Month"):
        # 損益計算書（PL）
        pl = data[data["Account"].isin(pl_accounts)]
        if not pl.empty:
            pl_summary = pl.groupby("Account")[["Debit", "Credit"]].sum()
            pl_summary["Net"] = pl_summary["Credit"] - pl_summary["Debit"]
            pl_summary = pl_summary[["Net"]].rename(columns={"Net": f"{month} Profit/Loss"})
            pl_summary.to_excel(writer, sheet_name=f"{month}_PL")
            any_written = True

        # 貸借対照表（BS）
        bs = data[data["Account"].isin(bs_accounts)]
        if not bs.empty:
            bs_summary = bs.groupby("Account")[["Debit", "Credit"]].sum()
            bs_summary["Balance"] = bs_summary["Debit"] - bs_summary["Credit"]
            bs_summary = bs_summary[["Balance"]].rename(columns={"Balance": f"{month} Balance"})
            bs_summary.to_excel(writer, sheet_name=f"{month}_BS")
            any_written = True

    if not any_written:
        raise ValueError("❌ No sheets were written. Please check if your input data is empty or incorrectly filtered.")

print("✅ PL and BS reports saved to 'monthly_PL_and_BS.xlsx'")
