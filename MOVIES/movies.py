import sqlite3
mov = sqlite3.connect('lismovies.db')
c = mov.cursor()
c.execute("""CREATE TABLE movies (
        movie_name text,
        lead_actor text,
        actress text,
        release_year text,
        director text    
    )""")
movie_list = [
              ('Drishyam',' Mohanlal','Meena','2013','Jeethu Joseph'),
              ('Lucifer ', 'Mohanlal',' Manju Warrier','2019','Prithviraj Sukumaran'),
              ('Dhoom 3','Aamir Khan',' Katrina Kaif','2013','Vijay Krishna Acharya '),
              ('Oppam','Mohanlal','Anusree','2016','Priyadarshan'),
              ('Jurassic Park','Sam Neill','Laura Dern','1993','Steven Spielberg'),
              ('Pirates of the Caribbean The Curse of the Black Pearl','Johnny Depp','Keira Knightley','2003','Gore Verbinski'),
              ('johnny english strikes again','Rowan Atkinson','Olga Kurylenko','2018','David Kerr'),
              ('Njan Prakashan','Fahadh Faasil','Anju Kurian','2018','Sathyan Anthikad'),
              ]
c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)", movie_list )
c.execute("SELECT * FROM movies")
c.execute("SELECT * FROM movies WHERE lead_actor = 'Mohanlal' ")
items = c.fetchall()
for item in items:
    print(item) 
mov.commit()
mov.close()
