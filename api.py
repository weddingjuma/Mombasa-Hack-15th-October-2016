from flask import Flask
from 
app = Flask ('the-box-library')

@app.route('api/category/books', methods =['GET','POST'])
def book_api():
           if request.method == 'GET'
             return jsonify(books)
         else :
         	name = request.value.get('name', None)
         	author = request.value.get('author', None)
         	category = request.value.get('category', None)
         	id_= request.value.get('id', None)

         	new_book{
         	     'name':name
         	     'author':author
         	     'category':category
         	     'id_':id_
         	}	
	
	books.append(new_book)
	return jsonify({'Ok':'Book added'})
	#resp = jsonify({'Ok':'Book added'})
	return resp
   
if __name__  == '__main__':
	app.run()