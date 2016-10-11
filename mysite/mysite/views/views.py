from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb 

db = MySQLdb.connect("localhost", "root", "", "test")  #database     

cur = db.cursor()

db.query("SELECT * FROM main;")	#query stmt from database
r = db.store_result();	#view data from query

db.query("""INSERT INTO main (id, name, score) VALUES (null, 'Stacy', 100);""")
db.commit()	#actually does query, writes in database

# Create your views here.
def index(request):
	return HttpResponse(r.fetch_row(0))	#get this working on website
