def traffic_light(action):
    match action:
        case "red":
            return "Stop"
        case "yellow":
            return "Caution"
        case "green":
            return "Go"
        case _:
            return "Invalid color"

print(traffic_light("green"))  # Output: Go
