'''
You are working on a Python program that processes temperature data from an IoT sensor network. The sensors collect temperature readings every hour and send the data to a central server. Your task is to write a Python program that reads the temperature data, calculates the average temperature for each day, and identifies any anomalies where the temperature exceeds a certain threshold.


'''

# Sample data representing temperature readings from the sensors
# Each sublist represents readings for a single day
temperature_data = [
    [22.4, 21.9, 23.1, 24.0, 22.8, 23.3, 24.5, 23.1, 22.9, 24.4, 23.6, 22.7, 24.1, 23.5, 22.9, 24.3, 23.2, 22.8, 24.0, 23.7, 22.5, 24.6, 23.8, 22.9],
    [23.0, 22.5, 24.0, 23.8, 22.9, 24.1, 23.7, 22.8, 24.2, 23.6, 22.7, 24.5, 23.3, 22.9, 24.0, 23.5, 22.6, 24.4, 23.7, 22.8, 24.2, 23.6, 22.9, 24.0],
    # More data can be added for additional days
]

# Function to calculate the average temperature for each day
def calculate_daily_averages(data):
    daily_averages = []
    for day in data:
        daily_average = sum(day) / len(day)
        daily_averages.append(daily_average)
    return daily_averages

# Function to identify anomalies where the temperature exceeds a threshold
def identify_anomalies(data, threshold):
    anomalies = []
    for day_index, day in enumerate(data):
        for hour_index, temp in enumerate(day):
            if temp > threshold:
                anomalies.append((day_index, hour_index, temp))
    return anomalies

# Calculate daily averages
daily_averages = calculate_daily_averages(temperature_data)
print("Daily Averages:", daily_averages)

# Identify anomalies with a threshold of 24.0
anomalies = identify_anomalies(temperature_data, 24.0)
print("Anomalies:", anomalies)
