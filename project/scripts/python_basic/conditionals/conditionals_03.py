def run():
    print("\nLet the user vote for a candidate: R (Red Party), G (Green Party), ")
    print("or B (Blue Party). Print the corresponding party.")
    print("If the input is invalid, show “Invalid option”.")
    print("\nR = RED Party\nG = GREEN Party\nB = BLUE Party\n")
    party_input = input("Choose a letter: ")

    party = party_input.strip().upper()
    parties = { "R": "RED", "G": "GREEN", "B": "BLUE" }

    if party in parties:
        print(f"\n✅ You voted for the {parties[party]} party.\n")
    else:
        print("\n❌ Invalid option.\n")
    return
