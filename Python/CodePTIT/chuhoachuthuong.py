"""
Cho một xâu ký tự chỉ bao gồm các ký tự chữ cái, độ dài không quá 100. Hãy thực hiện:
Biến đổi tất cả xâu thành viết thường, nếu số lượng chữ cái viết thường lớn hơn hoặc bằng số lượng chữ cái viết 
hoa.
Biến đổi tất cả xâu thành chữ hoa, nếu số lượng chữ cái viết hoa lớn hơn số lượng chữ cái viết thường.
Input
"""
def bien_doi_xau(s):
    so_luong_chu_hoa = sum(1 for c in s if c.isupper())
    so_luong_chu_thuong = len(s) - so_luong_chu_hoa
    if so_luong_chu_hoa > so_luong_chu_thuong:
        return s.upper()
    else:
        return s.lower()
s = input()
print(bien_doi_xau(s))  # Kết quả: "abc"
