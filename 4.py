def Uper(word):
    word = word[0].upper() + word[1:].lower()
    return word






list_of = []
n = int(input())
for i in range(n):
    person = input()
    list_of_rezome = person.split('.')
    person = (list_of_rezome[0], Uper(list_of_rezome[1]) +' ' +list_of_rezome[2])
    list_of.append(person)

list_of.sort(key=lambda x: x[0])
for latter in list_of :
    print(latter[0] , latter[1])