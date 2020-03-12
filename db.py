import sqlite3 as sql
from card import Card   

class Database:
    def __init__(self):
        pass

    def GetCardByID(self, cardID):
        conn = sql.connect('C:\\Users\\Paul\\Documents\\Projekt\\Discord\\FFTCG Bot\\cards.db')

        c = conn.cursor()

        c.execute("select * from cards")

        result = c.fetchall()
        print(result)
        conn.close()

    def InsertCardByTxt(self, cardData):
        card = Card(cardData)
        conn = sql.connect('C:\\Users\\Paul\\Documents\\Projekt\\Discord\\FFTCG Bot\\cards.db')
        c = conn.cursor()
        c.execute('INSERT INTO "cards" ("cardid","cost","name","ex","type","job","category", "power", "ability") VALUES (?, ?, ?, ?, ?, ?, ?,?,?);', card.ToArray())
        conn.commit()
        conn.close()


    def UpdateCardDataByID(self, cardData):
        card = Card(cardData)
        conn = sql.connect('C:\\Users\\Paul\\Documents\\Projekt\\Discord\\FFTCG Bot\\cards.db')
        c = conn.cursor()
        c.execute(f"update cards set x='', y = ''  where cardid = {card.id}")

        result = c.fetchall()
        print(result)
        conn.close()
        pass    