"""
Cho một xâu ký tự độ dài không quá 100 chỉ bao gồm các chữ cái in hoa. Người ta thực hiện mã hóa bằng cách đếm các ký tự cạnh 
nhau giống nhau và viết số lượng phía sau các chữ cái đó.
Ví dụ xâu AAECCCCGGGD thì được mã hóa thành A2E1C4G3D1
Với giả thiết không có ký tự nào xuất hiện nhiều hơn 9 lần liên tiếp.
Cho trước xâu kết quả mã hóa. Hãy khôi phục xâu ký tự ban đầu tương ứng.

Input
Dòng đầu ghi số bộ test. Mỗi bộ test ghi xâu mã hóa.

Output
Với mỗi test ghi ra xâu ký tự ban đầu
Ex: 
A8 -> AAAAAAAA
A2E1C4G3D1 -> AAECCCCGGGD
"""
t = int(input())
for _ in range(t):
    txt = input()
    m = []
    n = []
    for i in range(len(txt)):
        if txt[i].isalpha():
            m.append(txt[i])
        else:
            n.append(int(txt[i]))
    result = ''
    for i in range(len(m)):
        result += m[i] * n[i]
    print(result)