# f = open('test.text', 'r')
# f1 = open('odd.text', 'w')
# f2 = open('even.text', 'w')
# odd = even = []

# for item in f:
#     num = int(item)
#     if num % 2 == 0:
#         f2.write(str(num) + "\n")
#     else:
#         f1.write(str(num) + "\n")

# f.close()
# f1.close()
# f2.close()

import csv

with open('users.csv') as f:
    reader = csv.reader(f)