def make_music_list(list_of_csv_lines):
    print(list_of_csv_lines)

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
music = []

csv_file = open('music.txt')
list_of_csv_lines = csv_file.readlines()
csv_file.close()