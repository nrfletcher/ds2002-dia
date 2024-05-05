from api_util import ApiUtility
from db_util import DbUtil

api_util = ApiUtility()
db_util = DbUtil()

db_util.connect()
db_util.persist(api_util.get())
db_util.disconnect()

