import sqlite3

class historyDatabase:
   def __init__(self):
       self.con = sqlite3.connect('sql/users.db')
       self.cur = self.con.cursor()
       self.create()
   def create(self):
       self.cur.execute('''
           CREATE TABLE IF NOT EXISTS kill_history
              (
                  login TEXT,
                  id INTEGER,
                  node_id TEXT,
                  avatar_url TEXT,
                  type TEXT,
                  site_admin INTEGER,
                  name TEXT,
                  location TEXT,
                  email TEXT,
                  hireable INTGER,
                  bio TEXT,
                  twitter_username TEXT,
                  public_repos INTEGER,
                  public_gists INTEGER,
                  followers INTEGER,
                  following INTEGER,
                  created_at INTEGER,
                  updated_at INTEGER
              )
        ''')
       self.con.commit()
