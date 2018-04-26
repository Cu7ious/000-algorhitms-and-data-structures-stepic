#! /usr/bin/env python3
import random as rd

def simulate_coin_flips(num_trials):
    heads = 0
    tails = 0
    p_heads = 0.5

    for i in range(num_trials):
        random_number = rd.random()
        if random_number < p_heads:
            heads = heads + 1
        else:
            tails += 1
    percent_heads = heads / num_trials

    return [heads, tails, percent_heads]



trials = 1000
results = simulate_coin_flips(trials)
heads, tails, percent_heads = results

print("In", trials, "trials there were", heads, "heads and", tails, "tails")
print("PERCENT HEADS:", 100 * percent_heads, "percent")
