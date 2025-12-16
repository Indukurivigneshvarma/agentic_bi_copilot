import matplotlib
matplotlib.use("Agg")   # 🔴 REQUIRED FOR SERVER

import matplotlib.pyplot as plt

def plot_pie(data):
    plt.figure(figsize=(6, 6))
    data.plot(kind="pie", autopct="%1.1f%%")
    plt.ylabel("")  # cleaner
