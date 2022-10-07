class nhanVien:
    def __init__(self, ten, heSoLuong, soNguoi):
        self.ten = ten
        self.heSoLuong = heSoLuong
        self.soNguoi = soNguoi
        self.luongCoBan = 1260000
        self.giaSanPham = 10000
        self.mucGiamTru = 11000000
        self.motNguoiGiamTru = 3600000
        self.thuNhap = 0
        self.luongThuong = 0
        self.thuNhapChiuThue = 0
        self.thueThuNhap = 0
        self.thucLinh = 0

    def tinhThuNhap(self):
        self.thuNhap = self.luongCoBan * self.heSoLuong + self.luongThuong()
        return self.thuNhap

    def tinhThuNhapChiuThue(self):
        self.thuNhapChiuThue = self.tinhThuNhap() - self.mucGiamTru - self.motNguoiGiamTru * self.soNguoi
        return self.thuNhapChiuThue

    # def tinhThueThuNhap(self):

        
class kinhDoanh(nhanVien):
    def __init__(self, ten, heSoLuong, soNguoi, tiLe):
        super().__init__(ten, heSoLuong, soNguoi)
        self.tiLe = tiLe

    def luongThuong(self):
        return self.luongCoBan * self.tiLe

    def thuNhap(self):
        return self.luongCoBan() + self.luongThuong()

class sanXuat(nhanVien):
    def __init__(self, ten, heSoLuong, soNguoi, sanPham):
        super().__init__(ten, heSoLuong, soNguoi)
        self.sanPham = sanPham

    def luongThuong(self):
        if self.sanPham > 450:
            return (self.sanPham - 450) * self.giaSanPham
        
        return 0

    def thuNhap(self):
        return self.luongCoBan() + self.luongThuong()

    