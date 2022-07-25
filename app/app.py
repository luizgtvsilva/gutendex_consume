from flask import Flask, request
import sqlite3
import requests
import json

app = Flask(__name__)


#FUNCTION TO CONNECT TO DATABASE 
def get_db_connection():

    try:
        conn = sqlite3.connect('database/database.db') #OUR DATABASE CREATED THROUGH 'schema.sql' FILE
        return conn
    except:
        return False


#FUNCTION TO GET THE RATING INFORMATION FROM DATABASE
def get_rating(book_id):
    try:
        conn = get_db_connection()
        sql = conn.execute('SELECT * FROM rates WHERE book_id = ?', [book_id]).fetchall() #THIS FUNCTION WILL RETURN A TUPLE
        return [dict(rate_id=row[0], book_id=row[1], rating=row[2], review=row[3]) for row in sql] #WILL RETURN A DICT OF KEY/VALUE INFORMATION FROM DATABASE
    except:
        return False


"""
THAT IS THE MAIN FUNCTION OF THE CODE, WE WILL STRUCTURE ALL THE RETURN INFORMATIONS AS WE NEED
I PREFER TO KEEP THE RETURN OF THE EXTERNAL API AND JUST MANIPULATE IT AS NECESSARY.
SO I WILL KEEP THE PAGINATION AND SEARCH FUNCTION OF THE API, AN WILL JUST CHANGE THE INFORMATION ITSELF.
IN THAT FUNCTION WE WILL RECEIVE A DICT FROM THE API, CALLED 'data'.
"""
def creating(data):

    req_fields = ['id', 'title', 'authors', 'languages', 'download_count'] #FIELDS THAT WE WANT TO RETURN, IF WE WANT ONE OR MORE: JUST ADD HERE. CHECK LINE 52.
    url_rules = request.base_url.split('/') #SPLITTING THE URL TO MANIPULATE THE PAGINATION

    if url_rules[-1] == '': #CHECK IF IT'S THE FIRST PAGE
        actual_page = '1'
    else: 
        actual_page = url_rules[-1] #IF NOT, OUR ACTUAL PAGE WILL BE OUR LAST PARAMETER IN URL. EXP: https://localhost:5000/books/5 <- OUR ACTUAL PAGE WILL BE '5'.

    url_rules.pop(-1) #REMOVING THE LAST PAGE INFORMATION TO REWRITE IN THE NEXT LINES
    next_page = int(actual_page) + 1
    previous_page = int(actual_page) - 1

    data['next'] = '/'.join(url_rules) + '/'+ str(next_page) #REWRITING OUR URL AND CHANGING THE PAGE NUMBER

    if actual_page != '1':
        data['previous'] = '/'.join(url_rules) + '/'+ str(previous_page)

    for element in data['results']: #RUN THROUGH OUR ELEMENTS INSIDE OUR 'RESULTS' IN OUR DATA FROM API
        for key, value in element.copy().items():
            if key not in req_fields:
                del element[key] #IF THE FIELD ISN'T WHAT WE WANT, WE WILL JUST REMOVE IT FROM OUR FINAL RESULT

        actual_element = data['results'][data['results'].index(element)] #GET OUR ACTUAL BOOK

        """
        WE STORED INTO AN SIMPLE SQL LITE THE INFORMATIONS ABOUT THE RATING OF EACH BOOK.
        TO ADD THE INFORMATION TO OUR RESULT, WE NEED TO TAKE THE INFORMATION INTO OUR DB AND ADD TO INDEX OF EACH BOOK.
        """
        rating_info = get_rating(book_id=actual_element['id']) #GET THE RATING INFORMATION ABOUT THAT BOOK

        if rating_info:
            if len(rating_info) > 0:
                actual_element['rating'] = sum(star['rating'] for star in rating_info) / len(rating_info) #OUR RATING WILL BE BASICALLY: RATING = SUM OF VOTES/TOTAL OF VOTES

            reviews = []
            for r in rating_info: #THEN WE CREATED A LIST OF REVIEWS
                reviews.append(r['review'])
            actual_element['review'] = reviews

        else:
            actual_element['rating'] = 'Was not possible to get this information right now'
            actual_element['review'] = 'Was not possible to get this information right now'
        
    return json.dumps(data)


#AN SIMPLE ENDPOINT THAT RECEIVE AN JSON AND SEND A 'POST' TO OUR SQL LITE DATABASE 
@app.route("/rate/", methods=['POST'])
def add_rate():
    try:
        conn = get_db_connection()
        sql = """ INSERT INTO rates (book_id, rating, review) values (?,?,?); """

        book_id = request.json['id']
        rating = request.json['rating']

        if rating > 5 or rating < 0:
            return 'Rating must be an number between 0 and 5'

        review = request.json['review']

        data = (book_id, rating, review)

        cursor = conn.cursor()
        cursor.execute(sql, data) #EXECUTE QUERY OF THE LINE 81 THE INFORMATIONS OF THE LINE 87
        
        conn.commit()

        return f'Rated successfully! You drop for Book No {book_id} the rate of {rating} star(s).'
    except:
        return 'Was not possible to add your rate right now, please try again later!'



#ENDPOINT TO RETRIEVE INFORMATIONS FROM ALL BOOKS IN OUR EXTERNAL API, USING PAGINATION. BY DEFAULT THE THE PAGE WILL BE '1'.
@app.route("/books/")
@app.route("/books/<page>")
def get_books(page='1'):
    try:    
        url = f'https://gutendex.com/books/?page={page}'
        api = requests.get(url)
        data = api.json()

        return creating(data)
    except requests.exceptions.RequestException as err:
        return {f'Error code: {api.status_code}': f'{err}'}


#ENDPOINT TO RETRIEVE INFORMATIONS FROM BOOKS FILTERED BY BOOK'S NAME IN OUR EXTERNAL API, USING PAGINATION. BY DEFAULT THE THE PAGE WILL BE '1'.
@app.route("/books_name/<name>/")
@app.route("/books_name/<name>/<page>")
def get_books_by_name(name, page='1'):
    try:
        url = f'https://gutendex.com/books/?search={name}&page={page}'
        api = requests.get(url)
        data = api.json()

        return creating(data)
    except requests.exceptions.RequestException as err:
        return {f'Error code: {api.status_code}': f'{err}'}


@app.route("/")
def home():

    return "This is my app for the AGAP2 opportunity!"
