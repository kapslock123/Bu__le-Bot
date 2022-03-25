from selenium import webdriver
from time import sleep
from random import random
from random import uniform
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://bumble.com')

sleep(uniform(5, 10))

#faltu_buttons=driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[3]/button[2]')
#faltu_buttons.click()
faltu_buttons=driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
faltu_buttons.click()

try:
    hold=driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span')
except Exception:
        sleep(80)
        
        hold=driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span')

while(True):
    
    
    
    sleep(random()*10)
    if random()<=0.85:
        print("should like")
        try:
            #//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span
            #//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span
            likebutton=driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')
            likebutton.click()
            print('liked!')
        except Exception:
            try:
                sleep(2)
                likebutton=driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div/div[1]/span')
            
                likebutton.click()
                
                print('liked! 2nd try')
            except Exception:
                print('adios amigos! powering off')
                
    else:
        print("should dislike")
        try:
            #//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span
            #//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span
            #//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span
            #//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span
            dislike_button=driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span')
            dislike_button.click()
            print('disliked :(')
        except Exception:
            try:
                sleep(2)
                dislike_button=driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span')
                dislike_button.click()
                print('disliked :( 2nd try')
            except Exception:
                print('adios amigos! powering off')
                
                