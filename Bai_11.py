class tron():
    def dienTich(self):
        return self.r * self.r * 3.14

    def chuVi(self):
        return self.r * 2 * 3.14

    def xuLy(self):
        print('Chu vi la:', self.chuVi())
        print('Dien tich la:', self.dienTich())

    def nhapThongTin(self):
        self.r = int(input('Ban kinh hinh tron la:'))

class vuong():
    def dienTich(self):
        return self.a * self.a

    def chuVi(self):
        return self.a * 4

    def xuLy(self):
        print('Chu vi la:', self.chuVi())
        print('Dien tich la:', self.dienTich())

    def nhapThongTin(self):
        self.a = int(input('Canh hinh tron la:'))

class chuNhat():
    def dienTich(self):
        return self.a * self.b

    def chuVi(self):
        return (self.a + self.b) * 2

    def xuLy(self):
        print('Chu vi la:', self.chuVi())
        print('Dien tich la:', self.dienTich())

    def nhapThongTin(self):
        self.a = int(input('Chieu dai hinh chu nhat la:'))
        self.b = int(input('Chieu rong hinh chu nhat la:'))

class binhHanh():
    def dienTich(self):
        return self.a * self.h

    def chuVi(self):
        return (self.a + self.b) * 2

    def xuLy(self):
        print('Chu vi la:', self.chuVi())
        print('Dien tich la:', self.dienTich())

    def nhapThongTin(self):
        self.a = int(input('Chieu dai hinh binh hanh la:'))
        self.b = int(input('Chieu rong hinh binh hanh la:'))
        self.h = int(input('Chieu cao hinh binh hanh la:'))

class tamGiac():
    def dienTich(self):
        return self.a * self.h / 2

    def chuVi(self):
        return self.a + self.b + self.c

    def xuLy(self):
        print('Chu vi la:', self.chuVi())
        print('Dien tich la:', self.dienTich())

    def nhapThongTin(self):
        self.a = int(input('Chieu dai canh 1 cua tam giac la:'))
        self.b = int(input('Chieu dai canh 2 cua tam giac la:'))
        self.c = int(input('Chieu dai canh 3 cua tam giac la:'))
        self.h = int(input('Chieu cao cua tam giac la:'))

while (True):
    print("Chon hinh:")
    print('1. Hinh tron')
    print('2. Hinh vuong')
    print('3. Hinh chu nhat')
    print('4. Hinh binh hanh')
    print('5. Hinh tam giac')

    chon = int(input())

    if chon == 1 :
        a = tron()
        a.nhapThongTin()
        a.xuLy()
    elif chon == 2:
        a = vuong()
        a.nhapThongTin()
        a.xuLy()
    elif chon == 3:
        a = chuNhat()
        a.nhapThongTin()
        a.xuLy()
    elif chon == 4:
        a = binhHanh()
        a.nhapThongTin()
        a.xuLy()
    elif chon == 5:
        a = tamGiac()
        a.nhapThongTin()
        a.xuLy()
    else:
        print('Nhap sai')

    tiepTuc = input('Ban co muon tiep tuc:(y/n)')

    if tiepTuc == 'n':
        break