def input_number():
    num_ = int(input("Hay nhap so luong so trong day fibonaci can tao: "))
    if num_ < 0:
        print("So nhap vao phai > 0")
        exit()
    else:
        return num_


def insert_number(num_):
    list1 = []
    for i in range(num_):
        if i < 2 :
            list1.append(1)
        if i >= 2:
            list1.append(list1[i-1] + list1[i-2])
    print(list1)

insert_number(input_number())
        

