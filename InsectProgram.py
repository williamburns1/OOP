import InsectClass as c


def main():
    mosquito = c.Insect('Mosquito', 2, 4)
    housefly = c.Insect("Housefly", 2, 4)
    print('This insect can fly ', mosquito.get_length(), 'miles.')


main()
