"""
# 💰 Personal Finance Snapshot
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

NAME = 'Sateesh'
MONTHLY_INCOME = 50000
RENT = 12500.00
GROCERIES = 3200.75
TRANSPORT = 1800.00
IS_SAVING = True

TOTAL_EXPENSES = RENT + GROCERIES + TRANSPORT
SAVINGS = MONTHLY_INCOME - TOTAL_EXPENSES
SAVINGS_PERCENTAGE = (SAVINGS / MONTHLY_INCOME) * 100
TAX = MONTHLY_INCOME * 0.10

print(f"👤 Name: {NAME}")
print(f"💵 Monthly Income: ₹{MONTHLY_INCOME}")
print(f"💸 Total Expenses: ₹{TOTAL_EXPENSES:.2f}")
print(f"🐷 Savings: ₹{SAVINGS:.2f} ({SAVINGS_PERCENTAGE:.1f}%)")
print(f"📊 Tax @10%: ₹{TAX:.2f}")
print(f"✅ Saving mode : {IS_SAVING}")
