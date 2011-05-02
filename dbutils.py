#!/usr/bin/python

import sqlite3

class db:
    def __init__(self):
        self.conn = sqlite3.connect('gms.db')
        self.conn.row_factory = sqlite3.Row        
        self.c = self.conn.cursor()
        

    def __del__(self):
        #self.conn.close()
        pass
        
    def createDatabase(self):
        cmd = "CREATE TABLE settings (key TEXT, value TEXT);"
        self.conn.execute(cmd)
        self.conn.commit()

if __name__ == '__main__':
    pass
    