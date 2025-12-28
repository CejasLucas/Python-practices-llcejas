def run():
    print("\nDaily class log: ")
    print("\n- Ask for the day of the week.")
    print("\n- If it’s Monday (beginner), Tuesday (intermediate), or Wednesday (advanced)")
    print("  ask if there were exams. If yes, enter number of students who passed")
    print("  and failed, then show the pass percentage.")
    print("\n- If it’s Thursday (python_basic), enter class attendance percentage.")
    print("  Show if the majority attended (over 50%).")
    print("\n- If it’s Friday (consultation), enter number of students and fee per student.")
    while True:
        menu_text = (
            "\nWrite the number corresponding to the day of the week to complete the task:\n"
            "1) Monday\n"
            "2) Tuesday\n"
            "3) Wednesday\n"
            "4) Thursday\n"
            "5) Friday\n"
            "0) Exit\n"
        )
        number_input = input(menu_text + "Enter a number: ")

        try:
            number = int(number_input.strip())
        except ValueError:
            print("❌ Invalid input: please enter a number.\n")
            continue

        if number == 0:
            print("Exiting the exercise.\n")
            break

        levels = {1: level, 2: level, 3: level, 4: practical, 5: queries}

        if number in levels:
            levels[number]()
        else:
            print("❌ Invalid option. Try again.\n")


def level():
    response = input("\nWere there exams that day? Enter [Y] to confirm: ")
    if response.strip().upper() == "Y":
        approved_input = input("Enter the number of students who passed = ")
        disapproved_input = input("Enter the number of failed students = ")
        try:
            approved = int(approved_input.strip())
            disapproved = int(disapproved_input.strip())
        except ValueError:
            print("❌ Invalid input: numbers only.\n")
            return

        number_of_students = approved + disapproved
        if number_of_students == 0:
            print("No students registered.\n")
        else:
            passing_percentage = (approved / number_of_students) * 100
            print(f"✅ Passing percentage: {passing_percentage:.2f}%\n")
    else:
        print("No exams that day.\n")


def practical():
    response_input = input("\nEnter the attendance percentage between 0 and 100: ")
    try:
        response = int(response_input.strip())
    except ValueError:
        print("❌ Invalid input: number expected.\n")
        return

    if 0 < response <= 100:
        if response > 50:
            print("✅ Perfect, most of the students attended\n")
        else:
            print("⚠️ The number of student attendance is very low\n")
    else:
        print("❌ Number outside the requested parameters\n")


def queries():
    number_input = input("\nEnter the number of students who attended: ")
    value_input = input("\nEnter the price per consultation: ")

    try:
        number_of_student = int(number_input.strip())
        value_per_query = float(value_input.strip())
    except ValueError:
        print("❌ Invalid input: numbers only.\n")
        return

    final_total_income = number_of_student * value_per_query
    print(f"✅ Final total income: ${final_total_income:.2f}\n")
