class Bookshelf:
    def __init__(self):
        # ブックシェルフを初期化
        self.books = []

    def add_book(self, title, read_status):
        # ブックを追加します ブックのタイトルと既読/未読のステータスを受け取り、ブックシェルフに追加。
        # self.booksはブックシェルフ内の本を格納するリスト、その長さに1を加えることで、新しい本のIDを設定
        book_id = len(self.books) + 1
        # bookは新しい本の情報を保持する辞書、'id'、'title'、'read_status'のキーを保持
        book = {'id': book_id, 'title': title, 'read_status': read_status}
        # 新しい本の辞書をブックシェルフ内の本を格納するリストに追加
        self.books.append(book)
        print(f"(ID: {book_id})Book '{title}' added to the bookshelf.")

    def edit_book(self, book_id, title, read_status):
        # 指定されたIDのブックを編集
        for book in self.books:
            if book['id'] == book_id:
                book['title'] = title
                book['read_status'] = read_status
                print(f"Book with ID {book_id} edited.")
                return
        print(f"Book with ID {book_id} not found.")

    def search_books(self, keyword):
        # 指定されたキーワードに一致するブックを検索し、一覧表示。
        found_books = [book for book in self.books if keyword.lower() in book['title'].lower()]
        if found_books:
            print("Found books:")
            for book in found_books:
                print(f"ID: {book['id']}, Title: {book['title']}, Read Status: {'Read' if book['read_status'] else 'Unread'}")
        else:
            print("No books found matching the search criteria.")

    def delete_book(self, book_id):
        # 指定されたIDのブックを削除。
        for book in self.books:
            if book['id'] == book_id:
                self.books.remove(book)
                print(f"Book with ID {book_id} deleted.")
                return
        print(f"Book with ID {book_id} not found.")

    def show_statistics(self):
        # ブックシェルフの統計情報を表示します　ブックの総数、既読の数、未読の数を表示。
        total_books = len(self.books)
        total_read = sum(book['read_status'] for book in self.books)
        total_unread = total_books - total_read
        print(f"Total Books: {total_books}, Read: {total_read}, Unread: {total_unread}")
        # 本の一覧（ID、タイトル、既読／未読ステータス）を表示
        print("Book List:")
        # ブックシェルフに登録されているすべての本に対して、以下の処理を実行。
        for book in self.books:
            #book辞書の中の'read_status'キーの値を確認。
            #'read_status'がTrue（既読）の場合は"Read"を、False（未読）の場合は"Unread"をread_status変数に割り当て。
            read_status = "Read" if book['read_status'] else "Unread"
            print(f"ID: {book['id']}, Title: {book['title']}, Status: {read_status}")

def display_menu():
    # ブックシェルフの操作メニューを表示します。
    print("===============================================\nWelcome to your personal books digital library!\n===============================================")
    print("1. Add a Book")
    print("2. Edit a Book")
    print("3. Search Books")
    print("4. Delete a Book")
    print("5. View Library Stats")
    print("6. Exit app")

def main():
    # メイン関数 アプリケーションのエントリーポイント。
    bookshelf = Bookshelf()
    while True:
        display_menu()
        choice = input("Please select from 1 to 6: ")
        if choice == '1':
            # ブックを追加する
            title = input("Enter the title of the book: ")
            # .lower() メソッドは、ユーザーが大文字で "Y" を入力した場合でも小文字の "y" に変換します。
            read_status = input("Is the book read? (y/n): ").lower() == 'y'
            bookshelf.add_book(title, read_status)
        elif choice == '2':
            # ブックを編集する
            book_id = int(input("Enter the ID of the book to edit: "))
            title = input("Enter the new title of the book: ")
            read_status = input("Is the book read? (y/n): ").lower() == 'y'
            bookshelf.edit_book(book_id, title, read_status)
        elif choice == '3':
            # ブックを検索する
            keyword = input("Enter the keyword to search: ")
            bookshelf.search_books(keyword)
        elif choice == '4':
            # ブックを削除する
            book_id = int(input("Enter the ID of the book to delete: "))
            bookshelf.delete_book(book_id)
        elif choice == '5':
            # ブックシェルフの統計情報を表示する
            bookshelf.show_statistics()
        elif choice == '6':
            # アプリケーションを終了する
            print("Exiting the Digital Bookshelf. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()