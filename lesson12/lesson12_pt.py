# 1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, 
# вывести результаты в терминал. Записать результаты в файлы group.json, group.pickle соответственно. 
# В файле group.json указать кодировку utf-8.
import json, pickle
my_favourite_group = {
'name': 'Алиса',
'tracks': ['Моё поколение', 'Тоталитарный рэп'],
'Albums': [{'name': 'Энергия', 'year': 1985}, {'name': 'Посолонь', 'year': 2019}]}

bmfg = pickle.dumps(my_favourite_group);
jmfg = json.dumps(my_favourite_group);
print('Bytes:', bmfg)
print('Json:', jmfg)

with open('lesson12\\mfg.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)

with open('lesson12\\mfg.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

# 2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, 
# прочитать из них информацию. И получить объект: словарь из предыдущего задания.
import json, pickle

with open('lesson12\\mfg.pickle', 'rb') as f:
    mfg1 = pickle.load(f)
print('Bytes: ', mfg1)

with open('lesson12\\mfg.json', 'r', encoding='utf-8') as f:
    mfg2 = json.load(f)
print('Json: ', mfg2)
