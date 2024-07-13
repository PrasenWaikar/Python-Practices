# You are developing a Python program for a smart home system. The system needs to control the lighting in different rooms based on the time of day and occupancy. Your task is to write a Python program that reads the occupancy status and current time, then decides whether to turn the lights on or off in each room.

from datetime import datetime

# Sample data representing occupancy status for each room
# True indicates the room is occupied, False indicates it is not
occupancy_status = {
    "living_room": True,
    "kitchen": False,
    "bedroom": True,
    "bathroom": False
}

# Function to determine if lights should be on based on the time of day and occupancy
def control_lights(occupancy, current_time):
    lights_status = {}
    for room, is_occupied in occupancy.items():
        if is_occupied:
            if 18 <= current_time.hour <= 23 or 0 <= current_time.hour < 6:
                lights_status[room] = "ON"
            else:
                lights_status[room] = "OFF"
        else:
            lights_status[room] = "OFF"
    return lights_status

# Get the current time
current_time = datetime.now()

# Determine the lights status for each room
lights_status = control_lights(occupancy_status, current_time)
print("Lights Status:", lights_status)
