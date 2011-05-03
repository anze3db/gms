#!/usr/bin/python
from dbutils import db

class settings():
    
    @classmethod
    def set(cls, key, value):   
            
        if cls.get(key):
            db.q("UPDATE settings SET value = ? WHERE key = ?", (value, key))
        else:
            db.q("INSERT INTO settings VALUES(?,?)", (key, value))
    
    @classmethod    
    def get(cls, key):
        
        cmd = "SELECT * FROM settings WHERE key = ?"
        r = db.q(cmd, (key,)).fetchone()
        from types import NoneType
        if type(r) is NoneType:
            return False
        else:
            return r['value']

    @classmethod    
    def delete(cls, key):
                
        cmd = "DELETE FROM settings WHERE key = ?"
        db.q(cmd, (key,))
        
        
if __name__ == '__main__':
    pass