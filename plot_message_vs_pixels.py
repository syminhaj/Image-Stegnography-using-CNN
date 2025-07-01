import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.DataFrame({
    'message_length': [10, 50, 100, 200, 400],
    'altered_pixels': [80, 400, 800, 1600, 3200]
})

sns.scatterplot(data=dataset, x='message_length', y='altered_pixels')
plt.title("Impact of Message Length on Altered Pixels")
plt.xlabel("Message Length (in characters)")
plt.ylabel("Number of Altered Pixels")
plt.grid(True)
plt.show()
