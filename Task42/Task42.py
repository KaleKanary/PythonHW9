# Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd

# Читаем CSV-файл и создаем DataFrame
df = pd.read_csv('data.csv')

# Находим минимальное значение столбца population
min_pop = df['population'].min()

# Фильтруем DataFrame по столбцу population, чтобы оставить только строки с минимальным значением population
min_pop_df = df[df['population'] == min_pop]

# Находим максимальное значение столбца households в отфильтрованном DataFrame
max_households = min_pop_df['households'].max()

# Выводим результат
print("Максимальное количество households в зоне минимального значения population:", max_households)