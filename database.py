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
    sql_create_table = """CREATE TABLE essays
      (
        Title TEXT,
        Doi TEXT,
        Conference TEXT,
        Section TEXT,
        Year NUMBER,
        Author TEXT,
        Abstract TEXT,
        Keywords TEXT,
        Interest NUMBER,
        Other TEXT
      );"""
    try:
      self.cursor.execute(sql_create_table)
    except:
      pass

  def insert(self,title="",doi="",conference="",section="",year=0,author="",abstract="",keywords="",interest=0,other=""):
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
      if original[1]=="":self.update(identifier,"Doi = \"%s\""%(doi))
      if original[4]==0:self.update(identifier,"Year = %d"%(year))
      if original[5]=="":self.update(identifier,"Author = \"%s\""%(author))
      if original[6]=="":self.update(identifier,"Abstract = \"%s\""%(abstract))
      if original[7]=="":self.update(identifier,"Keywords = \"%s\""%(keywords))
    else:
      sql_insert = """INSERT INTO essays VALUES
      (
        "%s","%s","%s","%s",%d,"%s","%s","%s",%d,"%s"
      );"""%(title,doi,conference,section,year,author,abstract,keywords,interest,other)
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