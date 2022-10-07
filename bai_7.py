#----------------------------------------------------------------
#LIB
#----------------------------------------------------------------
class cd:
    def __init__(self, cd_name, cd_singer, song_number, price):
        self.cd_name = cd_name
        self.cd_singer = cd_singer
        self.song_number = song_number
        self.price = price
#----------------------------------------------------------------
# FUNC
#----------------------------------------------------------------
import csv
with open('cd_info.csv') as f:
    reader = csv.reader(f)
    cd_list = []

    for row in reader:
        cd_item = cd(row[0], row[1], row[2], row[3])
        cd_list.append(cd_item)

    del cd_list[0]
    total_money = 0
    for cd in cd_list:
        print('ten cd:', cd.cd_name)
        print('ten ca si:', cd.cd_singer)
        print('so bai hat:', cd.song_number)
        print('gia tien:', cd.price)
        total_money += int(cd.price)
    print('tong tien: ', total_money)
