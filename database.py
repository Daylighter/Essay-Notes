import sqlite3
import re

class EssayBase():
  def __init__(self,file_name):
    self.file_name = file_name
    self.insert_duration = 10
    self.insert_count = 0
    [self.database,self.cursor] = self._create_cursor()
    self._create_table()

  def _create_cursor(self):
    database = sqlite3.connect(self.file_name)
    cur = database.cursor()
    return [database,cur]

  def _create_table(self):
    sql_create_table = """CREATE TABLE "essays" (
      "Title"	TEXT NOT NULL,
      "Url"	TEXT NOT NULL,
      "Abstract"	TEXT NOT NULL,
      "Keywords"	TEXT NOT NULL,
      "Date"	TEXT NOT NULL DEFAULT 0,
      "Doi"	TEXT NOT NULL,
      "Conference"	TEXT NOT NULL,
      "Section"	TEXT NOT NULL,
      "Year"	NUMBER NOT NULL DEFAULT 0,
      "Author"	TEXT NOT NULL,
      "Interest"	NUMBER NOT NULL DEFAULT 0
    );"""
    try:
      self.cursor.execute(sql_create_table)
    except:
      pass

  def insert(self,title="",url="",abstract="",keywords="",date="0",doi="",conference="",section="",year=0,author="",interest=0):
    title = re.sub("[\"]","\'",title)
    conference = re.sub("[\"]","\'",conference)
    section = re.sub("[\"]","\'",section)
    author = re.sub("[\"]","\'",author)
    abstract = re.sub("[\"]","\'",abstract)
    keywords = re.sub("[\"]","\'",keywords)
    identifier = "Title = '%s'"%(title)
    search_result = self.search(identifier)
    if len(search_result)>0:
      original = search_result[0]
      if original[5]=="":self.update(identifier,"Doi = \"%s\""%(doi))
      if original[8]==0:self.update(identifier,"Year = %d"%(year))
      if original[9]=="":self.update(identifier,"Author = \"%s\""%(author))
      if original[2]=="":self.update(identifier,"Abstract = \"%s\""%(abstract))
      if original[3]=="":self.update(identifier,"Keywords = \"%s\""%(keywords))
    else:
      sql_insert = """INSERT INTO essays VALUES
      (
        "%s","%s","%s","%s","%s","%s","%s","%s",%d,"%s",%d
      );"""%(title,url,abstract,keywords,date,doi,conference,section,year,author,interest)
      self.cursor.execute(sql_insert)
    if self.insert_count%self.insert_duration==0:
      self.database.commit()
    self.insert_count = self.insert_count+1

  def search(self,condition):
    sql_search = "SELECT * FROM essays WHERE %s;"%(condition)
    self.cursor.execute(sql_search)
    return self.cursor.fetchall()

  def update(self,identifier,update_data):
    sql_update = "UPDATE essays SET %s WHERE %s;"%(update_data,identifier)
    self.cursor.execute(sql_update)
    self.database.commit()

  def delete(self,identifier):
    sql_delete = "DELETE FROM essays WHERE %s;"%(identifier)
    self.cursor.execute(sql_delete)
    self.database.commit()

  def finalize(self):
    self.database.commit()
    self.cursor.close()
    self.database.close()