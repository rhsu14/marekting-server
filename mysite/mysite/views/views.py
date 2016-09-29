from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb 

db = MySQLdb.connect("localhost", "root", "", "test")       

cur = db.cursor()

db.query("SELECT name FROM main WHERE id=4;")
r = db.store_result();

db.query("""INSERT INTO main (id, name, score) VALUES (null, 'Stacy', 100);""")
db.commit()

# Create your views here.
def index(request):
	return HttpResponse(r.fetch_row())
