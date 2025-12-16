import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def plot_histogram(data):
    plt.figure(figsize=(7, 4))
    plt.hist(data, bins=10)
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.tight_layout()
