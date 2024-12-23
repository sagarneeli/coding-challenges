"""
Design a SQL transaction system for a key-value store. 
So have a way to commit and rollback data from the DB, but also be able to update the DB without using commit and rollback (just write straight to it). 
Step two was to enable this in a nested manner (one level deep)
"""

class Transaction:
    def __init__(self):
        self.changes = {}  # Stores temporary changes for this transaction
        self.parent = None  # For nested transactions

class KeyValueStore:
    def __init__(self):
        self.data = {}  # Main storage
        self.current_transaction = None
    
    def get(self, key):
        """Get value for a key, considering active transactions"""
        if self.current_transaction:
            # Check in current transaction first
            if key in self.current_transaction.changes:
                return self.current_transaction.changes[key]
            # Check in parent transaction if exists
            if self.current_transaction.parent and key in self.current_transaction.parent.changes:
                return self.current_transaction.parent.changes[key]
        return self.data.get(key)
    
    def put(self, key, value):
        """Put a key-value pair"""
        if self.current_transaction:
            self.current_transaction.changes[key] = value
        else:
            self.data[key] = value
    
    def begin_transaction(self):
        """Start a new transaction"""
        transaction = Transaction()
        if self.current_transaction:
            # Nested transaction
            transaction.parent = self.current_transaction
        self.current_transaction = transaction
    
    def commit(self):
        """Commit the current transaction"""
        if not self.current_transaction:
            raise ValueError("No active transaction to commit")
        
        # If there's a parent transaction, merge changes into it
        if self.current_transaction.parent:
            self.current_transaction.parent.changes.update(self.current_transaction.changes)
            self.current_transaction = self.current_transaction.parent
        else:
            # Commit changes to main storage
            self.data.update(self.current_transaction.changes)
            self.current_transaction = None
    
    def rollback(self):
        """Rollback the current transaction"""
        if not self.current_transaction:
            raise ValueError("No active transaction to rollback")
            
        if self.current_transaction.parent:
            self.current_transaction = self.current_transaction.parent
        else:
            self.current_transaction = None

# Example usage:
if __name__ == "__main__":
    db = KeyValueStore()
    
    # Direct writes (no transaction)
    db.put("a", 1)
    print("Direct write:", db.get("a"))  # Output: 1
    
    # Single transaction
    db.begin_transaction()
    db.put("a", 2)
    print("In transaction:", db.get("a"))  # Output: 2
    db.commit()
    print("After commit:", db.get("a"))  # Output: 2
    
    # Nested transaction
    db.begin_transaction()
    db.put("a", 3)
    db.begin_transaction()  # Nested
    db.put("a", 4)
    print("In nested transaction:", db.get("a"))  # Output: 4
    db.rollback()  # Rollback inner transaction
    print("After inner rollback:", db.get("a"))  # Output: 3
    db.commit()  # Commit outer transaction
    print("After outer commit:", db.get("a"))  # Output: 3


"""
Design a SQL transaction system for a key-value store. 
So have a way to commit and rollback data from the DB, but also be able to update the DB without using commit and rollback (just write straight to it). 
Step two was to enable this in a nested manner (one level deep).
"""

class KeyValueStore:
    def __init__(self):
        self.store = {}  # Main database
        self.transaction_stack = []  # Stack to maintain transactions

    def set(self, key, value):
        if self.transaction_stack:
            # Save the current state of the key in the transaction's backup
            current_transaction = self.transaction_stack[-1]
            if key not in current_transaction['backup']:
                current_transaction['backup'][key] = self.store.get(key)
            current_transaction['updates'][key] = value
        else:
            # Direct write to the store
            self.store[key] = value

    def get(self, key):
        if self.transaction_stack:
            # Check the latest transaction for updates
            for transaction in reversed(self.transaction_stack):
                if key in transaction['updates']:
                    return transaction['updates'][key]
        return self.store.get(key)

    def delete(self, key):
        if self.transaction_stack:
            # Save the current state of the key in the transaction's backup
            current_transaction = self.transaction_stack[-1]
            if key not in current_transaction['backup']:
                current_transaction['backup'][key] = self.store.get(key)
            current_transaction['updates'][key] = None
        else:
            # Direct delete from the store
            self.store.pop(key, None)

    def begin(self):
        if len(self.transaction_stack) < 2:  # Allow one level of nesting
            self.transaction_stack.append({'backup': {}, 'updates': {}})
        else:
            raise Exception("Nested transactions beyond one level are not supported.")

    def commit(self):
        if not self.transaction_stack:
            raise Exception("No transaction to commit.")

        current_transaction = self.transaction_stack.pop()
        for key, value in current_transaction['updates'].items():
            if value is None:
                self.store.pop(key, None)
            else:
                self.store[key] = value

    def rollback(self):
        if not self.transaction_stack:
            raise Exception("No transaction to rollback.")

        current_transaction = self.transaction_stack.pop()
        # Restore the backup state
        for key, value in current_transaction['backup'].items():
            if value is None:
                self.store.pop(key, None)
            else:
                self.store[key] = value

# Example usage
if __name__ == "__main__":
    kv_store = KeyValueStore()

    # Direct update
    kv_store.set("a", 10)
    print(kv_store.get("a"))  # Output: 10

    # Start a transaction
    kv_store.begin()
    kv_store.set("a", 20)
    print(kv_store.get("a"))  # Output: 20

    # Rollback the transaction
    kv_store.rollback()
    print(kv_store.get("a"))  # Output: 10

    # Start another transaction
    kv_store.begin()
    kv_store.set("a", 30)
    kv_store.commit()
    print(kv_store.get("a"))  # Output: 30

    # Start nested transaction (one level deep)
    kv_store.begin()
    kv_store.set("b", 40)
    kv_store.begin()  # Nested transaction
    kv_store.set("b", 50)
    kv_store.rollback()  # Rollback nested transaction
    print(kv_store.get("b"))  # Output: 40
    kv_store.commit()
    print(kv_store.get("b"))  # Output: 40



"""
Design an in memory Key-Value pair based database with get(), set() and delete()
Follow Up: Extend it to a transaction based system with operations like begin(), commit() and rollback()
"""
class KeyValueStore:
    def __init__(self):
        self.store = {}  # Main key-value store
        self.transaction_stack = []  # Stack to hold transactions

    def get(self, key):
        if key in self.store:
            return self.store[key]
        else:
            return None

    def set(self, key, value):
        if self.transaction_stack:
            # Record the current value in the transaction for rollback
            if key not in self.transaction_stack[-1]:
                self.transaction_stack[-1][key] = self.store.get(key, None)
        self.store[key] = value

    def delete(self, key):
        if self.transaction_stack:
            # Record the current value in the transaction for rollback
            if key not in self.transaction_stack[-1]:
                self.transaction_stack[-1][key] = self.store.get(key, None)
        self.store.pop(key, None)

    def begin(self):
        # Start a new transaction
        self.transaction_stack.append({})

    def commit(self):
        if not self.transaction_stack:
            raise RuntimeError("No transaction to commit")
        # Merge the changes in the top transaction to the main store
        self.transaction_stack.pop()

    def rollback(self):
        if not self.transaction_stack:
            raise RuntimeError("No transaction to rollback")
        # Revert changes made in the current transaction
        last_transaction = self.transaction_stack.pop()
        for key, original_value in last_transaction.items():
            if original_value is None:
                self.store.pop(key, None)  # Key was newly added, remove it
            else:
                self.store[key] = original_value  # Revert to original value

# Example usage:
db = KeyValueStore()

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
db.commit()  # Commit transaction
print(db.get("name"))  # Outputs: Charlie