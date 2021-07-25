def input_number():
    num_ = int(input("Hay nhap so muon tinh giai thua: "))
    if num_ < 0:
        print("So nhap vao phai > 0")
        exit()
    else:
        return num_

def giai_thua(num_):
    if num_ == 1:
        return 1
    return num_ * giai_thua(num_ - 1)


print(giai_thua(input_number()))