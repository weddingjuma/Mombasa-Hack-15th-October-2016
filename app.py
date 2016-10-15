from flask import Flask
app = Flask('the-box-hack')
books = {'name':'Mombasa raha'}

@app.route('/api/category/books/', methods=['GET','POST'])
def book_api():
    return books

if __name__ = '__main__':
    app.run()
