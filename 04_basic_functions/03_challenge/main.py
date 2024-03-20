def unique_substrings(input_string):
    # 「pass」を削除して、ここにコードを書いてください
    # 文字列の長さを取得
    n = len(input_string)
    
    # 重複を除いた部分文字列を格納するためのセット
    substrings_set = set()
    
    # すべての部分文字列を生成してセットに追加
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings_set.add(input_string[i:j])
    
    # セットをリストに変換してソート
    substrings_set = sorted(list(substrings_set))
    
    # セットをリストに変換して返す
    return list(substrings_set)


input_string = "banana"
print(unique_substrings(input_string))
