start = 0
finish = TABLE.length - 1
flag = 0

while start <= finish:
    I = (start + finish)/2
    if TABLE[I] == ITEM:
        flag = 1
        break
    elif  TABLE[I] < ITEM:
        start = I + 1
    else:
        finish = I - 1

if flag == 0 and TABLE[start] == ITEM :
    flag = 1
elif flag == 0 and TABLE[finish] == ITEM :
    flag = 1
    
if flag == 1:
    print("FOUND")
else:
    print("NOT FOUND")
    
    # 此程序的功能是在一个有序的数组 TABLE 中查找数据项 
    # ITEM 是否存在，并返回查找结果。
    #输入的数组 TABLE 必须是有序的输入的数组 TABLE 必须是有序的