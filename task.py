import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Backend_logs.csv")

df["Request time"] = pd.to_datetime(df["Request time"], format="mixed")
df["Response time"] = pd.to_datetime(df["Response time"], format="mixed")
df["Time difference"] = (df["Response time"] - df["Request time"]).dt.total_seconds() * 1000

q_10 = df["Time difference"].quantile(0.1)
q_90 = df["Time difference"].quantile(0.9)

df_filtered = df[(df["Time difference"] >= q_10) & (df["Time difference"] <= q_90)]

plt.hist(df_filtered["Time difference"], density=True, alpha=0.5)
df_filtered["Time difference"].plot(kind="density")

plt.title("Histogram of Time difference")
plt.xlabel("Time difference")
plt.ylabel("Frequency")
plt.show()