import csv
import numpy as np
import matplotlib.pyplot as plt

class Spares_stats:
    def __init__(self, prop=False, motor=False, batt=False):
        '''Создаёт объект данных выбранной детали
        Атрибуты: 
        data: список [диаметр, шаг, аббревиатура, имя файла]s
        d_keys: сортированные диаметры без повторений
        p_keys: сортированные шаги без повторений'''
        self.path_to_prop_spec = 'C:\\Users\\Senya\\Prog_2\\Kyrsach\\Proga\\prop_spec.csv'
        self.path_to_Thrust_data = 'C:\\Users\\Senya\\Prog_2\\Kyrsach\\Proga\\Thrust_data\\'
        if prop:
            self.data = Spares_stats.create_prop_sizes(self)
            self.d_keys = sorted(set([i[0] for i in self.data]))
            self.p_keys = sorted(set([i[1] for i in self.data]))
        if motor:
            pass
        if batt:
            pass
        
    def create_prop_sizes(self) -> list:
        """Возвращает список [диаметр, шаг, аббревиатура, имя файла]"""
        with open(self.path_to_prop_spec, 'r') as inf:
            reader = csv.reader(inf, delimiter='\t')
            props = list(reader)[1:]
        for i, _ in enumerate(props):
            props[i][0], props[i][1] = float(props[i][0]), float(props[i][1])
        return props

    def get_prop_data(self, work_name):
        '''Получить подробную статистику конкретного пропеллера (коээфиценты тяги и мощности)'''
        with open(self.path_to_Thrust_data + work_name, 'r') as inf:
            data = inf.read().split('\n')[1:-1] #-1 РёР· Р·Р° \n  РІ РєРѕРЅС†Рµ
            data = [i.split() for i in data]
            data = [[float(j) for j in i] for i in data]
            return data

class Prop:
    '''Создаёт объект пропа из объекта данных пропа, не считает статистику, только подбирает наиболее похожий пропы
    data = Spares_stats(prop=True)
    prop = Prop(data, 5, 2)'''
    def __init__(self, data: Spares_stats, d: float, p: float, rpm=5000, tk=0.16, pk=0.1):
        '''Параметры:
        '''
        self.props_data = data.data
        self.d_keys = data.d_keys
        self.p_keys = data.p_keys
        self.d = float(d)
        self.p = float(p)
        self.rpm = int(rpm)
        self.tk = float(tk)
        self.pk = float(pk)
        self.selection = [[1, 1, 'пропеллер не определён', 'пропеллер не определён']]
        self.name = 'ancf'
        self.work_name = 'ancf_10x5_static_0755od.txt'
        self.done = False

    def re_elect(self, data):
        """Получает список пропа в формате self.selection и меняет атрибуты объекта"""
        self.name = data[2]
        self.work_name = data[3]
        self.d = data[0]
        self.p = data[1]
        self.tk = Prop.get_tk(self, self.rpm)
        self.pk = Prop.get_pk(self, self.rpm)
        
    def get_tk(self, rpm):
        """Если проп есть в БД тяг, возвращает коээфицент тяги на определённых rpm, иначе - не меняет коэфф"""
        try:
            data = Spares_stats.get_prop_data(self, self.work_name)
        except AttributeError:
            return self.tk
        x = np.array([float(i[0]) for i in data])
        y = np.array([float(i[1]) for i in data])
        return np.interp(self.rpm, x, y)
    
    def get_pk(self, rpm):
        """Если проп есть в БД тяг, возвращает коээфицент тяги на определённых rpm, иначе - не меняет коэфф"""
        try:
            data = Spares_stats.get_prop_data(self, self.work_name)
        except AttributeError:
            return self.pk
        x = np.array([float(i[0]) for i in data])
        y = np.array([float(i[2]) for i in data])
        return np.interp(self.rpm, x, y)

    def get_real_props(self, d=None, p=None, limit=7):
        """Подбирает список наиболее похожих пропов в БД,
        если не передать диаметр и шаг явно - возьмёт их из объекта пропа"""
        data = self.props_data
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
            self.done = True
            return repl[:5]

class Quad:
    '''Считает статисику переданных в класс объектов деталей'''
    def __init__(self, prop, rpm=5000):
        self.prop = prop
        self.prop_name = prop.name
        self.prop_work_name = prop.work_name
        self.prop_inf = f'Диаметр {prop.selection[0][0]}, шаг {prop.selection[0][1]} имя {prop.selection[0][3]}'
        self.d = prop.d
        self.d_cm = prop.d / 39.37
        self.p = prop.p
        self.tk = prop.tk
        self.pk = prop.pk
        self.rpm = rpm
        self.air_density = 1.2754
        data = Spares_stats()
        self.prop_tp_data = data.get_prop_data(self.prop_work_name)

    def calc_thrust(self, rpm, g=False):
        rpm = int(rpm)
        if g:
            return (self.tk * self.air_density * (rpm / 60) ** 2 * self.d_cm ** 4) / 9.806 * 1000
        return self.tk * self.air_density * (rpm / 60) ** 2 * self.d_cm ** 4
    
    def calc_power(self, rpm):
        rpm = int(rpm)
        return self.pk * self.air_density * (rpm / 60) ** 3 * self.d_cm ** 5
    
    def draw_prop_stats(self, path, rpm_x=5000):
        data = self.prop_tp_data
        f, (th_ax, pw_ax) = plt.subplots(1, 2, gridspec_kw={'wspace': 0.3})
        f.set_size_inches(8.3, 3.8)
        
        rpms = np.linspace(data[0][0] - 400, data[-1][0], 20)
        thr_rpm_y = Quad.calc_thrust(self, rpm_x, g=1)
        pwr_rpm_y = Quad.calc_power(self, rpm_x)
        thr = np.array([(Quad.calc_thrust(self, i, g=1)) for i in rpms])
        pwr = np.array([(Quad.calc_power(self, i)) for i in rpms])

        th_ax.plot(rpms, thr, color='orange')
        th_ax.scatter(rpm_x, thr_rpm_y, marker='x', c='red')
        th_ax.grid(linestyle='--')
        th_ax.set_title('График тяги ' + self.prop_name)
        th_ax.set_xlabel('Обороты в минуту')
        th_ax.set_ylabel('Грамм-силы')

        pw_ax.plot(rpms, pwr)
        pw_ax.scatter(rpm_x, pwr_rpm_y, marker='x', c='red')
        pw_ax.grid(linestyle='--')
        pw_ax.set_title('График требуемой мощности ' + self.prop_name)
        pw_ax.set_xlabel('Обороты в минуту')
        pw_ax.set_ylabel('Ватт')

        plt.savefig(path + r'\plot.png')
        return f