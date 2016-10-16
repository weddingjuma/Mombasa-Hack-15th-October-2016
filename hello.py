from flask import Flask, request
from flask import jsonify, make_response
app = Flask('rodgy-library')

books = [{
  'name': 'Harry Potter and the priosoner',
  'auther': 'jk. Rowling',
  'category': 'Magic/Fiction',
  'country' : 'Kenya',
  'id': '4325345234'
}]

@app.route('/api/category/books/', methods=['GET', 'POST'])
def book_api():
    resp = ''
    if request.method == 'GET':
        resp = jsonify(books)
    elif request.method == 'POST':
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
        resp = "book added succesfully"

    return resp

if __name__ == '__main__':
  app.debug=True
  app.run()
  app.run(debug=True)
