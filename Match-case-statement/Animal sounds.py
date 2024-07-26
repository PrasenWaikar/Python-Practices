def animal_sound(animal):
    match animal:
        case "dog":
            return "Bark"
        case "cat":
            return "Meow"
        case "cow":
            return "Moo"
        case "sheep":
            return "Baa"
        case _:
            return "Unknown sound"

print(animal_sound("cat"))  # Output: Meow
