def counter():
    occurrences = {}
    fruits = [
        "apple",
        "banana",
        "orange",
        "grape",
        "apple",
        "kiwi",
        "banana",
        "melon",
        "orange",
        "strawberry",
    ]

    # ここにコードを書いてください
    for fruit in fruits:
        if fruit in occurrences:
            occurrences[fruit] += 1
        else:
            occurrences[fruit] = 1
     # 辞書をループ処理して出力
    for fruit, count in occurrences.items():
        print(f"{fruit}: {count}")

    return occurrences

print(counter())
