# ここにコードを書いてください
def count_vowels(input_string):
    vowels = "aiueoAIUEO"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

user_input = input("文字列を入力してください:")
vowel_count = count_vowels(user_input)
print("Number of vowels:",vowel_count)