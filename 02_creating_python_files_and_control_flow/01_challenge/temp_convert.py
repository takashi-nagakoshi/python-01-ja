def convert():
    # ここにコードを書いてください
    # temp変数を編集し、ユーザー入力として温度を受け取ります。整数に変換することを忘れないでください
    temp = int(input("enter a number:"))
    temp_unit=input("f , c")
    x = temp
    y = temp_unit
    # f = 華氏、c = 摂氏
    if (y == 'f'):
        C = (x -32)*5/9
        print(int(C))
    elif (y =='c'):
        F = (x * 9/5) + 32
        print(int(F))
    
#     temp = 0

#     return temp


# convert()
