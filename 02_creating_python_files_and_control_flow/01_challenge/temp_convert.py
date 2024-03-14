# def convert():
    # ここにコードを書いてください
    # temp変数を編集し、ユーザー入力として温度を受け取ります。整数に変換することを忘れないでください

#入力値が華氏の場合
def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
#入力値が摂氏の場合
def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32
def convert():
        temperature = float(input("温度を入力してください： "))
        unit = input("温度の単位を入力してください（華氏または摂氏）： ")

        if unit.lower() == '華氏':
            celsius = fahrenheit_to_celsius(temperature)
            print(f"摂氏 {celsius:.2f} 度です。")
        elif unit.lower() == '摂氏':
            fahrenheit = celsius_to_fahrenheit(temperature)
            print(f"華氏 {fahrenheit:.2f} 度です。")
        else:
            print("無効な単位が入力されました。華氏または摂氏で入力してください。")
if __name__ == "__main__":
    convert()
    # f = 華氏、c = 摂氏
#     temp = 0

#     return temp

# convert()
