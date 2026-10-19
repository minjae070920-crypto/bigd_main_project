import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False

weight = [90, 86, 75, 78, 73]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(weight)
for i, p in enumerate(weight):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
        xytext=(0, 8), ha="center")
ax.set_title("내 몸무게 변화 추이")
fig.savefig("my_first_chart.png")