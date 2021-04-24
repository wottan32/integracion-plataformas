import hashlib
import requests
import json
import sqlite3
def main_api():
 public = '4d7a4470912fabe21d52b952bd35938d'
 private = 'a8e874c014790a1bf05747e8a4a7b2b000711afd'
 ts = '1'
 hash = hashlib.md5((ts + private + public).encode()).hexdigest()
 
 base = ' http://gateway.marvel.com/v1/public/'
 caracter = requests.get(base + 'characters',
       params={'apikey': public, 'ts': ts, 'hash' : hash, 'name': 'wolverine'}).json()
 nombre = (caracter ['data']['results'][0]['name'])
 descripcion = (caracter ['data']['results'][0]['description'])
 
 con = sqlite3.connect("C:/Users/c.valverde.olivares/Desktop/db")
 cursor = con.cursor()
 cursor.execute('''CREATE TABLE IF NOT EXISTS MARVEL
                     (NOMBRE   TEXT NOT NULL,
      DESCRIPCION TEXT NOT NULL)''')
      
 cursor.execute('''INSERT INTO MARVEL (NOMBRE,DESCRIPCION) VALUES (?,?)''',(nombre,descripcion))
 con.commit()
 cursor.execute('''SELECT * FROM MARVEL''')
 print(cursor.fetchall())
 con.close()
if __name__ == '__main__':
 main_api()