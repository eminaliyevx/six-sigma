import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Backend_logs_improved.csv")

df["Request time"] = pd.to_datetime(df["Request time"], format="mixed")
df["Response time"] = pd.to_datetime(df["Response time"], format="mixed")
df["Time difference"] = (df["Response time"] - df["Request time"]).dt.total_seconds() * 1000

plt.hist(df["Time difference"], density=True, alpha=0.5)
df["Time difference"].plot(kind="density")

plt.title("Histogram of Time difference")
plt.xlabel("Time difference")
plt.ylabel("Frequency")
plt.show()