def identify_shape(sides):
    match sides:
        case 3:
            return "Triangle"
        case 4:
            return "Quadrilateral"
        case 5:
            return "Pentagon"
        case 6:
            return "Hexagon"
        case _:
            return "Unknown shape"

print(identify_shape(5))  # Output: Pentagon
