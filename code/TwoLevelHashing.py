from dataset import prime_number
from utils import get_random_number

class TwoLevelHashing:
    def __init__(self, s):
        self.s = s

    def create_primary_hash_table(self):
        primary_hash_table = [[] for _ in range(len(2*self.s))]
        x, y = get_random_number(1, prime_number-1), get_random_number(0, prime_number-1)
        collisions = 0
        for i in self.s:
            index = ((i * x + y) % prime_number) % len(primary_hash_table)
            collisions += len(primary_hash_table[index])
            primary_hash_table[index].append(i)
        return primary_hash_table, collisions, x, y

    def create_secondary_hash_table(self):
        for bucket in self.primary_hash_table:
            if len(bucket) > 1:
                while True:
                    secondary_hash_table = [None for _ in range(len(bucket)**2)]
                    x, y = get_random_number(1, prime_number-1), get_random_number(0, prime_number-1)
                    collision = False
                    for i in bucket:
                        index = ((i * x + y) % prime_number) % len(secondary_hash_table)
                        if secondary_hash_table[index] is not None:
                            collision = True
                            break
                        secondary_hash_table[index] = i
                    if not collision:
                        bucket[:] = [(x, y, secondary_hash_table)]
                        break
        return True

    def create_hash_table(self):
        while True:
            primary_hash_table, collisions, x, y = self.create_primary_hash_table()
            if collisions < len(self.s):
                break
        while True:
            is_perfect_hashing_created = self.create_secondary_hash_table(primary_hash_table)
            if is_perfect_hashing_created:
                break
        return primary_hash_table, x, y

    def query_values(self, key):
        index = ((key * self.x + self.y) % prime_number) % len(self.primary_hash_table)
        if isinstance(self.primary_hash_table[index], tuple):
            return self.primary_hash_table[index][2][((key * self.primary_hash_table[index][0] + self.primary_hash_table[index][1]) % prime_number) % len(self.primary_hash_table[index][2])] == key
        else:
            return key in self.primary_hash_table[index]