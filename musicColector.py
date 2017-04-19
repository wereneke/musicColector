import time


# variables
menu = '''
Welcome in the CoolMusic! Choose the action:
         1) Add new album
         2) Find albums by artist/year/genre
         3) Calculate the age of all albums
         0) Exit'''
go = ''
name = ['artist', 'name']
information = ['year of release', 'genre', 'duration']
template = name + information


def op_csv_to_list(file='music.txt'):
    '''opens csv and convert it to list of lines'''
    csv_file = open(file)
    list_of_csv_lines = csv_file.readlines()  # list which elements are lines of csv file
    csv_file.close()
    return list_of_csv_lines


def list_of_list_of_lines(list_of_csv_lines):
    '''
    input: list of elements made of lines in string format from csv file
    output: list of lists which elements are strings from csv cells
    '''
    lista = [line.split(' | ') for line in list_of_csv_lines]
    for i in range(len(lista)):
        lista[i][4] = lista[i][4].strip('\n')
    return lista


def tupling(lista):
    '''
    input: list of lists which elements are strings from csv cells
    output: list of tuples in way -- [((name),(information)), ((),()), ...]
    '''
    music = []
    for i in range(len(lista)):
        name = [lista[i][j] for j in range(len(lista[i])) if j < 2]
        information = [lista[i][j] for j in range(len(lista[i])) if j >= 2]
        music += [tuple([tuple(name), tuple(information)])]
    return music


def list_of_tuple_to_csv(music):
    '''from list containing albums makes string writable to csv'''
    line = ''
    for i in range(len(music)):
        a = list(music[i])
        c = []
        for j in range(len(a)):
            b = list(a[j])
            c += b
        line += ' | '.join(c) + '\n'
    return line


def add_new_album(template):
    new_album = []
    for prop in template:
        ask = 'what is a ' + prop + ' of the album?'
        propert = input(ask)
        new_album += [propert]
    new_album = [new_album]
    new_album = tupling(new_album)
    return new_album


def uni_searching(music):
    '''asks for searching parameters and and print if found'''
    search = ''
    while search != '0' and search != '1' and search != '2':
        searching_type = ['artist', 'year', 'genre']
        print('You\'d like to search by: (0) %s, (1) %s, (2) %s ?'
              % (searching_type[0], searching_type[1], searching_type[2]))
        search = input()
    search = int(search)
    print('what is %s of album you want to find?' % searching_type[search])
    corespondent = input()

    if search != 2:
        for i in range(len(music)):
            if corespondent == music[i][search][0]:
                print(music[i])
    elif search == 2:
        for i in range(len(music)):
            if corespondent == music[i][1][1]:
                print(music[i])


def calculate(music):
    sum = 0
    for i in range(len(music)):
        sum += int(time.strftime('%Y')) - int(music[i][1][0])
    return sum


# albums import and conversion to procesable format
list_of_csv_lines = op_csv_to_list()
lista = list_of_list_of_lines(list_of_csv_lines)
music = tupling(lista)
print(music)
while go != '0':
    print(menu)
    go = input()
    if go == '0':
        continue
    if go == '1':
        new_album = add_new_album(template)
        music += new_album
    elif go == '2':
        uni_searching(music)
    elif go == '3':
        age = calculate(music)
        print('age of all albums is ', age)


# overwritting csv file so it contains updated information
to_write_to_csv = list_of_tuple_to_csv(music)
csv_file = open('music.txt', 'w')
csv_file.write(to_write_to_csv)
csv_file.close()