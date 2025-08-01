class Mod_N_Hashing:
    def __init__(self, s):
        self.s = s
        self.num_buckets = len(s)
        self.table = [[] for _ in range(self.num_buckets)]

    def create_hash_table(self):
        for value in self.s:
            index = value % self.num_buckets
            self.table[index].append(value)
        return self.table

    def query_values(self, key):
        index = key % self.num_buckets
        return key in self.table[index]