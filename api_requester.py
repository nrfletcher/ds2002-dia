import time
from api_util import ApiUtility
from db_util import DbUtil

def run_loop():
    api_util = ApiUtility()
    db_util = DbUtil()
    db_util.connect()

    for i in range(60):
        data = api_util.get()
        db_util.persist(data)
        print(f"Iteration {i+1}: Data persisted")
        time.sleep(60)  # Wait for 1 minute

    db_util.disconnect()

if __name__ == "__main__":
    run_loop()
