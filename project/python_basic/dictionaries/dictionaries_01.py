from project.utils.__terminal_format__ import TerminalFormat

phone_book = {
    'Cejas Lucas': 1169591337,
    'Diaz Brisa': 1147894526,
    'Sanchez Claudia': 1145789654,
    'Galarza Natalia': 112458794
}

def run():
    print("\nCreate a dictionary where the key is the user's name and the value is their")
    print("phone number. Keep asking for contacts until the user chooses to stop.")
    print("Names must be unique (no duplicates allowed).")
    print(">>> Leave the name empty and press Enter to finish")

    while True:
        TerminalFormat.line_with_jump("=", 50)
        username = input("Contact name: ").strip()
        user_telephone = input("Contact phone number: ").strip()

        if username == "" or user_telephone == "":
            print("🚫   I cannot save an empty contact.")
            TerminalFormat.line("-", 50)
            break

        if not user_telephone.isdigit():
            print("⚠️   The phone number must contain only digits.")
            print("[NOTE] Repeat or leave a blank space to exit.")
            TerminalFormat.line("-", 50)
            continue
        phone_book[username] = int(user_telephone)

    TerminalFormat.number_of_spaces()
    TerminalFormat.line("*", 50)
    TerminalFormat.align_center("📖  Created contact book", 50)
    TerminalFormat.line("*", 50)
    for name, telephone in phone_book.items(): print(f"Name: {name} | Telephone: {telephone}")