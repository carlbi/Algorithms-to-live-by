import numpy as np
import time
from tqdm import tqdm
from random import shuffle
from matplotlib import pyplot as plt

print("Optimal Stopping Problem")

# Parameters

N = 1000 # number of simulations
n = 100 # number of candidates
strategies = np.arange(0,1,0.01)
candidates = np.arange(n)
success_rate = np.zeros((strategies.shape[0], 1))

# Simulations

start_time = time.time()
for num, strategy in enumerate(tqdm(strategies)):
    success_counter = 0
    for sim in range(N):
        # Shuffle candidates randomly
        shuffle(candidates)
        best_yet = 0
        chosen = candidates[-1]
        # Execute look-and-leap strategy
        for place, cand in enumerate(candidates):
            if place < strategy*len(candidates):
                if cand > best_yet: best_yet = cand
            else:
                if cand > best_yet: chosen = cand; break
        if chosen == max(candidates): success_counter += 1
    success_rate[num] = success_counter/N
end_time = time.time()
run_time = round(end_time - start_time)
print('Completed {} simulations in {}s with {} candidates per simulation'.
format(N, run_time, n))

# Plotting

plt.plot(strategies*100, success_rate*100)
plt.axvline(100/np.exp(1), color='red')
plt.xlabel('Strategy in % wait time')
plt.ylabel('Success rate in % best pick')
plt.title('Optimal stopping problem with {} candidates'.format(n))
plt.grid()
plt.show()
