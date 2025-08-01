from dataset import universe_size, small_datasets, prime_number
from utils import get_random_number, get_queries
from time import perf_counter as time
class PerfectHashing:

    def __init__(self, s):
        self.s = s

    def create_primary_hash_table(self):
        primary_hash_table = [None for _ in range(len(self.s)**2)]
        x, y = get_random_number(1, prime_number-1), get_random_number(0, prime_number-1)
        for i in self.s:
            index = ((i * x + y) % prime_number) % (len(self.s)**2)
            if primary_hash_table[index] is not None:
                return None, 0, 0
            primary_hash_table[index] = i
        return primary_hash_table, x, y

    def perfect_hashing(self):
        while True:
            primary_hash_table, x, y = self.create_primary_hash_table()
            if primary_hash_table is not None:
                break
        return primary_hash_table, x, y

    def query_values(self, key):
        index = ((key * self.x + self.y) % prime_number) % len(self.s)
        return key in self.primary_hash_table[index]
