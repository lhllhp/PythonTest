#----------------------------------------------------------------
import csv
#----------------------------------------------------------------
class transaction:
    def __init__(self, code, date, priceItem, quantity, type, isBuy):
        self.code = code
        self.date = date
        self.priceItem = priceItem
        self.quantity = quantity
        self.type = type
        self.isBuy = isBuy
#----------------------------------------------------------------

with open('transaction.csv') as f:
    reader = csv.reader(f)
    transactions = []

    for row in reader:
        transactionItem = transaction(row[0], row[1], row[2], row[3], row[4], row[5])
        transactions.append(transactionItem)

    del transactions[0]
    totalMoney = 0

    for transactionItem in transactions:
        exchangeRate = 1
        if transactionItem.isBuy == '0':
            exchangeRate = 1.05
        totalMoney += int(transactionItem.priceItem) * int(transactionItem.quantity) * exchangeRate

    print('tong tien: ', totalMoney)
#----------------------------------------------------------------