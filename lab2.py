# Задание 1
from copyreg import dispatch_table
import numpy as np
import pandas as pd
def zadanie1():
    massive = np.linspace(0,10,50,endpoint=False,dtype=np.float64)
    massive = massive ** 0.5
    massive = massive[::-2]
    massive = np.vstack((massive, np.logspace(1,2,len(massive),dtype=np.float64)))
    avg = list()
    for i in range(len(massive[0])):
        avg.append((massive[0,i]*massive[0,i]) ** 0.5)
    massive1 = np.linspace(-3,3,1000,endpoint=False,dtype=np.float64)
    massive1 = np.sin(massive1)
    min_val = min(massive1)
    max_val = max(massive1)
    avg_val = sum(massive1)/1000
    mediam_of_mass = np.median(massive1)
    disp_of_mass = np.std(massive1)
    return avg, min_val, max_val, avg_val, mediam_of_mass, disp_of_mass

print(zadanie1())
# Задание 2
def zadanie2():
    dt = pd.DataFrame(np.zeros(shape=(10,5))/2., columns=['тип','цвет','масса','размер','стоимость'], index=['яблоко', 'банан', 'апельсин', 'мандарин', 'груша', 'персик', 'картошка', 'морковь', 'лук', 'капуста'])
    for col, x in dt.iteritems():
        if col == ('тип'):
            if (x.index).issubset(['яблоко','банан','апельсин','мандарин','груша','персик']):
                dt[x.index, 'тип'] = 'фрукт'
            else:
                dt[x.index, 'тип'] = 'овощ'

    return dt

print(zadanie2())