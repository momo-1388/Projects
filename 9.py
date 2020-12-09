from random import randint

class ensan:
    def __init__(self, name):
        self.name = name


    def return_name(self):
        return self.name


def return_number():
    num = randint(1,2)
    if fottball.A == 0 :
        num = 2
    if fottball.B == 0 :
        num = 1
    if num == 1 :
        fottball.A -= 1
        return 'A'
    elif num == 2 :
        fottball.B -= 1
        return 'B'
    else :
        pass


class fottball(ensan):
    A = 11
    B = 11


o1 = fottball('hosein')
o2 = fottball('maziar')
o3 = fottball('akbar') 
o4 = fottball('nima')
o5 = fottball('mahdi') 
o6 = fottball('farhad')
o7 = fottball('mohammad')
o8 = fottball('khashaiar')
o9 = fottball('milad')
o10 = fottball('mostafa')
o11 = fottball('amin')
o12 = fottball('said')
o13 = fottball('pouya')
o14 = fottball('pourya')
o15 = fottball('reza')
o16 = fottball('ali')
o17 = fottball('behzad')
o18 = fottball('soheil')
o19 = fottball('behroz')
o20 = fottball('shahroz')
o21 = fottball('saman')
o22 = fottball('mohsen')

print('%s : %s' % (o1.return_name(), return_number()))
print('%s : %s' % (o2.return_name(), return_number()))
print('%s : %s' % (o3.return_name(), return_number()))
print('%s : %s' % (o4.return_name(), return_number()))
print('%s : %s' % (o5.return_name(), return_number()))
print('%s : %s' % (o6.return_name(), return_number()))
print('%s : %s' % (o7.return_name(), return_number()))
print('%s : %s' % (o8.return_name(), return_number()))
print('%s : %s' % (o9.return_name(), return_number()))
print('%s : %s' % (o10.return_name(), return_number()))
print('%s : %s' % (o11.return_name(), return_number()))
print('%s : %s' % (o12.return_name(), return_number()))
print('%s : %s' % (o13.return_name(), return_number()))
print('%s : %s' % (o14.return_name(), return_number()))
print('%s : %s' % (o15.return_name(), return_number()))
print('%s : %s' % (o16.return_name(), return_number()))
print('%s : %s' % (o17.return_name(), return_number()))
print('%s : %s' % (o18.return_name(), return_number()))
print('%s : %s' % (o19.return_name(), return_number()))
print('%s : %s' % (o20.return_name(), return_number()))
print('%s : %s' % (o21.return_name(), return_number()))
print('%s : %s' % (o22.return_name(), return_number()))