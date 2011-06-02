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
        
class gestures():
    @classmethod
    def get_apps(cls):
       cmd = "SELECT * FROM apps"
       r = db.q(cmd).fetchall()
       return r 
    
    @classmethod
    def add_app(cls, name):
        cmd = "INSERT INTO apps (name) VALUES(?)"
        db.q(cmd, (name,))
    
    @classmethod
    def remove_app(cls, name):
        app_id = gestures._get_id_from_name(name)
        print name, app_id
        cmd = "DELETE FROM apps WHERE id = ?"
        db.q(cmd, (app_id,))
        
        cmd = "DELETE FROM gestures WHERE id_app = ?"
        db.q(cmd, (app_id,))
        
    @classmethod
    def _get_id_from_name(cls, name):
        cmd = "SELECT * FROM apps WHERE name = ?"
        r = db.q(cmd, (name,)).fetchall()

        if r == []:
            return 0
        else:
            return r[0]['id']
        

if __name__ == '__main__':
    from pprint import pprint
    # gestures.add_app("gedit")
    # gestures.remove_app('323')
    for i in gestures.get_apps():
        print i, i[1]   
        
        
     
