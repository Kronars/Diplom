import os
import csv
import numpy as np

class Props_data:
    def __init__(self):
        '''Создаёт объект данных выбранной детали
        Атрибуты: 
        data: 2д список [диаметр, шаг, аббревиатура, имя файла]
        d_keys: сортированные диаметры без повторений
        p_keys: сортированные шаги без повторений'''
        work_dir = os.getcwd()
        
        self.path_to_prop_spec = os.path.join(work_dir, 'Diplom', 'data', 'prop_spec.csv')
        self.path_to_Thrust_data = os.path.join(work_dir, 'Diplom', 'data', 'Thrust_data')
        self.path_to_plots = os.path.join(work_dir, 'Diplom', 'data')
        self.path_to_pics = os.path.join(work_dir, 'Diplom', 'data', 'Prop_pics')

        self.data = Props_data.parse_prop_spec(self)
        self.d_keys = sorted(set([i[0] for i in self.data]))
        self.p_keys = sorted(set([i[1] for i in self.data]))
        self.pics_names = os.listdir(self.path_to_pics)
        
    def parse_prop_spec(self) -> list:
        """Возвращает список [диаметр(float), шаг(float), аббревиатура, имя файла]"""
        with open(self.path_to_prop_spec, 'r') as inf:
            reader = csv.reader(inf, delimiter='\t')
            props = list(reader)[1:]
        for i, _ in enumerate(props):
            props[i][0], props[i][1] = float(props[i][0]), float(props[i][1])
        return props

    def get_prop_data(self, work_name):
        '''Получить подробную статистику конкретного пропеллера (коээфиценты тяги и мощности)'''
        with open(os.path.join(self.path_to_Thrust_data, work_name), 'r') as inf:
            data = inf.read().split('\n')[1:-1]
            data = [i.split() for i in data]
            data = [[float(j) for j in i] for i in data]
            return data

class Prop(Props_data):
    '''Создаёт объект пропа, не считает статистику, только подбирает наиболее похожие пропы
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

        self.selection = [[10, 5, 'custom.txt', 'custom.txt']]
        self.name = 'custom.txt'
        self.work_name = 'custom.txt'


    def get_params(self):
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
        self.tk = Prop.get_k(self, self.rpm, 't')
        self.pk = Prop.get_k(self, self.rpm, 'p')

    def get_k(self, rpm, mode):
        t_white_list, p_white_list = ['tk', 't', 'thrust'], ['pk', 'p', 'power']
        if mode in t_white_list:
            ind = 1
        elif mode in p_white_list:
            ind = 2
        else:
            raise f"неверно указан режим, получен - {mode}, ожидается: {t_white_list} или {p_white_list}"
        data = Props_data.get_prop_data(self, self.work_name)
        x = np.array([float(i[0]) for i in data])
        y = np.array([float(i[ind]) for i in data])
        return np.interp(rpm, x, y)

    def sorted_props(self, param, mode):
        '''Сортирует все пропы по одному param
        modes:
        'd' - сортировка по диаметрам 
        'p' - сортировка по шагу'''
        if mode == 'd':
            ind = 0
        elif mode == 'p':
            ind = 1
        else:   raise f"неверно указан режим, получен - {mode}, ожидается: 'd' или 'p'"
        delta = lambda x: param - x if param > x else x - param
        selection = sorted(self.data, key=lambda x: delta(x[ind]))
        self.elect_this(selection[0])
        return selection

    def get_real_props(self, d=None, p=None, limit=20) -> list:
        """Подбирает список наиболее похожих пропов в БД,
        если не передать диаметр и шаг явно - возьмёт их из объекта пропа
        Результат записывается в атрибуты selection, name, work_name
        Так же возвращает список подобранных пропов"""
        data = self.data
        selection = []
        d, p = d if d else self.d, p if p else self.p
        d_sort, p_sort = self.d_keys, self.p_keys
        d_flag, p_flag = False, False
        d_diff, p_diff = float(), float()
        d_near, p_near = float(), float()

        aver = lambda x, y: (x + y) / 2
        delta = lambda x, y: x - y if x > y else y - x
        diff_rate = lambda max, min, val: val / ((max-min) / 100)

        d_sort.insert(0, d_sort[0])
        p_sort.insert(0, p_sort[0])

        if d < d_sort[0]:            # РЅР°С…РѕРґРёС‚ СЂР°Р·РЅРёС†Сѓ РµСЃР»Рё Р·РЅР°С‡РµРЅРёРµ РјРµРЅСЊС€Рµ РёР»Рё Р±РѕР»СЊС€Рµ СЃСѓС‰РµСЃС‚РІСѓСЋС‰РµРіРѕ РІ Р‘Р”
            d_diff = diff_rate(d_sort[0], 0, d)
            d_near = d_sort[0]
            d_flag = True
        if p < p_sort[0]:
            p_diff = diff_rate(p_sort[0], 0, p)
            p_near = p_sort[0]
            p_flag = True
        if d > d_sort[-1]:
            d_diff = 100             # СЃРѕРјРЅРёС‚РµР»СЊРЅС‹Р№ РјРѕРјРµРЅС‚, С…Р· РєР°Рє РµРіРѕ РёР·Р±РµР¶Р°С‚СЊ
            d_near = d_sort[-1]
            d_flag = True
        if p > p_sort[-1]:
            p_diff = 100
            p_near = p_sort[-1]
            p_flag = True

        if p_flag and d_flag:
            selection = filter(lambda x: d_near == x[0], data)
            selection = filter(lambda x: p_near == x[1], data)
            return sorted(list(selection), key=lambda x: x[0], reverse=1)

        if not d_flag:              # РµСЃР»Рё РЅРµ РЅР°Р№РґРµРЅ РїРѕ РґРёР°РјРµС‚СЂСѓ
            for i in range(1, len(d_sort)):
                if d_sort[i] >= d:
                    daver = aver(d_sort[i-1], d_sort[i])
                    if d > daver:
                        d_diff = diff_rate(d_sort[i], daver, d_sort[i] - d)
                        d_near = d_sort[i]
                    else:
                        d_diff = diff_rate(daver, d_sort[i-1], d - d_sort[i-1])
                        d_near = d_sort[i-1]
                    d_flag = True
                    break

        if not p_flag:              # РµСЃР»Рё РЅРµ РЅР°Р№РґРµРЅ РїРѕ С€Р°РіСѓ
            for i in range(1, len(p_sort)):
                if p_sort[i] >= p:
                    paver = aver(p_sort[i-1], p_sort[i])
                    if p > paver:
                        p_diff = diff_rate(p_sort[i], paver, p_sort[i] - p)
                        p_near = p_sort[i]
                    else:
                        p_diff = diff_rate(paver, p_sort[i-1], p - p_sort[i-1])
                        p_near = p_sort[i-1]
                    p_flag = True
                    break

        if d_flag and p_flag:
            if d_diff < p_diff:
                selection = filter(lambda x: d_near == x[0], data)
            else:
                selection = filter(lambda x: p_near == x[1], data)
            repl = list(sorted(selection, key=lambda x: delta(p_near, x[1]) if d_diff < p_diff else delta(d_near, x[0])))
            self.name = repl[0][2]
            self.work_name = repl[0][3]
            self.selection = repl
            return repl[:limit]

class Prop_stats(Prop):
    '''Считает статисику переданных в класс объектов деталей'''
    def __init__(self, d: float, p: float, rpm=5000, tk=0.16, pk=0.1):
        super().__init__(d, p)
        self.d_cm = self.d / 39.37
        self.air_density = 1.2754
        self.prop_tp_data = self.get_prop_data(self.work_name)
        
    def inf(self) -> str:
        return f'Диаметр {self.d}, шаг, {self.p} имя {self.work_name}'

    def calc_thrust(self, rpm, g=False):
        rpm = int(rpm)
        d_cm = self.d / 39.37
        thrust = self.tk * self.air_density * (rpm / 60) ** 2 * d_cm ** 4
        return thrust * 9806 if g else thrust
    
    def calc_power(self, rpm):
        rpm = int(rpm)
        d_cm = self.d / 39.37
        return self.pk * self.air_density * (rpm / 60) ** 3 * d_cm ** 5