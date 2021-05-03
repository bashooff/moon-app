""" Write a program that asks for a planet as input, and shows (some of) their respective moons as output. Type exit to stop this program. """
print('Welcome to this program. By entering a planet of choice, you can see which moons orbit the chosen planet!')

def moons():
    while True:
        inp = input('Please insert planet: ')
        if inp == 'Earth':
            print('Earth has only one moon, which is called Moon.')
            continue
        elif inp == 'Jupiter':
            print('Jupiter has 53 named moons, which include Io, Europa, Ganymede and Callisto')
            continue
        elif inp == 'Uranus':
            print('Uranus has 27 moons, which include Ariel, Oberon, Puck, Rosalind, Titania and Umbriel')
            continue
        elif inp == 'Mars':
            print('Mars has two moons: Deimos and Phobos')
            continue
        elif inp == 'Saturn':
            print('Saturn has 82 moons, which include Enceladus and Titan')
            continue
        elif inp == 'Neptune':
            print('Neptune has 14 moons, including Larissa, Proteus, Triton and Halimede')
            continue
        elif inp == 'Mercury':
            print('This planet does not have any moons!')
            continue
        elif inp == 'Venus':
            print('This planet does not have any moons!')
            continue
        elif inp == 'exit':
            break
        else:
            print('This is not a planet!')
moons()

