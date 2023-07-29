class HashMap:
    INIT_BUCKET_COUNT = 16
    LOAD_FACTOR = 0.5

    class Entity:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    class Bucket:
        def __init__(self):
            self.list = []

        def add(self, entity):
            for e in self.list:
                if e.key == entity.key:
                    old_value = e.value
                    e.value = entity.value
                    return old_value
            self.list.append(entity)
            return None

        def remove(self, key):
            for e in self.list:
                if e.key == key:
                    removed_value = e.value
                    self.list.remove(e)
                    return removed_value
            return None

        def get(self, key):
            for e in self.list:
                if e.key == key:
                    return e.value
            return None

    class HashMapIterator:
        def __init__(self, buckets):
            self.buckets = buckets
            self.current_bucket_index = 0
            self.current_bucket_list = None
            self.list_iterator = None

        def find_next_bucket(self):
            while self.current_bucket_index < len(self.buckets):
                if self.buckets[self.current_bucket_index] is not None:
                    self.current_bucket_list = self.buckets[self.current_bucket_index].list
                    self.list_iterator = iter(self.current_bucket_list)
                    return
                self.current_bucket_index += 1
            raise StopIteration

        def __iter__(self):
            return self

        def __next__(self):
            if self.current_bucket_index >= len(self.buckets):
                raise StopIteration

            while True:
                if self.list_iterator is None:
                    self.find_next_bucket()
                try:
                    return next(self.list_iterator)
                except StopIteration:
                    self.current_bucket_index += 1
                    self.find_next_bucket()

    def __init__(self):
        self.size = 0
        self.buckets = [None] * self.INIT_BUCKET_COUNT

    def calculate_bucket_index(self, key):
        return hash(key) % len(self.buckets)

    def recalculate(self):
        self.size = 0
        old = self.buckets
        self.buckets = [None] * (len(old) * 2)
        for bucket in old:
            if bucket is not None:
                for entity in bucket.list:
                    self.put(entity.key, entity.value)

    def put(self, key, value):
        if len(self.buckets) * self.LOAD_FACTOR <= self.size:
            self.recalculate()

        index = self.calculate_bucket_index(key)
        bucket = self.buckets[index]
        if bucket is None:
            bucket = self.Bucket()
            self.buckets[index] = bucket

        entity = self.Entity(key, value)

        res = bucket.add(entity)
        if res is None:
            self.size += 1
        return res

    def remove(self, key):
        index = self.calculate_bucket_index(key)
        bucket = self.buckets[index]
        if bucket is None:
            return None

        res = bucket.remove(key)
        if res is not None:
            self.size -= 1
        return res

    def get(self, key):
        index = self.calculate_bucket_index(key)
        bucket = self.buckets[index]
        if bucket is None:
            return None

        return bucket.get(key)

    def __iter__(self):
        return self.HashMapIterator(self.buckets)


# Пример использования:
hash_map = HashMap()

hash_map.put("+79005554433", "Андрей")
hash_map.put("+79005554432", "Алексей")
hash_map.put("+79005554434", "Дарья3")
hash_map.put("+79005554435", "Дарья4")
hash_map.put("+79005554436", "Дарья5")
hash_map.put("+79005554437", "Дарья6")
hash_map.put("+79005554438", "Дарья7")
hash_map.put("+79005554439", "Дарья8")


for entity in hash_map:
    print(entity.key, "-", entity.value)

