class MiniDB:
    def __init__(self):
        self.store = {}

    def set(self, key, value):
        self.store[key] = value
        return "OK"

    def get(self, key):
        return self.store.get(key, None)

    def delete(self, key):
        return self.store.pop(key, None)

# example usage:
# db=MiniDB(); db.set("x",1); print(db.get("x"))
