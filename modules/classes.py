import os
import numpy as np
import pandas as pd

class Data_access:
    def __init__(self):
        work_dir = os.getcwd()
        
        self.path_to_prop_spec   = os.path.join(work_dir, 'data', 'prop_spec.csv')
        self.path_to_Thrust_data = os.path.join(work_dir, 'data', 'Thrust_data')
        self.path_to_custom_prop = os.path.join(self.path_to_Thrust_data, 'custom.txt')
        self.path_to_plots       = os.path.join(work_dir, 'data')
        self.path_to_pics        = os.path.join(work_dir, 'data', 'Prop_pics')

        self.check_path = lambda x: os.path.exists(x)

        self.data = Data_access.summary_table(self)
        self.pics_names = os.listdir(self.path_to_pics)
        
    def summary_table(self) -> list:
        data = pd.read_csv(self.path_to_prop_spec, delimiter='\t', index_col=[3])
        return data

    def exp_data(self, work_name):
        '''Получить подробную статистику конкретного пропеллера (коээфиценты тяги и мощности)'''
        path = os.path.join(self.path_to_Thrust_data, work_name)
        if self.check_path(path):
            with open(path, 'r') as inf:
                txt = inf.readlines()
            table = [i.split() for i in txt]
            return pd.DataFrame(table[1:], columns=table[0], dtype='float')
        else:
            return pd.read_csv(self.path_to_custom_prop, delimiter='\t')


class Prop(Data_access):
    '''Создаёт объект пропа, сортирует их по параметрам
    prop = Prop(5, 2)'''
    '''Создаёт объект пропа с переданными параметрами
    get_real_props - возвращает список наиболее похожих пропов, 
                     если не передать параметры поиска явно - возьмёт их из атрибутов класса
                     формат списка - [диаметр, шаг, аббревиатура, имя файла]
    elect_this - получает на вход список параметров, подставляет их в атрибуты класса
    '''
    def __init__(self, d: float, p: float, rpm=5000, tk=0.16, pk=0.1):
        '''Параметры:
        '''
        super().__init__()
        self.d = float(d)
        self.p = float(p)
        self.rpm = int(rpm)
        self.tk = float(tk)
        self.pk = float(pk)

        self.selection = [[d, p, 'custom.txt', 'custom.txt']]
        self.name = 'custom.txt'
        self.work_name = 'custom.txt'

    def current_params(self):
        return [self.d, self.p, self.name, self.work_name]

    def elect_this(self, data):
        """Получает список пропа в формате [диаметр, шаг, аббревиатура, имя файла] и меняет атрибуты объекта"""
        self.d = data[0]
        self.p = data[1]
        self.name = data[2]
        self.work_name = data[3]
        if self.name == 'custom.txt':
            self.tk = 0.16
            self.pk = 0.1
        self.tk = Prop.get_k(self, self.work_name, self.rpm, 'CT')
        self.pk = Prop.get_k(self, self.work_name, self.rpm, 'CP')

    def elect_by_name(self, name):
        if name[-4:] != '.txt':
            name = name + '.txt'
        path = os.path.join(self.path_to_Thrust_data, name)
        if self.check_path(path):
            prp = self.data.loc[name]
            self.elect_this([prp.diam, prp.pitch, prp.short_name, name])

    def get_k(self, name, rpm, coef):
        """Коэффициент винта из датасета. 
        CT - Коэффициент тяги
        CP - Коэффициент мощности"""
        data = self.exp_data(name)
        x = data.RPM
        y = data[coef]
        k = np.interp(rpm, x, y)
        return k

    def one_val_sort(self, val, param, limit=20) -> list: # one_param_sort
        '''Сортирует по одному указанному параметру
        'diam' - сортировка по диаметру
        'pitch' - сортировка по шагу
        Возвращает список сортированных пропов'''
        selection = self.data.sort_values(by=[param], key=lambda x: abs(val - x))
        return selection.index[:limit].to_list()

    def two_val_sort(self, d, p, limit=20) -> list: #two param sort
        """Сортирует по дельте обоих переданных параметров
        Возвращает список сортированных пропов"""
        def delta_sort(x):
            return abs((d if x.name == 'diam' else p) - x)

        data = self.data.sort_values(by=['diam', 'pitch'], key=delta_sort)
        return data.index[:limit].to_list()

class Prop_stats(Prop):
    '''Считает статисику переданных в класс объектов деталей'''
    def __init__(self, d: float, p: float, rpm=5000, tk=0.16, pk=0.1):
        super().__init__(d, p)
        self.d_cm = self.d / 39.37
        self.air_density = 1.2754
        
    def inf(self) -> str:
        return f'Диаметр {self.d}, шаг, {self.p} имя {self.work_name}'

    def calc_thrust(self, rpm, air=1.2754, g=False):
        rpm = int(rpm)
        tk = self.get_k(self.work_name, rpm, 'CT')
        thrust = tk * air * (rpm / 60) ** 2 * self.d_cm ** 4
        return thrust * 9806 if g else thrust
    
    def calc_power(self, rpm, air=1.2754):
        rpm = int(rpm)
        pk = self.get_k(self.work_name, rpm, 'CP')
        return pk * air * (rpm / 60) ** 3 * self.d_cm ** 5