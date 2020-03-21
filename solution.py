import csv
from collections import OrderedDict

# ICICI-Input-Case2.csv  HDFC-Input-Case1.csv
with open('ICICI-Input-Case2.csv', newline='') as csvFile:
  obj = csv.DictReader(csvFile)
  reader = csv.reader(csvFile)
  outData = []
  transaction = obj.fieldnames[1].split()[0]

  for row in reader:
    if row[0] == '' and row[1]:
      last = row[1].split(' ')[-1]
      if last.capitalize() == 'Transactions':
        transaction = row[1].split()[0]
      else:
        cardName = row[1]

    if transaction.capitalize() == 'Domestic':
      currency = 'INR'

    if row[0] and row[0][:4] != 'Date':
      date = row[0]
      trDes = ' '.join(row[1].split()[:-1])
      location = row[1].split()[-1]
    
      if transaction.capitalize() == 'International':
        trDes = ' '.join(row[1].split()[:-2])
        currency = row[1].split()[-1]
        location = row[1].split()[-2]

      if len(row) == 3:
        if row[2].split()[-1] == 'cr':
          credit = row[2].split()[0]
          debit = 0
        else:
          credit = 0
          debit = row[2].split()[0]
      elif len(row) == 4:
        if row[3]:
          credit = row[3]
          debit = 0
        else:
          debit = row[2]
          credit = 0
      outRow = (date, trDes, debit, credit, currency,
      cardName, transaction, location)
      outData.append(outRow)

with open('output_case2.csv', 'w', newline='') as outFile:
  fields = ['Date', 'Transaction Description', 'Debit',
   'Credit', 'Currency', 'Card Name', 'Transaction', 'Location']
  obj = csv.DictWriter(outFile, fieldnames=fields)
  obj.writeheader()
  writer = csv.writer(outFile)
  for row in outData:
    writer.writerow(row)

