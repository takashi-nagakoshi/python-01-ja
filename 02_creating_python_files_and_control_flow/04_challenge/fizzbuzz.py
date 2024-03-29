# ここにコードを書いてください
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# for raw in range(100): 15にするよりは下記のほうがいい
#順番が大事
    # if (raw + 1) % 3 == 0 and (raw + 1) % 5 == 0:
        # print("FizzBuzz")    
    # elif(raw + 1) % 3 == 0:
    #     print("Fizz")
    # elif (raw + 1) % 5 == 0:
    #     print("Buzz")
    # # else:
    #     print(raw + 1)
        