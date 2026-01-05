from colorama import Fore, Style

RESET = Style.RESET_ALL

PRIMARY_INTENSITY, SECONDARY_INTENSITY = Style.BRIGHT, Style.NORMAL

PRIMARY_COLOR, SECONDARY_COLOR = Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX

class Runtime:
    def __init__(self, title):
        self.module_name: str = title
        self.menu: dict[int, str] = {}
        self.exercises: dict[int, object] = {}

    def register(self, practice):
        for idx, item in enumerate(practice):
            name = item.get("statement")
            exercise = item.get("exercise")

            if not name or not exercise:
                print(f"Warning: The exercise at index {idx} does not have 'exercise' or 'name' and will be omitted.")
                continue

            self.menu[idx + 1] = name
            self.exercises[idx + 1] = exercise

    def show_title(self):
        title_display = f"\n========== {self.module_name} PRACTICE =========="
        print(PRIMARY_COLOR + PRIMARY_INTENSITY + title_display)
        print(SECONDARY_COLOR + SECONDARY_INTENSITY, end="")

    def show_menu(self):
        for key, name in self.menu.items():
            print(f" {key}. {name}")
        print(" 0. Exit")

    def run(self):
        while True:
            self.show_title()
            self.show_menu()
            try:
                choice = int(input("Enter a name according to the option: ").strip())
                print()
            except ValueError:
                print("Invalid entry. Please enter a valid number.\n")
                continue

            if choice == 0:
                print("You have finished the program.\n")
                break

            exercise = self.exercises.get(choice)

            if exercise:
                exercise()
            else:
                print("Invalid entry. Please enter a valid number.\n")
