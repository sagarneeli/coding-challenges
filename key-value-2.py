class KV:
    def __init__(self):
        self.data = {}
        self.transaction_stack = []

    def get(self, key):
        if key in self.data:
            return self.data[key]
        return None

    def set(self, key, value):
        if self.transaction_stack:
            if key not in self.transaction_stack[-1]:
                self.transaction_stack[-1][key] = self.data.get(key, None)
        self.data[key] = value

    def delete(self, key):
        if self.transaction_stack:
            if key not in self.transaction_stack[-1]:
                self.transaction_stack[-1][key] = self.data.get(key, None)
        self.data.pop(key, None)

    def begin(self):
        self.transaction_stack.append({})

    def commit(self):
        if not self.transaction_stack:
            return
        if len(self.transaction_stack) == 1:
            self.transaction_stack.pop()
        else:
            top_transaction = self.transaction_stack.pop()
            for key, _ in top_transaction.items():
                if key not in self.transaction_stack[-1]:
                    self.transaction_stack[-1][key] = self.data.get(key, None)

    def rollback(self):
        if not self.transaction_stack:
            return
        last_transaction = self.transaction_stack.pop()
        for key, original_value in last_transaction.items():
            if original_value is None:
                self.data.pop(key, None)
            else:
                self.data[key] = original_value


db = KV()
# Basic operations
db.set("name", "Alice")
print(db.get("name"))  # Outputs: Alice
db.delete("name")
print(db.get("name"))  # Outputs: None

# Transactional operations
db.set("name", "Alice")
db.begin()  # Start transaction
db.set("name", "Bob")
print(db.get("name"))  # Outputs: Bob
db.rollback()  # Rollback transaction
print(db.get("name"))  # Outputs: Alice
db.begin()  # Start another transaction
db.set("name", "Charlie")
db.begin()  # Nested transaction
db.set("name", "David")
print(db.get("name"))  # Outputs: David
db.rollback()  # Rollback nested transaction
print(db.get("name"))  # Outputs: Charlie
db.commit()  # Commit outer transaction
print(db.get("name"))  # Outputs: Charlie
