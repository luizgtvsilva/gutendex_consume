**API Documentation**

**AGAP2 TEST**


<table>
  <tr>
   <td><strong>Version</strong>
   </td>
   <td><strong>Date</strong>
   </td>
   <td><strong>Author</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>1.0
   </td>
   <td>25-July-2012
   </td>
   <td>Luiz Gustavo
   </td>
   <td>Initial draft
   </td>
  </tr>
</table>



## The APIs on this document will get some information about the external API provided ([https://gutendex.com/](https://gutendex.com/)). That external API provides us with some information about books.

To run this endpoint would be necessary to [install python](https://www.python.org/downloads/).

Then, on CMD you need to run this commands:



* pip install flask
* pip install pytest
* git clone https://github.com/luizgtvsilva/gutendex_consume.git

Go to gutendex_consume/app and run:



* flask run

The endpoints will be available to run through any client (Postman, Insomnia, etc)

You can also run tests, you need to go to gutendex_consume/app/tests and run:



* python -m pytest test.py


## For the endpoints below, it is not necessary any kind of authentication.


## 


## <p style="text-align: right">
Endpoints</p>



## 1. get all books

The objective of this endpoint are retrieve informations of all books


## Request


<table>
  <tr>
   <td><strong>Method</strong>
   </td>
   <td><strong>URL            </strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>GET</code></strong>
   </td>
   <td><code>/books/</code>
   </td>
  </tr>
</table>



<table>
  <tr>
   <td><strong>Type</strong>
   </td>
   <td><strong>Params</strong>
   </td>
   <td><strong>Values</strong>
   </td>
  </tr>
  <tr>
   <td><strong>N/A</strong>
   </td>
   <td><strong>No param required</strong>
   </td>
   <td>
   </td>
  </tr>
</table>



## Response


<table>
  <tr>
   <td><strong>Status</strong>
   </td>
   <td><strong>Response</strong>
   </td>
  </tr>
  <tr>
   <td><code>200</code>
   </td>
   <td><code>{</code>
<p>
<code>	"count": 68507,</code>
<p>
<code>	"next": "http://127.0.0.1:5000/books/2",</code>
<p>
<code>	"previous": null,</code>
<p>
<code>	"results": [</code>
<p>
<code>		{</code>
<p>
<code>			"id": 1342,</code>
<p>
<code>			"title": "Pride and Prejudice",</code>
<p>
<code>			"authors": [</code>
<p>
<code>				{</code>
<p>
<code>					"name": "Austen, Jane",</code>
<p>
<code>					"birth_year": 1775,</code>
<p>
<code>					"death_year": 1817</code>
<p>
<code>				}</code>
<p>
<code>			],</code>
<p>
<code>			"languages": [</code>
<p>
<code>				"en"</code>
<p>
<code>			],</code>
<p>
<code>			"download_count": 34176,</code>
<p>
<code>			"rating": "Was not possible to get this information right now",</code>
<p>
<code>			"review": "Was not possible to get this information right now"</code>
<p>
<code>		},</code>
<p>
<code>		{</code>
<p>
<code>			"id": 11,</code>
<p>
<code>			"title": "Alice's Adventures in Wonderland",</code>
<p>
<code>			"authors": [</code>
<p>
<code>				{</code>
<p>
<code>					"name": "Carroll, Lewis",</code>
<p>
<code>					"birth_year": 1832,</code>
<p>
<code>					"death_year": 1898</code>
<p>
<code>				}</code>
<p>
<code>			],</code>
<p>
<code>			"languages": [</code>
<p>
<code>				"en"</code>
<p>
<code>			],</code>
<p>
<code>			"download_count": 21051,</code>
<p>
<code>			"rating": 3.0,</code>
<p>
<code>			"review": [</code>
<p>
<code>				"this is a good film",</code>
<p>
<code>				"this is a good film",</code>
<p>
<code>				"this is a good film"</code>
<p>
<code>			]</code>
<p>
<code>		},</code>
<p>
<code>[...]</code>
   </td>
  </tr>
  <tr>
   <td><code>!200</code>
   </td>
   <td><code>"{error_message}":{error_code}</code>
   </td>
  </tr>
</table>



## 2. get book by name

The objective of this endpoint are retrieve informations of an book, filtered by name


## Request


<table>
  <tr>
   <td><strong>Method</strong>
   </td>
   <td><strong>URL            </strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>GET</code></strong>
   </td>
   <td><code>/books_name/&lt;name_of_the_book>/</code>
   </td>
  </tr>
</table>



<table>
  <tr>
   <td><strong>Params</strong>
   </td>
   <td><strong>Values</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Path Param</strong>
   </td>
   <td><strong>String (name of the book to search)</strong>
   </td>
  </tr>
</table>



## Response


<table>
  <tr>
   <td><strong>Status</strong>
   </td>
   <td><strong>Response</strong>
   </td>
  </tr>
  <tr>
   <td><code>200</code>
   </td>
   <td><code>{</code>
<p>
<code>	"count": 68507,</code>
<p>
<code>	"next": "http://127.0.0.1:5000/books_name/pride%20and%20prejudice/2",</code>
<p>
<code>	"previous": null,</code>
<p>
<code>	"results": [</code>
<p>
<code>		{</code>
<p>
<code>			"id": 1342,</code>
<p>
<code>			"title": "Pride and Prejudice",</code>
<p>
<code>			"authors": [</code>
<p>
<code>				{</code>
<p>
<code>					"name": "Austen, Jane",</code>
<p>
<code>					"birth_year": 1775,</code>
<p>
<code>					"death_year": 1817</code>
<p>
<code>				}</code>
<p>
<code>			],</code>
<p>
<code>			"languages": [</code>
<p>
<code>				"en"</code>
<p>
<code>			],</code>
<p>
<code>			"download_count": 34176,</code>
<p>
<code>			"rating": "Was not possible to get this information right now",</code>
<p>
<code>			"review": "Was not possible to get this information right now"</code>
<p>
<code>		}</code>
<p>
<code>[...]</code>
   </td>
  </tr>
  <tr>
   <td><code>!200</code>
   </td>
   <td><code>"{error_message}":{error_code}</code>
   </td>
  </tr>
</table>



## 3. get book by name with pages

The objective of this endpoint are retrieve informations of of an book, filtered by name, with pagination (if has)


## Request


<table>
  <tr>
   <td><strong>Method</strong>
   </td>
   <td><strong>URL            </strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>GET</code></strong>
   </td>
   <td><code>/books_name/&lt;name_of_the_book>/&lt;number_of_the_page_you_want>/</code>
   </td>
  </tr>
</table>



<table>
  <tr>
   <td><strong>Params</strong>
   </td>
   <td><strong>Values</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Path Param</strong>
   </td>
   <td><strong>String: name of the book to search</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Path Param</strong>
   </td>
   <td><strong>String: number of the page you want to go</strong>
   </td>
  </tr>
</table>



## Response


<table>
  <tr>
   <td><strong>Status</strong>
   </td>
   <td><strong>Response</strong>
   </td>
  </tr>
  <tr>
   <td><code>200</code>
   </td>
   <td><code>{</code>
<p>
<code>	"count": 68507,</code>
<p>
<code>	"next": "http://127.0.0.1:5000/books_name/pride%20and%20prejudice/4",</code>
<p>
<code>	"previous": http://127.0.0.1:5000/books_name/pride%20and%20prejudice/2,</code>
<p>
<code>	"results": [</code>
<p>
<code>		{</code>
<p>
<code>			"id": 1342,</code>
<p>
<code>			"title": "Pride and Prejudice",</code>
<p>
<code>			"authors": [</code>
<p>
<code>				{</code>
<p>
<code>					"name": "Austen, Jane",</code>
<p>
<code>					"birth_year": 1775,</code>
<p>
<code>					"death_year": 1817</code>
<p>
<code>				}</code>
<p>
<code>			],</code>
<p>
<code>			"languages": [</code>
<p>
<code>				"en"</code>
<p>
<code>			],</code>
<p>
<code>			"download_count": 34176,</code>
<p>
<code>			"rating": "Was not possible to get this information right now",</code>
<p>
<code>			"review": "Was not possible to get this information right now"</code>
<p>
<code>		}</code>
<p>
<code>[...]</code>
   </td>
  </tr>
  <tr>
   <td><code>!200</code>
   </td>
   <td><code>"{error_message}":{error_code}</code>
   </td>
  </tr>
</table>



## 4. Insert an rating to any book

The objective of this endpoint are to store an rating to an book


## Request


<table>
  <tr>
   <td><strong>Method</strong>
   </td>
   <td><strong>URL            </strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>POST</code></strong>
   </td>
   <td><code>api/rate/</code>
   </td>
  </tr>
</table>



<table>
  <tr>
   <td><strong>Params</strong>
   </td>
   <td><strong>Values</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>Body: application/json</code></strong>
   </td>
   <td><code>{</code>
<p>
<code>	"id": 11, #book id</code>
<p>
<code>	"rating": 3, #rating between 0-5</code>
<p>
<code>	"review": "this is a good book" #free text</code>
<p>
<code>}	</code>
   </td>
  </tr>
</table>



## Response


<table>
  <tr>
   <td><strong>Status</strong>
   </td>
   <td><strong>Response</strong>
   </td>
  </tr>
  <tr>
   <td><code>200</code>
   </td>
   <td><code>"Rated successfully! You drop for Book No {id} the rate of {rating} star(s)."</code>
   </td>
  </tr>
  <tr>
   <td><code>!200</code>
   </td>
   <td><code>"{error_message}":{error_code}</code>
   </td>
  </tr>
</table>