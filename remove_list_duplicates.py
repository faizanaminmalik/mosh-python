sample_list = [12,45,35,67,56,56,70,87,70,15,12,15,15]
new_list = []

for item in sample_list:
    if item not in new_list:
        new_list.append(item)
print  (new_list)