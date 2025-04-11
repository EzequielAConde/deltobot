import shelve

DB_FILE = "storage/counter_data.db"

def incrementUserCounter(user_id: int) -> int:
    with shelve.open(DB_FILE) as db:
        current = db.get(str(user_id), 0)
        current += 1
        db[str(user_id)] = current
        return current
