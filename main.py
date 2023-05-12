import csv
import os
from PIL import Image

def z1():
    i = 'C:/Users/Nasta/PycharmProjects/9 лаба 2/1'

    if not os.path.exists('C:/Users/Nasta/PycharmProjects/9 лаба 2/2'):
        os.mkdir('C:/Users/Nasta/PycharmProjects/9 лаба 2/2')

    for f in os.listdir(i):
        if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
            im = Image.open(os.path.join(i,f))
            im = im.resize((500, 500))
            im.save(os.path.join('C:/Users/Nasta/PycharmProjects/9 лаба 2/2', f))
def z2():
    with open("data.csv") as f:
        t_readed = csv.reader(f, delimiter = ",")
        c = 0
        print("Нужно купить")

        for row in t_readed:
            print(f'{row[0]} - {row[1]} шт. за {row[2]} руб.')
            c += 1
        print(f'Всего в файле {c} строк.')


z2()