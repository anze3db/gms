#!/usr/bin/python

class settings():
    
    from dbutils import db
    
    c = db().c
    
    @classmethod
    def set(cls, key, value):       
        if cls.get(key):
            cls.c.execute("UPDATE settings SET value = ? WHERE key = ?", (value, key))
        else:
            cls.c.execute("INSERT INTO settings VALUES(?,?)", (key, value))

    
    @classmethod    
    def get(cls, key):
        cmd = "SELECT * FROM settings WHERE key = ?"
        r = cls.c.execute(cmd, (key,)).fetchone()
        from types import NoneType
        if type(r) is NoneType:
            return False
        else:
            return r['value']
    @classmethod    
    def delete(cls, key):
        cmd = "DELETE FROM settings WHERE key = ?"
        cls.c.execute(cmd, (key,))
        
if __name__ == '__main__':
    pass