import random
def ran():
    num_ = random.randint(1000, 9999)
    print(num_)
    return num_


def input_answer():
    answer = int(input("Enter answer: "))
    return answer

def check_answer(num_, answer):
    cow = 0
    bull = 0
    while answer != num_:
        for i in range(4):
            if str(answer)[i] == str(num_)[i]:
                cow += 1
            else:
                bull += 1
        print(f"{cow} cow, {bull} bull")
        cow = 0
        bull = 0
        answer = input_answer()
    print("Bingo")


check_answer(ran(), input_answer())
