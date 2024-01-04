from src.main.lab import regExFunctions, regExExerciseOne, regExExerciseTwo, regExExerciseThree

if __name__ == "__main__":
    print('regExFunctions')
    regExFunctions()

    print('regExExerciseOne: ', regExExerciseOne())
    print('regExExerciseTwo: ', regExExerciseTwo())

    while True:
        print("Enter test email address for exercise 3")
        email = input()
        print('regExExerciseThree: ', regExExerciseThree(email))
