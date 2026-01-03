def run():
    print("\nPrint the first 100 natural numbers\n")
    for number in range(0,101):
        if number != 0 and number % 20 == 0:
            print(f"{number} \n")
        else:
            print(f"{number}  ", end="")