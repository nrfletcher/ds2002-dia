'''
Analyze relationships between the data fields provided by the API.
'''
from db_util import DbUtil

db_util = DbUtil()
db_util.connect()
items = db_util.query()
for item in items:
    print(item)
db_util.disconnect()