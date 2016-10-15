from flask import Flask
from flask import jsonify

app = Flask("the-box")

books =[
        {
            "name":"Harry potter and the prisoner of Azkaban",
            "author":"JK. Rowling",
            "category":"Magic/fiction",
            "id":"2334235"
        },
        {
            "name":"Harry potter and the prisoner of azkaban",
            "author":"JK. Rowlings",
            "category":"magic/fiction",
            "id":"4354234"
        }
        ]

@app.route('/api/category/books/', methods=['GET', 'POST'])
def book_api():
    if request.method=='GET':
        return jsonify(books)
    else:
        name=request.values.get('name', None)
        author = request.values.get('author', None)
        category = request.values.get('category', None)
        id = request.values.get('id', None)

        new_book = {
            'name':name,
            'author':author,
            'category':category,
            'id':id
            }

        books.append(new_book)
        resp = jsonify({'ok':'book added'})

    return resp

if __name__ == '__main__':
    app.run()
