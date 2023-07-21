#Write a program that asks the user to enter five test scores. The program should display a letter
#grade for each score and the average test score. Write the following functions in the program:
#• calc_average—This function should accept five test scores as arguments and return the
#average of the scores.
#• determine_grade—This function should accept a test score as an argument and return a
#letter grade for the score, based on the following grading scale:

def calc_average(scores):
    """Calculate the average of the test scores."""
    total = sum(scores)
    average = total / len(scores)
    return average

def determine_grade(score):
    """Determine the letter grade based on the score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    test_scores = []
    for i in range(5):
        score = int(input("Enter test score {}: ".format(i+1)))
        test_scores.append(score)

    average_score = calc_average(test_scores)

    print("\nTest Scores and Grades:")
    for i in range(len(test_scores)):
        grade = determine_grade(test_scores[i])
        print("Test {}: {}, Grade: {}".format(i + 1, test_scores[i], grade))

    print("\nAverage Test Score:", average_score)

if __name__ == "__main__":
    main()


    

