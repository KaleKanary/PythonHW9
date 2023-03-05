# Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома (median_house_value), 
# где кол-во людей от 0 до 500 (population).

import pandas as pd

# Читаем CSV-файл и создаем DataFrame
df = pd.california_housing_train_csv('data.csv')

# Фильтруем DataFrame по столбцу population
filtered_df = df[df['population'] <= 500]

# Находим медиану столбца median_house_value
median_price = filtered_df['median_house_value'].median()

# Выводим результат
print("Средняя стоимость дома для населения от 0 до 500:", median_price)