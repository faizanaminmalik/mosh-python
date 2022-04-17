import json
from pathlib import Path

# create a list of dictionaries

movies = [
    {"id": 3, "title": "Terminator2", "year": 1990},
    {"id": 4, "title": "Twilight2", "year": 2007}
]

# Write data to JSON file
data = json.dumps(movies)
Path("movies.json").write_text(data)

print("*********** Read data from json file ***********")
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0]) # get only 1st dictionary data
print(movies[0]["title"]) # Get title only of 1st dictionary data