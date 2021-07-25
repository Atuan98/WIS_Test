def input_number():
    num_ = input("Hay nhap chuoi so: ")
    return num_


def check_number(num_):
    num1 = ''
    str_ = ''
    for i in range(len(num_)):
        if num_[i] != ',':
            num1 += num_[i]
        else:
            if int(num1,2) % 5 == 0:
                print(int(num1,2))
                str_ += num1 + ', '
            num1 = ''
    print(str_)


check_number(input_number())