
FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly."""
    data = get_data()
    display_subjects(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line) 
        print(repr(line))  
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
     
        parts[2] = int(parts[2]) 
        print(parts)  # to see if that worked
        data.append(parts)
    input_file.close()
    return data


def display_subjects(data):
    """Display data nicely."""
    for subject_data in data:
        print("{} is taught by {:12} and has {:3} students".format(*subject_data))


main()
