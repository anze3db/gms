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

    # TODO: Move settings into own model class
    def settingsSet(self, key, value):       
        if self.settingsGet(key):
            self.c.execute("UPDATE settings SET value = ? WHERE key = ?", (value, key))
        else:
            self.c.execute("INSERT INTO settings VALUES(?,?)", (key, value))
            
        
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
    # Usage example:
    db = dbutils()
    
    # Add new key value pair:
    db.settingsSet('foo', 'bar')
    print db.settingsGet('foo')
    
    # Modify value of foo:
    db.settingsSet('foo', 'buz')
    print db.settingsGet('foo')

    # Cleanup:
    db.settingsDelete('foo')
    