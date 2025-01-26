import pandas as pd
import matplotlib.pyplot as plt

# Load the output data
file_path = "/Users/manuyadav/Downloads/sentiment_analysis_results.csv"
data = pd.read_csv(file_path)

# Calculate average sentiment scores
average_sentiment = data[
    ["Advantages_Polarity", "Challenges_Polarity", "Additional Features_Polarity"]
].mean()

# Display average polarity
print("Average Sentiment Scores:")
print(average_sentiment)

# Visualize polarity distribution
for column in ["Advantages_Polarity", "Challenges_Polarity", "Additional Features_Polarity"]:
    plt.hist(data[column], bins=20, alpha=0.7, label=column)

plt.title("Polarity Distribution")
plt.xlabel("Polarity")
plt.ylabel("Frequency")
plt.legend()
plt.show()