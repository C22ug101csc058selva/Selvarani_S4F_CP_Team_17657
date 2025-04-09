
# failure_prediction.py

# Dataset: [temperature, voltage, current, time_since_last_maintenance, failure]
data = [
    [45, 220, 5.0, 10, 1],
    [40, 215, 5.2, 8, 0],
    [50, 210, 4.8, 12, 1],
    [35, 225, 5.1, 7, 0],
    [55, 205, 4.5, 15, 1],
    [38, 218, 5.3, 6, 0],
    [48, 212, 5.0, 11, 1],
    [37, 230, 5.1, 5, 0]
]

# Splitting features and labels
X = [row[:-1] for row in data]
y = [row[-1] for row in data]

# Improved prediction logic
def improved_predict(sample):
    temp, voltage, current, maintenance = sample

    score = 0

    if temp > 47:
        score += 1
    if maintenance > 10:
        score += 1
    if voltage < 215:
        score += 1
    if current < 4.9:
        score += 1

    if score >= 2:
        return 1
    else:
        return 0

# Test improved model
correct = 0
for i in range(len(X)):
    pred = improved_predict(X[i])
    print(f"Sample {i+1}: Predicted = {pred}, Actual = {y[i]}")
    if pred == y[i]:
        correct += 1

accuracy = correct / len(X) * 100
print(f"\nImproved Model Accuracy: {accuracy:.2f}%")
