import random
from dataset import universe_size

def get_random_number(start, end):
    return random.randint(start, end)

def get_queries(dataset, number_of_queries_from_dataset, number_of_queries_from_universe):
    dataset_samples = random.sample(dataset, number_of_queries_from_dataset)
    universe_samples = random.sample(range(universe_size), number_of_queries_from_universe)
    return dataset_samples + universe_samples
