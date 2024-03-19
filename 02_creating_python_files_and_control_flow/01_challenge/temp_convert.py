def convert():
    # ここにコードを書いてください
    # temp変数を編集し、ユーザー入力として温度を受け取ります。整数に変換することを忘れないでください
    # f = 華氏、c = 摂氏
    # ユーザーから温度と温度単位を受け取る
    temp_input = input("Enter temperature: ")
    unit_input = input("Enter unit (f for Fahrenheit, c for Celsius): ")

    # 温度を整数に変換
    temp = int(temp_input)

    # 温度の単位が華氏の場合は摂氏に変換し、摂氏の場合は華氏に変換
    if unit_input == 'f':
        temp = (temp - 32) * 5 / 9
        unit_output = 'Celsius'
    elif unit_input == 'c':
        temp = temp * 9 / 5 + 32
        unit_output = 'Fahrenheit'
    else:
        print("Invalid unit input. Please enter 'f' for Fahrenheit or 'c' for Celsius.")
        return

    # 変換された温度を出力
    print(f"The temperature is {int(temp)} {unit_output}.")

    return temp

convert()
