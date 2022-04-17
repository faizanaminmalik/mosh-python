import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["trans_id", "prod_id", "price"])
    writer.writerow([100,1,10])
    writer.writerow([101,2,20])

with open("data.csv") as file:
    reader = csv.reader(file)
    #print(list(reader))
    for row in reader:
        print(row)