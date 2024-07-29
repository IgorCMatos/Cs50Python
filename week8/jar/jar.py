class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, more_cookie):
        if self.size + more_cookie > self.capacity:
            raise ValueError("Too Full")
        if more_cookie > self.capacity:
            raise ValueError("Too Full")

        self._size += more_cookie

    def withdraw(self, less_cookie):
        if self.size < less_cookie:
            raise ValueError("There is no cookie to remove")
        self._size -= less_cookie

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
