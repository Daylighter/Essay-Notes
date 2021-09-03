from crawler import *
from database import EssayBase

def main():
  database = EssayBase("./essays.db")
  operationType = input("Operation to take:")
  if operationType == "crawl":
    crawlType = input("Conference to crawl:")
    crawlSection = input("Section to crawl:")
    startIndex = int(input("start from:"))
    endIndex = int(input("end with:"))
    browser = initialize()
    conferenceUrl = {"title":crawlType,"url":"https://dblp.uni-trier.de/db/conf/"+crawlType+"/index.html"}
    if crawlSection=="all":
      sectionUrls = getSectionUrl(conferenceUrl)
    else:
      sectionUrls = [{"title":crawlSection,"url":"https://dblp.uni-trier.de/db/conf/"+crawlType+"/"+crawlSection+".html"}]
    for sectionUrl in sectionUrls:
      try:
        paperUrls = getPaperUrl(sectionUrl)
        index = 0
        for paperUrl in paperUrls:
          print(index)
          if index<startIndex:
            index = index+1
            continue
          elif index>endIndex:
            break
          else:
            index = index+1
            if index%100==0:
              browser = initialize()
          try:
            paperInfo = getInfo(paperUrl,browser)
            database.insert(title=paperInfo["title"],doi=paperInfo["doi"],conference=conferenceUrl["title"],section=sectionUrl["title"],\
              year=paperInfo["year"],author=paperInfo["author"],abstract=paperInfo["abstract"],keywords=paperInfo["keywords"],interest=0,other="")
          except Exception as e:
            print(e)
            print("Insertion failed.")
            continue
      except:
        print("Paper not found.")
        continue
  elif operationType == "delete":
    deleteCondition = input("Condition to delete:")
    database.delete(deleteCondition)
  database.finalize()

main()