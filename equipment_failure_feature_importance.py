
# equipment_failure_feature_importance.py

# Simulated data (each item is: [temperature, voltage, current, time_since_last_maintenance, failure])
data = [
    [45, 220, 5, 10, 1],
    [40, 215, 5.2, 8, 0],
    [50, 210, 4.8, 12, 1],
    [35, 225, 5.1, 7, 0],
    [55, 205, 4.5, 15, 1],
]

# Feature names
features = ['temperature', 'voltage', 'current', 'time_since_last_maintenance']
importance_scores = [0, 0, 0, 0]

# Separate data into failures and non-failures
failures = [row for row in data if row[-1] == 1]
non_failures = [row for row in data if row[-1] == 0]

# Calculate simple correlation-like importance (difference between failure vs no-failure average)
for i in range(4):
    avg_fail = sum(row[i] for row in failures) / len(failures)
    avg_no_fail = sum(row[i] for row in non_failures) / len(non_failures)
    importance_scores[i] = abs(avg_fail - avg_no_fail)

# Combine feature names and scores
feature_importance = list(zip(features, importance_scores))

# Sort and print feature importance
feature_importance.sort(key=lambda x: x[1], reverse=True)

print("Feature Importance (Higher = More Important):")
for feature, score in feature_importance:
    print(f"{feature}: {score:.2f}")
