import pickle

test_dict = dict(zip([1, 2, 3], [4, 5, 6]))  # создаст словарь пар "ключ - значение"

# Сериализация
with open("serialization.pkl", "wb") as input_pickle:
    pickle.dump(test_dict, input_pickle)

# Десериализация
with open("serialization.pkl", "rb") as output_pickle:
    loaded_dict = pickle.load(output_pickle)
    print(loaded_dict)
