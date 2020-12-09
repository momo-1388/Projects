from statistics import mean


# This is my code
class klas:
    def __init__(self, age, witgh, hight):
        self.age = sum(age) / len(age)
        self.witgh = sum(witgh) / len(witgh)
        self.hight = sum(hight) / len(hight)

    def return_info(self):
        print((self.age))
        print((self.witgh))
        print((self.hight))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#              This is my Object
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sint(st):
    sty = int(st)
    return sty


def lINT(li):
    lis = li
    list_ = list()
    for i in lis:
        list_.append(sint(i))
    return list_


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n = input()
A_age = input()
A_list_age = A_age.split(' ')
A_witgh = input()
A_list_witgh = A_witgh.split(' ')
A_list_witgh = lINT(A_list_witgh)
A_hight = input()
A_list_hight = A_hight.split(' ')
A_list_hight = lINT(A_list_hight)
A_list_age = lINT(A_list_age)
A = klas(A_list_age, A_list_witgh, A_list_hight)

n = input()
B_age = input()
B_list_age = B_age.split(' ')
B_witgh = input()
B_list_witgh = B_witgh.split(' ')
B_list_witgh = lINT(B_list_witgh)
B_hight = input()
B_list_hight = B_hight.split(' ')
B_list_hight = lINT(B_list_hight)
B_list_age = lINT(B_list_age)
B = klas(B_list_age, B_list_witgh, B_list_hight)

A.return_info()
B.return_info()
# This is my Programer Prossional

if (sum(A_list_hight) / len(A_list_hight)) > (sum(B_list_hight) / len(B_list_hight)):
    print('A')

elif (sum(A_list_hight) / len(A_list_hight)) < (sum(B_list_hight) / len(B_list_hight)):
    print('B')

elif (sum(A_list_hight) / len(A_list_hight)) == (sum(B_list_hight) / len(B_list_hight)):
    if (sum(A_list_witgh) / len(A_list_witgh)) > (sum(B_list_witgh) / len(B_list_witgh)):
        print('A')
    elif (sum(A_list_witgh) / len(A_list_witgh)) < (sum(B_list_witgh) / len(B_list_witgh)):
        print('B')
    else:
        print('Same')
