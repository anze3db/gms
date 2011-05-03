#!/usr/bin/python

class db:
    
    @staticmethod
    def q(sql, params = ()):
        import sqlite3
        conn = sqlite3.connect('gms.db')
        conn.row_factory = sqlite3.Row        
        c = conn.cursor()
        
        query = c.execute(sql, params)
        
        conn.commit()
        
        # TODO: If I close it here fetchall() doesn't work later:
        #conn.close()
        
        return query

    @staticmethod        
    def createDatabase():
        cmd = "CREATE TABLE settings (key TEXT, value TEXT);"
        db.q(cmd)

if __name__ == '__main__':
    pass
    