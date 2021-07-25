def input_str():
    chuoi = input("Hay nhap 1 chuoi de kiem tra: ")
    return chuoi

def check_str(chuoi):
    chuoi2 = chuoi
    chuoi1 = chuoi[::-1]
    print(f"Chuoi1 = {chuoi1}, Chuoi2 = {chuoi2}")
    if chuoi1 == chuoi2:
        print(f"Chuoi {chuoi2} la palindrome ")
    else:
        print(f"Chuoi {chuoi2} khong la palindrome ")


check_str(input_str())