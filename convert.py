import csv
import json

# Import data
to_json = []
with open('USvideos.csv', encoding='utf-8') as file:
    reader = csv.reader(file)

    catagories = next(reader)
    num_rows = 40940 #sum(1 for row in reader)

    print(catagories)

    for i in range(num_rows):
        try:
            row = next(reader)
            if len(row) == 16: # Check for wierdly delimited data
                temp = {}
                for i in range(len(catagories)):
                    temp[catagories[i]] = row[i]

                to_json.append(temp)
        except:
            pass

with open('data.json', 'w') as file:
    json.dump(to_json, file)
