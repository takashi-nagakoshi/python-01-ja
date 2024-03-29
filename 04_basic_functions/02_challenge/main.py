def encode(message):
    if not message:
        return "No message provided"
    #for char in message: メッセージ内の各文字について反復処理します。
    #ord(char): 文字 char のUnicodeコードポイントを取得します。ord()関数は、与えられた文字のUnicodeコードポイントを返します。
    #ord('文字列') 例print(ord('a'))
    #str(ord(char)): Unicodeコードポイントを文字列に変換します。str()関数を使用して数値を文字列に変換します。
    #' '.join(...): 上記で生成された文字列のリストを、スペースで区切られた1つの文字列に連結します。
    encoded_message = ' '.join(str(ord(char)) for char in message)
    return encoded_message

def decode(encoded_message):
    if not encoded_message:
        return "No encoded message provided"
    #encoded_message.split(): エンコードされたメッセージを空白文字で分割し、分割された部分文字列のリストを生成します
    #int(code): エンコードされた文字のUnicodeコードポイントを表す文字列 code を整数に変換します。int() 関数は、文字列を整数に変換します。
    #chr(int(code)): Unicodeコードポイントを文字に変換します。
    #(chr(数字))　(chr(97))
    #''.join(...): デコードされた各文字を空の文字列に結合して、元のメッセージを再構築します
    decoded_message = ''.join(chr(int(code)) for code in encoded_message.split())
    return decoded_message

# 関数のテスト
message = "Hello World"
encoded_message = encode(message)
decoded_message = decode(encoded_message)

print("Encoded message:", encoded_message)
print("Decoded message:", decoded_message)

# def encode(message):
#     encoded = []
#     for c in message:
#         encoded.append(str(ord(c)))
#     return " ".join(encoded)

# def decode(message):
#文字列を分解する
#     unicode_list = message.split()
#先に入れるべき箱を作る
#     result = ""
#     for i in unicode_list:
#         result += chr(int(i))
#     return result