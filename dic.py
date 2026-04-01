dic = {
    
    101:25,
    102:55,
    103:15,
    104:85,
    105:45
}
maxxvalue = max(dic.values())

for roll,marks in dic.items():
    if marks == maxxvalue:
        print(roll,marks)
        
    dic[101] = {120} #update

delete = 101
del dic[delete]
print(dic)


for fp1 , fp2 in dic.items():
    print(fp1 , fp2)