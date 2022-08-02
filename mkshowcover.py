#!/usr/bin/env python
# coding: utf-8

# In[53]:


from logging import info
import sys
import time
import subprocess
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# In[41]:
subprocess.Popen(['notify-send', 'Downloading show poster'])


wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = Options()
options.add_argument('--user-data-dir=/home/hazem/.config/google-chrome/System Profile')


# In[42]:


term = sys.argv[1]
term_pluses = term.replace(' ', '+')+'+poster'
google_images_url = f'https://www.google.com/search?q={term_pluses}&sxsrf=ALiCzsaSwQF-jHx83wxnkHwVsQx5TgkumQ:1658170583191&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiJx9nkjoP5AhUF7xoKHX54CGwQ_AUoAnoECAIQBA&biw=765&bih=770&dpr=1.25'


# In[43]:


wd.get(google_images_url)


# In[44]:


first_img_a_tag = wd.find_element(
    By.CSS_SELECTOR,
    "div.islrc > div > a"
)
first_img_a_tag.click()


# In[55]:



img = wd.find_element(
    By.CSS_SELECTOR,
    "div.v4dQwb > a > img"
)


# wd.save_screenshot(img_src)


while True:
    try:
        img_src = img.get_attribute('src')
        img_data = requests.get(img_src).content
        with open(f'{sys.argv[2]}/.cover.jpg', 'wb') as handler:
            handler.write(img_data)

        info('Success')

        break;
    except requests.exceptions.InvalidSchema as e:
        subprocess.Popen(['notify-send', f'{e}trying again...'])
        time.sleep(1)

    except Exception as e: 
        subprocess.Popen(['notify-send', f'ERROR happened {e}'])
        break;

subprocess.Popen(['notify-send', f'Image Downloaded'])
 


wd.close()
