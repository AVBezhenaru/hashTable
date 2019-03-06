class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        index = len(value) % self.size
        return index

    def seek_slot(self, value):
        index = self.hash_fun(value)
        length = self.size

        while length > 0:
            if self.slots[index] == None:
                return index

            index += self.step

            if index > self.size - 1:
                index -= self.size
            length -= 1

        return None

    def put(self, value):
        index = self.seek_slot(value)

        if index != None:
            self.slots[index] = value
            return index

        else:
            return None

    def find(self, value):
        index = self.hash_fun(value)
        if self.slots[index] == value:
            return index
        for i in range(self.size):
            if self.slots[i] == value:
                return i

        return None
