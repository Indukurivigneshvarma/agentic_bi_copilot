import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def plot_line(data, x_label="Semester"):
    plt.figure(figsize=(7, 4))
    data.plot(marker="o")
    plt.xlabel(x_label)
    plt.ylabel("Average Marks")
    plt.grid(True)
    plt.tight_layout()
