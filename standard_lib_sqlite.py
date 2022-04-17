import sqlite3
import json
from pathlib import Path

#get the data from json file and store in movies
movies = json.loads(Path("movies.json").read_text())
print(movies)

with sqlite3.connect("db.sqlite3") as conn:
    #command = "INSERT INTO Movies VALUES(?, ?, ?)"
    #for movie in movies:
      #  conn.execute(command, tuple(movie.values()))
    conn.commit()

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command,) # command returns a cursor object which is iterable
   # for row in cursor:
   #    print(row)

    movies = cursor.fetchall()
    print(movies)
