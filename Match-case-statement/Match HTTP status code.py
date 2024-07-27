def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case 403:
            return "Forbidden"
        case _:
            return "Unknown status code"

print(http_status(404))  # Output: Not Found
