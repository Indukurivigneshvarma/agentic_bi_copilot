import base64
from io import BytesIO
import matplotlib.pyplot as plt

def encode_chart():
    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    plt.close("all")     # 🔴 VERY IMPORTANT
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")
