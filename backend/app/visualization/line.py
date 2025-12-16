import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def plot_line(data):
    plt.figure(figsize=(7, 4))
    data.plot(marker="o")
    plt.xlabel("Semester")
    plt.ylabel("Average Marks")
    plt.grid(True)
    plt.tight_layout()
