values = list(range(5))
print(values)
values = [*range(5)]
print(values)
values = [*range(5), *"Hello"]
print(values)
values_2 = (*values, "a", *"Hello")
print(values_2)

print("************************************")
#Dictionary

first = {"x": 1}
second = {"x": 10,"y": 20}
combined = {**first, **second, "z": 11}
print(combined)

