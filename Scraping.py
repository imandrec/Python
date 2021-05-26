import sys
import time
from bs4 import BeautifulSoup
import requests

try:
        
    page=requests.get('https://www.amazon.in/Apple-iPhone-11-Pro-256GB/product-reviews/B07XVMJF2D/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')                             # this might throw an exception if something goes wrong.
    
except Exception as e:                                   
    error_type, error_obj, error_info = sys.exc_info()     
    print ('ERROR FOR LINK:',url)                          
    print (error_type, 'Line:', error_info.tb_lineno)      
                                                 
time.sleep(2)   
soup=BeautifulSoup(page.text,'html.parser')
links=soup.find_all('div',attrs={'class':'a-size-base'})   

for i in links:
    print(i.text)
    print("\n")
