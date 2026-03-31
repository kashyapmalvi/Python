dic = {
    101:50,
    102:30,
    103:40,
    104:50,
    105:25
}

heighestmark = max(dic,key=dic.get) # Heigest mark
print(heighestmark)


dic[102] = 50
print({dic[102]})

dic.pop(105)
print(dic)


for roll,mark in dic.items():
    print({roll},{mark})





