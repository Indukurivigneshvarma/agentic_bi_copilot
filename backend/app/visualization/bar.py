import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def plot_bar(data, y_label="Count"):
    plt.figure(figsize=(7, 4))
    data.plot(kind="bar")
    plt.xlabel(data.index.name if data.index.name else "Category")
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.tight_layout()
