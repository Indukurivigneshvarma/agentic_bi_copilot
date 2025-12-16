import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def plot_bar(data):
    plt.figure(figsize=(7, 4))
    data.plot(kind="bar")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
