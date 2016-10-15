from flask import Flask
from flask import request

app = Flask('the-box-hack')
books = [{'name':'Mombasa raha'}]

@app.route('/api/category/books/', methods=['GET','POST'])
def book_api():
	if request.method == 'GET':
        return jsonify(books)
    else:
    	name = request.values.get('name', None)
    

if __name__ = '__main__':
    app.run()
