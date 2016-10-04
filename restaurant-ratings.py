# your code goes here
def ratings(file_path):
    """returns a dictionary from file"""

    restaurant_ratings = {}
    my_file = open(file_path)
    
    for line in my_file:
        line = line.strip().split(':')
        restaurant_ratings[line[0]] = line[1]

    return restaurant_ratings

final_ratings = ratings("scores.txt") #create a dictionary from the file

def print_dict(grades):
    """sort and alphabetize restaurants and rates before printing"""

    for grade in grades: #looping through dictionary
        grade = final_ratings.items() #generating a list of tuples
        sorted_grades = sorted(grade) #sorting tuples in order(alphabetizing)

    print sorted_grades

print_dict(final_ratings)

