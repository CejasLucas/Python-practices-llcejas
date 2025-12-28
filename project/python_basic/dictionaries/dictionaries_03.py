from project.utils.format import TerminalFormat

students = {
    "Benitez Nicolas": [10, 9, 7, 8],
    "Rodriguez Facundo" : [10, 6, 4, 2],
    "Paz Leonel": [10, 8, 0, 10],
    "Joaquin Diaz": [8, 9, 7, 6],
    "Tolo Federico": [10, 7, 5, 3],
    "Manes Rodolfo": [5, 6, 4, 2]
}

def warning(name):
    print(f"⚠️  The student {name} has no grades.")
    print(">>>  The course will be cancelled/absent")

def format_print(student:str, average: str):
    return (TerminalFormat.align_left(f"Grade average: {average}", 40) +
            TerminalFormat.align_center(f"Student name: {student}", 40))


def final_result_table(elements: dict[str, list[int]]):
    TerminalFormat().title("Final average of the students loaded", "=", 80)

    for student, grades in elements.items():
        if grades:
            average = sum(grades) / len(grades)
            print( format_print(student, str(average)) )
        else:
            print( format_print(student, 'N/A') )


def run():
    print("\nCreate a program to store student names and their grades.")
    print("Each student can have a different number of grades.")
    print("Use a dictionary where keys are student names and values are lists of grades.")

    print("\nAsk how many students will be entered, then ask for each name and grades")
    print("(until a negative number is entered). At the end, display each student")
    print("with their average grade. If a name is repeated, show an error.")
    print(">>> The cut-off condition is given if a grade is entered outside the range [0,10]")

    TerminalFormat.line_with_jump("-", 80)
    name_student = input("↪️   Enter the student's name: ")

    if name_student == "" or name_student.isdigit():
        print("\n🚫   Error: The name entered is invalid.")
        TerminalFormat.line("-", 80)
        TerminalFormat.number_of_spaces()
        return

    if name_student in students:
        print("\n🚫   Error: That name is already on the student list.")
        TerminalFormat.line("-", 80)
        TerminalFormat.number_of_spaces()
        return

    index = 0
    notes = list()
    while True:
        try:
            note = float(input(f"🔄   Enter note [{index}] for {name_student}: "))
            if note < 0 or note > 10:
                TerminalFormat.line("-", 80)
                TerminalFormat.number_of_spaces()
                break
            notes.append(note)
            index += 1

        except ValueError:
            print("⚠️  You did not enter a valid number.")
            TerminalFormat.line("-", 80)
            TerminalFormat.number_of_spaces()

    if index == 0: warning(name_student)
    students[name_student] = notes
    final_result_table(students)