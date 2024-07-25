def grade_by_score(score):
    match score:
        case score if 90 <= score <= 100:
            return "A"
        case score if 80 <= score < 90:
            return "B"
        case score if 70 <= score < 80:
            return "C"
        case score if 60 <= score < 70:
            return "D"
        case score if 0 <= score < 60:
            return "F"
        case _:
            return "Invalid score"

print(grade_by_score(85))  # Output: B
