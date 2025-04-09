
# Sample input: [temperature, voltage, current, time_since_last_maintenance]
sample_data = [
    [45, 220, 5.0, 10],
    [35, 225, 5.1, 7],
    [52, 210, 4.7, 14],  # High risk
    [38, 218, 5.3, 6]
]

def predict_failure(sample):
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
    return 1 if score >= 2 else 0

def take_action(sample_id, sample):
    print(f"\n>> ALERT: Potential inverter failure detected for Sample {sample_id}")
    print("- Notifying maintenance team...")
    print("- Logging issue to system...")
    print("- Scheduling inspection for panel...")
    print(f"- Details: Temp={sample[0]}, Voltage={sample[1]}, Current={sample[2]}, Maintenance Age={sample[3]}")

# Run predictions
for i, sample in enumerate(sample_data, start=1):
    prediction = predict_failure(sample)
    print(f"Sample {i} Prediction: {'Failure' if prediction else 'Normal'}")
    if prediction == 1:
        take_action(i, sample)
