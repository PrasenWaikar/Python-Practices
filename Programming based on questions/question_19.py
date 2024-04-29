""" 
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""
def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: (x[0], int(x[1]), int(x[2])))

def main():
    tuples = []
    while True:
        try:
            input_str = input("Enter name, age, and height (separated by commas, 'q' to quit): ")
            if input_str.lower() == 'q':
                break
            name, age, height = input_str.split(',')
            tuples.append((name.strip(), age.strip(), height.strip()))
        except ValueError:
            print("Invalid input. Please enter name, age, and height separated by commas.")

    sorted_tuples = sort_tuples(tuples)
    print(sorted_tuples)

if __name__ == "__main__":
    main()
