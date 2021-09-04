from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep

numType = 1

def initialize():
  chrome_options = ChromeOptions()
  # chrome_options.add_argument('--headless')
  prefs = {
              'profile.default_content_setting_values': {
                   'images': 2,
                'javascript': 2
                }
             }
  chrome_options.add_experimental_option('prefs', prefs)
  browser = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe",options=chrome_options)
  return browser

def getPage(url,option=0):
  if option==1:
    return BeautifulSoup(url.page_source,features="html.parser")
  try:
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
    request = Request(url=url,headers=headers)
    html = urlopen(request).read()
  except:
    return None
  else:
    return BeautifulSoup(html,features="html.parser")

def getCategoryUrl(mainUrl):
  mainPage = getPage(mainUrl+"/Academic_Evaluation/By_category")
  links = []
  for link in mainPage.find("div",{"class":"col-md-2"}).find_all("a"):
    if "href" in link.attrs:
      if "Contact_Us" not in link.attrs["href"] and "By_category" not in link.attrs["href"] and "Academic_Evaluation" in link.attrs["href"]:
        categoryUrl = mainUrl+(link.attrs["href"])
        links.append({"title":link.attrs["title"],"url":categoryUrl})
  return links

def getConferenceUrl(categoryUrl):
  categoryPage = getPage(categoryUrl["url"])
  links = []
  try:
    sections = categoryPage.find_all("ul",{"class":"g-ul x-list3"})
    sectionName = {"Journal A":0,"Journal B":1,"Journal C":2,"Conference A":3,"Conference B":4,"Conference C":5}
    for link in sections[sectionName["Conference A"]].find_all("a"):
      if "href" in link.attrs:
        conferenceUrl = link.attrs["href"]
        conferenceStrs = conferenceUrl.split("/")
        index = conferenceStrs.index("conf")+1
        conferenceLink = link.attrs["href"]
        if conferenceLink[-4:]!="html":
          conferenceLink = conferenceLink+"index.html"
        links.append({"title":conferenceStrs[index],"url":conferenceLink})
  except:
    pass
  return links

def getSectionUrl(conferenceUrl):
  sectionPage = getPage(conferenceUrl["url"])
  links = []
  try:
    meetings = sectionPage.find_all("ul",{"class":"publ-list"})
    for i in range(numType):
      for link in meetings[i].find_all("a",{"class":"toc-link"}):
        if "href" in link.attrs:
          sectionUrl = link.attrs["href"]
          sectionStrs = re.split("[/.]", sectionUrl)
          index = sectionStrs.index("conf")+2
          links.append({"title":sectionStrs[index],"url":sectionUrl})
  except:
    pass
  return links

def getPaperUrl(sectionUrl):
  paperPage = getPage(sectionUrl["url"])
  links = []
  try:
    papers = paperPage.find_all("ul",{"class":"publ-list"})
    for part in papers:
      for entry in part.find_all("li",{"class":"entry inproceedings"}):
        title = entry.find("span",{"class":"title"})
        title = title.get_text()
        try:
          doiLink = entry.find("a",href=re.compile("https://doi.org/.*"))
          doiLink = doiLink.get("href")
          doiLink = str(doiLink)
          doi=doiLink.replace("https://doi.org/","")
        except:
          doi = ""
        links.append({"title":title,"doi":doi,"url":doiLink})
  except:
    pass
  return links

def getInfo(paperUrl,browser):
  info = {"title":paperUrl["title"],"doi":paperUrl["doi"]}
  print(paperUrl["title"])
  if len(paperUrl["doi"])>1:
    doi = paperUrl["doi"].replace("/","%2F")
    link = "https://xueshu.baidu.com/s?wd="+doi+"&ie=utf-8&tn=SE_baiduxueshu_c1gjeupa&sc_from=&sc_as_para=sc_lib%3A&rsv_n=2&rsv_sug2=0"
  else:
    searchTitle = paperUrl["title"].replace(" ","+")
    link = "https://xueshu.baidu.com/s?wd="+searchTitle+"&ie=utf-8&tn=SE_baiduxueshu_c1gjeupa&sc_from=&sc_as_para=sc_lib%3A&rsv_n=2&rsv_sug2=0"
  browser.get(link)
  #print(link)
  try:
    more_button = browser.find_element_by_class_name("abstract_more")
    more_button.click()
  except:
    #print("No extension.")
    pass
  infoPage = getPage(browser,1)
  try:
    author_text = infoPage.find("p",{"class":"author_text"})
    author_list = author_text.find_all("a")
    authors = ""
    for author in author_list:
      authors = authors+author.get_text()+", "
    info["author"] = authors
  except:
    #print("No author.")
    info["author"] = ""
  try:
    abstract = infoPage.find("p",{"class":"abstract kw_main_s"})
    info["abstract"] = abstract.get_text()
  except:
    try:
      abstract = infoPage.find("p",{"class":"abstract"})
      info["abstract"] = abstract.get_text()
    except:
      #print("No abstract.")
      info["abstract"] = ""
  try:
    keywords = infoPage.find("div",{"class":"kw_wr"})
    keywords = keywords.find("p",{"class":"kw_main"})
    info["keywords"] = keywords.get_text()
  except:
    #print("No keywords.")
    info["keywords"] = ""
  try:
    year = infoPage.find("div",{"class":"year_wr"})
    year = year.find("p",{"class":"kw_main"})
    info["year"] = int(year.get_text())
  except:
    #print("No year.")
    info["year"] = 0
  return info