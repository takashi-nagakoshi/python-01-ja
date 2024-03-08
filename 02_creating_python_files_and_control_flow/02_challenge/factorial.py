def compute_factorial():
    # ここにコードを書いてください
    # number変数を編集し、ユーザー入力として正の整数を受け取ります。整数に変換することを忘れないでください
    
    number = int(input())
    if number == 0:
        return 1 

    count = number
    while(count > 0):
        if count ==1:
            break

        number = number * (count - 1)
        count = count - 1
    # result変数を編集し、最終的な計算結果を保存します
    result = number
    print(result)

    return result

compute_factorial()

#for loop
#range(5) = 0,1,2,3,4
#range(1,5) = 1,2,3,4
#number = number * oneNumber
#linter