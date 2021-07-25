
def input_number():
    num_ = int(input("Hay nhap so: "))
    if num_ < 0:
        print("So nhap vao phai > 0")
        exit()
    else:
        return num_

def check_number(num_):
    num1 = round(num_/2)
    count = 0
    for i in range(2,num1 + 1):
        if num_ % i == 0:
            count += 1
    if count == 0:
        print(f"So {num_} la so nguyen to")
    else:
        print(f"So {num_} khong la so nguyen to")

check_number(input_number())