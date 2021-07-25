def input_number():
    num_ = int(input("Hay nhap so: "))
    return num_

def input_base():
    base = int(input("Hay nhap he co so: ")) 
    if 2 <= base <= 32:
        return base
    else:
        print("Nhap sai he co so")
        exit()

def change_number(base, num_):
    num1 = num_
    m = 0
    sb = ""
    k = 0
    h = 0
    count = 0
    while num_ > 0:
        if base >= 10:
            m  = num_ % base
            if 10 <= m <= base - 1:
                sb = sb + str(chr(55 + m))
            else:
                sb = sb + str(m)
            num_ = int(num_/base)
        else:
            sb  = sb + str(num_ % base)
            num_ = int(num_ / base)
    print(f"He co so {base} cua so nguyen {num1} la: {sb[::-1]}")

change_number(input_base(), input_number())

