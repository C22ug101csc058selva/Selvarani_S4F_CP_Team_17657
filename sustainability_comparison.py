
# Simulated data for 12 months of a solar plant

months = 12

# Traditional Maintenance: fixed checks every month (regardless of need)
traditional_checks = 12
traditional_failures = 6
traditional_downtime_hours = traditional_failures * 5  # each failure causes 5 hours of downtime

# Predictive Maintenance: checks only when needed
predictive_checks = 5
predictive_failures = 2
predictive_downtime_hours = predictive_failures * 2  # downtime is reduced due to early detection

# Material usage (e.g., spare parts, technician visits)
traditional_parts_used = traditional_checks
predictive_parts_used = predictive_checks

# Energy loss due to downtime (kWh)
traditional_energy_loss = traditional_downtime_hours * 50  # 50 kWh lost per hour
predictive_energy_loss = predictive_downtime_hours * 50

# Display comparison
print("=== Sustainability Comparison ===")
print(f"Total Checks - Traditional: {traditional_checks}, Predictive: {predictive_checks}")
print(f"Failures Detected - Traditional: {traditional_failures}, Predictive: {predictive_failures}")
print(f"Downtime Hours - Traditional: {traditional_downtime_hours}, Predictive: {predictive_downtime_hours}")
print(f"Energy Lost (kWh) - Traditional: {traditional_energy_loss}, Predictive: {predictive_energy_loss}")
print(f"Parts Used - Traditional: {traditional_parts_used}, Predictive: {predictive_parts_used}")

# Calculate improvements
energy_saved = traditional_energy_loss - predictive_energy_loss
downtime_saved = traditional_downtime_hours - predictive_downtime_hours
parts_saved = traditional_parts_used - predictive_parts_used

print("\n=== Sustainability Gains from Predictive Maintenance ===")
print(f"Energy Saved: {energy_saved} kWh")
print(f"Downtime Reduced: {downtime_saved} hours")
print(f"Parts Waste Reduced: {parts_saved} units")
