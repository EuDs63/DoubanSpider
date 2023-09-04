# 读取merged2.json
import json

json_file_path = 'merge/merged2.json'

# 打开 JSON 文件并将其加载为 JSON 对象
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    books_count = len(data)

    # # 访问特定书籍的信息，例如 "613" 对应的书籍
    # book_613 = data["613"]
    #
    # # 现在 book_613 是一个包含书籍信息的字典对象
    # book_name = book_613["book_name"]
    # book_author = book_613["author_name"]
    # book_price = book_613["price"]
    #
    # # 打印书籍信息
    # print(f"书名: {book_name}")
    # print(f"作者: {book_author}")
    # print(f"价格: {book_price}")


    for book_id in range(1, books_count+1):
        print(book_id)
        book_data = data[str(book_id)]
        title = book_data["book_name"]
        print(title+"\n")


