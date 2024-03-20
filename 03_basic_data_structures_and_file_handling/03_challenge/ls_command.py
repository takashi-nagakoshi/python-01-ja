import os


def ls_command(directory):
    # ユーザー入力が「sample」の場合、ディレクトリは「sample」になります
    # 無効なディレクトリパスについて考える必要はありません

    # 「pass」を削除して、ここにコードを書いてください
    # ファイルの拡張子を格納するための辞書を初期化
    extension_dict = {}
    # 指定されたディレクトリ内のファイルを確認,指定したディレクトリ内のファイルやディレクトリのリストを返します。
    for file in os.listdir(directory):
        #特定のパスがファイルかどうかを確認するための条件文
        if os.path.isfile(os.path.join(directory, file)):
            # 拡張子を取得 指定されたファイルパスを拡張子とそれ以外の部分に分割します。
            _, extension = os.path.splitext(file)
             # 辞書に拡張子とファイル名を追加, extension が既に辞書に登録されている拡張子かどうか
            if extension in extension_dict:
                extension_dict[extension].append(file)
            else:
                extension_dict[extension] = [file]           
    # 概要を表示
    print("Summary in alphabetical order:")
    # extension_dict.items() は辞書のキーと値のペアを返すイテレータ
    # extension は拡張子を表します。
    # files はその拡張子に関連付けられたファイル名のリストです。
    # len(files) はリストの長さ、つまりその拡張子のファイルの数を示します。
    for extension, files in sorted(extension_dict.items()):
        if len(files) == 1:
            print(f"{extension}:{len(files)} file")
        else:
            print(f"{extension}:{len(files)} files")

if __name__ == "__main__":
    directory_path = input("Enter directory path to organize files: ")

    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
    else:
        ls_command(directory_path)
