# Pair ou impair

def odd_or_even(number):

    try:
        number = int(number)

        if int(number) % 2 == 0:
            print("pair")
        else:
            print("impair")

    except ValueError:
        print("Tu ne me la mettras pas à l’envers.")


number = input("Write a number: ")

odd_or_even(number)
