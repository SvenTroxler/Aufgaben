from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient("mongodb://localhost:27017/")
col = client["monitoring"]["power"]

docs = list(col.find().sort("timestamp", 1).limit(100))

timestamps = [d["timestamp"] for d in docs]
cpu = [d["cpu"] for d in docs]
ram_used = [d["ram_used"] / 1024 / 1024 / 1024 for d in docs]
ram_total = [d["ram_total"] / 1024 / 1024 / 1024 for d in docs]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

ax1.plot(timestamps, cpu)
ax1.set_ylabel("CPU (%)")
ax1.set_ylim(0, 100)

ax2.plot(timestamps, ram_used, label="Used")
ax2.plot(timestamps, ram_total, label="Total")
ax2.set_ylabel("RAM (GB)")
ax2.legend()

plt.tight_layout()
plt.show()