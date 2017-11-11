"""
Created on Sat Nov 11 11:20:36 2017

@author: Noah
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

# tested    
#url_string = 'https://stackoverflow.com/questions/19687421/difference-between-beautifulsoup-and-scrapy-crawler'

# tested
#url_string2 = 'https://stackoverflow.com/questions/8589812/python-iterate-over-a-dictionary'

def scrapeSOPage(url_string):
    print("[" + "SCRAPPING FROM: " + url_string + "]")
    
    # page varable is opened page from url string
    page = urlopen(url_string)
    
    # content is content from the page
    content = page.read()
    
    # soup is content that have been parsed
    soup = BeautifulSoup(content, 'html.parser')
    
    result_dict = {}

    # url 
    result_dict['URL'] = url_string

    # tag
    post_tag_list = soup.find('div', {'class' : 'post-taglist'})
    temp = []
    for post_tag in post_tag_list:
        if len(str(post_tag)) > 10:
            temp.append(post_tag.contents[0])    
    post_tag_list = temp
    result_dict['TAG'] = temp

    # votes, for q and a
    votes = soup.findAll('span', {'itemprop' : 'upvoteCount'})            

    # question    
    question = soup.find('title')
    question = question.contents[0]
    result_dict['QUESTION'] = {'TITLE' : question, 'VOTE' : int(votes[0].contents[0])}

    # anwswer
    answers = soup.findAll('td', {"class" : "answercell"})    
    temp = []   
    for i in range(0,len(answers)):
        temp_answer_tag = answers[i].findAll(['p','pre'])
        
        temp.append((temp_answer_tag, int(votes[i+1].contents[0])))  
        # it would be tuple, (answer, vote)
    result_dict['ANSWERS'] = temp

    return result_dict


