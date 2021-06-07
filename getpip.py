
from pyquery import PyQuery as pq
import pymongo
from datetime import datetime

cluster = pymongo.MongoClient(
    "mongodb+srv://stark:stark265@cluster0.tc6fa.mongodb.net/ktu?retryWrites=true&w=majority")
db = cluster['ktu']
collection = db['ktubot']
pf = []

d = pq(url='https://ktu.edu.in/eu/core/announcements.htm')
rows = d(".content .c-details table tr   ").items()

rows = list(rows)
l = len(rows)
db_data = collection.find({})
db_data = list(db_data)
for row in range(l):
    ele = rows[row].find('a').attr('href')

    if ele != None:
        pf.append(ele)
print(db_data)
for y in pf:
    count = 0
    for x in db_data:
        if y == x['notif']:
            count = count+1

   # if count == 0:
   #       data={"date":datetime.today().strftime('%Y-%m-%d') ,"notif":y}
   #       z=collection.insert_one(data)
   #       print(z.inserted_id)
