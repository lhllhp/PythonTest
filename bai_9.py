class hinh:
    def __init__(self, ten, dinh_nghia):
        self.ten = ten
        self.dinh_nghia = dinh_nghia
        
class vuong(hinh):
    def __init__(self, ten, dinh_nghia):
        super().__init__('vuong', '4 canh bang nhau va co 1 goc vuong')

class thoi(hinh):
    def __init__(self, ten, dinh_nghia):
        super().__init__('thoi', '4 canh bang nhau')

class binh_hanh(hinh):
    def __init__(self, ten, dinh_nghia):
        super().__init__('binh hanh', '2 cap canh doi song song')

class chu_nhat(hinh):
    def __init__(self, ten, dinh_nghia):
        super().__init__('chu nhat', '2 cap canh doi song song va co 1 goc vuong')

class tron(hinh):
    def __init__(self, ten, dinh_nghia):
        super().__init__('tron', 'khoang cach tu cac diem tren duong tron den 1 tam la hang so')

class tam_giac(hinh):
    def __init__(self, ten, dinh_nghia):
        super().__init__('tam giac', 'co 3 canh')

class da_giac(hinh):
    def __init__(self, ten, dinh_nghia):
        super().__init__('da giac', 'co nhieu canh')

class ngu_giac(hinh):
    def __init__(self, ten, dinh_nghia):
        super().__init__('ngu giac', 'co 5 canh')