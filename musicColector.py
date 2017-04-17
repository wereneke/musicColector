def list_of_list_of_lines(list_of_csv_lines):
    lista = [line.split(' | ') for line in list_of_csv_lines]
    for i in range(len(lista)):
        lista[i][4] = lista[i][4].strip('\n')
    return lista


def tupling(lista):
    music = []
    for i in range(len(lista)):
        name = [lista[i][j] for j in range(len(lista[i])) if j < 2]
        information = [lista[i][j] for j in range(len(lista[i])) if j >= 2]
        music += [tuple([tuple(name), tuple(information)])]
    return music

        
menu = '''Welcome in the CoolMusic! Choose the action:
         1) Add new album
         2) Find albums by artist
         3) Find albums by year
         4) Find musician by album
         5) Find albums by letter(s)
         6) Find albums by genre
         7) Calculate the age of all albums
         8) Choose a random album by genre
         9) Show the amount of albums by an artist *
        10) Find the longest-time album *
         0) Exit'''


csv_file = open('music.txt')
list_of_csv_lines = csv_file.readlines()
csv_file.close()
lista = list_of_list_of_lines(list_of_csv_lines)

music = tupling(lista)
print(music)