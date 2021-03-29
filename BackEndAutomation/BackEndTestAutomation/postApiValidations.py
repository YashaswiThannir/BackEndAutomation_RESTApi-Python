import requests

# post call
from BackEndTestAutomation.payLoad import *

add_book = requests.post('http://216.10.245.166/Library/Addbook.php',
                         json=addBookPayload("bweui"),
                         headers={"Content-Type":"application/json"})

print(add_book.json())
response_json = add_book.json()
assert add_book.status_code == 200

# delete call
bookId = response_json['ID']

delete_book = requests.post('http://216.10.245.166/Library/DeleteBook.php', json = {
    'ID': bookId
}, headers={"Content-Type":"application/json"})

assert delete_book.status_code == 200
res_json = delete_book.json()
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

