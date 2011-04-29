#!/usr/bin/python

import sqlite3
from types import NoneType

class dbutils:
    def __init__(self):
        self.conn = sqlite3.connect('gms.db')
        self.conn.row_factory = sqlite3.Row        
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        
    def createDatabase(self):
        cmd = "CREATE TABLE settings (key TEXT, value TEXT);"
        self.conn.execute(cmd)
        self.conn.commit()

    def settingsSet(self, key, value):
        cmd = "SELECT * FROM settings WHERE key = ?"
        r = self.c.execute(cmd, (key,)).fetchone()

        
        if type(r) is NoneType:
            self.c.execute("INSERT INTO settings VALUES(?,?)", (key, value))
            print "inserting new", key, value
        else:
            self.c.execute("UPDATE settings SET value = ? WHERE key = ?", (key, value))
            print "updating old", key, value
        
        self.conn.commit()
        
    def settingsGet(self, key):
        cmd = "SELECT * FROM settings WHERE key = ?"
        r = self.c.execute(cmd, (key,)).fetchone()
        if type(r) is NoneType:
            return False
        else:
            return r['value']
        
    def settingsDelete(self, key):
        cmd = "DELETE FROM settings WHERE key = ?"
        self.c.execute(cmd, (key,))
        self.conn.commit()
        
    

if __name__ == '__main__':
    db = dbutils()
    db.settingsDelete('test')
    print db.settingsGet('test')
    print db.settingsGet('m')
    print db.settingsGet('muca')
    