from flask import Flask
from flask import jsonify
from flask import request

app = Flask('the-box-library')

books = [{
    'name': 'Harry Potter and the prisoner of Azkaban',
    'author': 'JK. Rowling',
    'category': 'Magic / Fiction',
    'id': '4325345234'
},
{
    'name': 'Harry Potter and the prisoner of Azkaban',
    'author': 'JK. Rowling',
    'category': 'Magic / Fiction',
    'id': '4325345234'
}]

@app.route('/api/category/books/', methods=['GET','POST'])
def book_api():
    resp = ''
    if request.method == 'GET':
        resp = jsonify(books)
    else:
        name     = request.values.get('name', None)
        author   = request.values.get('author', None)
        category = request.values.get('category', None)
        id_      = request.values.get('id', None)

        new_book = {
          'name': name,
          'author': author,
          'category': category,
          'id': id_
        }
        books.append(new_book)
        resp = jsonify({'OK': 'Book added'})

    return resp

if __name__ == '__main__':
app.run()
