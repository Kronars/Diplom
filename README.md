##  Подбор и автоматизированный расчёт характеристик воздушных винтов

Цель дипломной работы - разработка программного обеспечения для удобного анализа харктеристик и подбора воздущных винтов мультироторных беспилотных систем.  
  
Приложение находится в разработке, на данных момент интерфейс выглядит так:  

![image](https://user-images.githubusercontent.com/95420558/169510503-df194e0e-0657-4c61-b667-56d6098adc61.png)

> Поля со средней и максимальной скоростью на данный момент в разработке    

Реализованы три алгоритма подбора:  
 * По соотвествию диаметру
 * По соответстивю шага винта
 * По обоим параметра  
  
Производится расчёт тяги только для статических условий, расчёт характеристик в динамике в разработке.  
Формулы используемые для расчёта:  
```
      T = tk * p * n² * d⁴  
      N = pk * p * n³ * d⁵  
```
Где T- тяга, N - мощность  
  
Коэффиценты тяги и мощности взяты из измерений Департамента аэрокосмической техники и Университета Иллинойс в Урбана-Шампейн в США.  
Сайт с датасетами: https://m-selig.ae.illinois.edu/props/propDB.html  
Из всего датасета используются данные о 218 винтах.  
