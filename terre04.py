# Pair ou impair

def odd_or_even(number):

    try:
        number = int(number)

        if number % 2 == 0:
            print("pair")
        else:
            print("impair")

    except ValueError:
        print("Tu ne me la mettras pas à l’envers.")


write = input("Write a number: ")

odd_or_even(write)
