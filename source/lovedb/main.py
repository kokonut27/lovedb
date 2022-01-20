import sqlite3
import os
import json
# from replit import db

class nonexistingfile(Exception):
  pass
class dberror(Exception):
  pass
class nonexistingtypeofdb(Exception):
  pass

class lovedb:
  def __init__(self, db_name):
    try:
      f = open(db_name)
    except:
      raise nonexistingfile("no such file exists!")
    
    self.db = f

  def create(db_name, type_db, code=None):
    try:
      f = open(db_name, "w")

      if code != None:
        with open("schema.sql", "w") as schema:
          schema.write(code)
      if type_db not in ["table", "slots"]: # will add more later
        raise nonexistingtypeofdb("no such type of db exists!")
    except:
      raise dberror("the database could not be created due to some error! try again!")