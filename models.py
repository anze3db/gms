#!/usr/bin/python
from dbutils import db

class settings():
    
    @classmethod
    def set(cls, key, value):   
        k = cls.get(key)    
        if k or k == '':
            db.q("UPDATE settings SET value = ? WHERE key = ?", (value, key))
        else:
            db.q("INSERT INTO settings VALUES(?,?)", (key, value))
    
    @classmethod    
    def get(cls, key):
        
        cmd = "SELECT * FROM settings WHERE key = ?"
        r = db.q(cmd, (key,)).fetchall()
        if len(r) == 0:
            return False
        
        from types import NoneType
        if type(r[0]) is NoneType:
            return ''
        else:
            return r[0]['value']

    @classmethod    
    def delete(cls, key):
                
        cmd = "DELETE FROM settings WHERE key = ?"
        db.q(cmd, (key,))
        
        
if __name__ == '__main__':
    pass