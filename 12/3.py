import collections

class LRUCache:

    def __init__(self, capacity):
        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn):
        if isbn not in self._isbn_price_table: return False, None
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price

        return True, price

    def insert(self, isbn, price):
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif len(self._isbn_price_table) >= self._capacity:
            self._isbn_price_table.popitem(last=False)

        self._isbn_price_table[isbn] = price

    def erase(self, isbn):
        return self._isbn_price_table.pop(isbn, None) is not None

k_capacity = 2
c = LRUCache(k_capacity)
c.insert(1, 1)
c.insert(1, 10)
assert c.lookup(2) == (False, None)
assert c.lookup(1) == (True, 1)
c.erase(1)
assert c.lookup(1) == (False, None)
