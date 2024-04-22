import requests
from flask import Flask,render_template,request
app = Flask(__name__)

def error(message, errorCode):
    return render_template('error.html', customMessage=message, code=errorCode)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/genres')
def genersPage():
    result = requests.get('https://librarymanagementpw.azurewebsites.net/api/genre')
    if (result.status_code == 200):
        return render_template('genres.html', json=result.json() , len=len(result.json()))
    else:
        return error(result.json(),result.status_code)

@app.route('/bookshelf')
def bookshelfPage():
    bookshelfId = request.args.get('bookshelfId') 
    if not bookshelfId:
        result = requests.get('https://librarymanagementpw.azurewebsites.net/api/BookShelf')
        if (result.status_code == 200):
            return render_template('bookshelf.html', json=result.json() , len=len(result.json()))
        else:
            return error(result.json(),result.status_code)
    else:
        result = requests.get(f'https://librarymanagementpw.azurewebsites.net/api/BookShelf/{bookshelfId}')
        if (result.status_code == 200):
            return render_template('bookshelfsng.html', json=result.json() , len=len(result.json()))
        else:
            return error(result.json(),result.status_code)

@app.route('/search/book')
def srcbook():
    return render_template('searchbook.html')

@app.route('/search/book/<bookname>')
def srcbookNM(bookname):
    result = requests.get(f'https://librarymanagementpw.azurewebsites.net/api/Book')
    if (result.status_code == 200):
        for result in result.json():
            if (result['title'] == bookname):
                return result
        return f'{bookname} not found'
    else:
        return error(result.json(), result.status_code)

@app.route('/delete/book')
def deleteBook():
    return "Del"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3246, debug=True)