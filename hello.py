from flask import Flask
from flask import jsonify,make_response
from flask import request
app = Flask("the-box-library")

books=[{
	"name":"Kiswahili kitukuzwe",
	"id":"12345",
	"author":"Jimmy"
},
{
	"name":"Kamusi",
	"id":"123456",
	"author":"Maawy"
}]

@app.route("/api/cstegory/books/",methods=['GET','POST'])
def book_api():
	if request.method == "GET":
		rep =jsonify(books)
	else:
		name=request.values.get("name",None)
		author=request.values.get("author",None)
		id_=request.values.get("id",None)
		new_book={"name":name,"author":author,"id":id_}
		books.append(new_book)
		resp=jsonify(books)
	return resp

if __name__ == "__main__":
	app.run()