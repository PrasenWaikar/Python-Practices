def command_option(option):
    match option:
        case "--help":
            return "Display help"
        case "--version":
            return "Show version"
        case "--verbose":
            return "Enable verbose mode"
        case _:
            return "Unknown option"

print(command_option("--help"))  # Output: Display help
