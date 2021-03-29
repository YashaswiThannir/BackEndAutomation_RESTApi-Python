import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty2'},)

print(response.text)
print(type(response))   # <class 'requests.models.Response'>
json_response = response.json()     # to convert the response into json format(list or dictionary)
print(type(json_response))  # <class 'list'>
print(json_response[0]['isbn'])
print(response.status_code)
assert response.status_code == 200
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# retrieve the book details with ISBN bcz888effed

for book in response.json():
    if book['isbn'] == "bcz888effed":
        print(book)
        break

expectedBook = {
                    "book_name": "Learn Appium Automation with Java",
                    "isbn": "bcz888effed",
                    "aisle": "20027"
                }

assert book == expectedBook