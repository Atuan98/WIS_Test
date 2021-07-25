def input_number():
    num_ = int(input("Hay nhap so: "))
    return num_


def check_number(num_):
    if num_ % 2 == 0:
        print(f"So {num_} la so chan")
    else:
        print(f"So {num_} la so le")

check_number(input_number())
