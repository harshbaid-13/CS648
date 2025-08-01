import random

dataset_sizes = [10**3, 10**4, 10**5, 10**6]
small_dataset_sizes = [10**1, 10**2, 5*10**3, 10**3, 2*10**3, 4*10**3, 6*10**3, 8*10**3, 10**4]
universe_size = 10**18
prime_number = 10**18 + 3

def generate_ap_series(size, start=1, difference=2):
    return [start + i * difference for i in range(size)]

ap_series = generate_ap_series(100, start=0, difference=100)

print("Loading datasets...")    
datasets = []
for size in dataset_sizes:
    datasets.append(random.sample(range(universe_size), size))
    print(f"Loaded dataset of size {size}.")

small_datasets = []
# for size in small_dataset_sizes:
#     small_datasets.append(random.sample(range(universe_size), size))

__all__ = ['datasets', 'universe_size', 'prime_number', 'small_datasets', 'ap_series']

