BATCH_SIZE = 10
DATA = [2, 3, 3, 4, 3, 2, 4, 6, 5, 3,
        3, 2, 2, 3, 3, 4, 3, 3, 4, 4]
ORDER = [i + 1 for i in range(len(DATA))]

heads = sum(DATA)
observation_count = BATCH_SIZE * len(DATA)
estimate = heads / observation_count