# def tinhGiaiThua(n):
#     s = 1
#     if (s == 0):
#         print(0)
#     else:
#         for i in range(1, n+1):
#             s *= i
#     return s
# def tinhFibonaci(n):
#     if n < 1:
#         print(1)
#     elif n < 3:
#         for i in range(1, n + 1):
#             print(1)
#     else:
#         print(1)
#         print(1)
#         a = b = s = 1
#         for i in range(3, n + 1):
#             s = a + b
#             a = b
#             b = s
#             print(s)
# def kiemTraSoNguyenTo(n):
#     if n < 2:
#         print('Khong phai so nguyen to')
#         return 
#     for i in range(2, (n+1) / 2):
#         if n % i == 0:
#             print('Khong phai so nguyen to')
#             return 
#     print('La so nguyen to')
# n = int(input('Nhap so n:'))
# tinhFibonaci(n)
# kiemTraSoNguyenTo(n)
def check100YearsOld(perName, perYearsOld):
    import time
    currentYear = time.localtime().tm_year
    yearsOld = currentYear - perYearsOld + 100
    print('Vao nam', yearsOld, perName, 'se duoc 100 tuoi')
perName = str(input('Nhap ten cua ban:'))
age = int(input('Nhap tuoi cua ban:'))
check100YearsOld(perName, age)
