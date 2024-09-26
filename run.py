import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM


print('=======================================================================================')
print('Hey! You need to manually login to tiktok. I will wait 1 minute for to login manually!')
print('=======================================================================================')
time.sleep(8)
print('Bot is now running! Please log into TikTok')
time.sleep(4)

options = webdriver.ChromeOptions()
bot = webdriver.Chrome(options=options,  executable_path=CM().install())
bot.set_window_size(1680, 900)

bot.get('https://www.tiktok.com/login')
ActionChains(bot).key_down(Keys.CONTROL).send_keys(
    '-').key_up(Keys.CONTROL).perform()
ActionChains(bot).key_down(Keys.CONTROL).send_keys(
    '-').key_up(Keys.CONTROL).perform()
print('Waiting 50s for manual login...')
time.sleep(50)
bot.get('https://www.tiktok.com/upload/?lang=en')
time.sleep(3)

def addCaption():
    while(True):
        choice='x'
        caption='x'
        print("Please enter caption and press Enter")
        caption=input()
        print("Are you sure you want this to be your caption - Yes or No \n" + caption)
        choice=input()
        if(choice == 'YES'):
            f=open("caption.txt", 'w')
            f.write(caption)
            print("Caption Saved!")
            return True
        elif(choice == 'NO'):
            print("Caption not Saved!")

def addHashtags():
    loop1=True
    loop2=True
    while(loop1==True):
        hashTag = 'x'
        choice1='x'
        choice2='x'
        choice3='x'
        print("Add Hashtags? - Yes or No")
        choice1=input()
        if(choice1 =='YES'):
            while(loop2==True):
                print("Add your hashtag and press Enter")
                hashTag='#'+input('#')
                print("Add this hashtag to post? - Yes or No\n", hashTag)
                choice2=input()
                if(choice2 =='YES'):
                    with open("caption.txt", "a") as f:
                        f.write('\n'+hashTag)
                    print("Hashtag Saved!")
                    print("Add another Hashtag? - Yes or No")
                    choice3=input()
                    if(choice3=='YES'):
                        continue
                    else:
                        loop2=False
                elif(choice2=='NO'):
                    print('Hastag not Saved')
                    loop1=False
                    loop2=False
        else:
            return False
    loop1=False

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False

    return True


def upload(video_path):
    while True:
        file_uploader = bot.find_element_by_xpath(
            '//*[@id="main"]/div[2]/div/div[2]/div[2]/div/div/input')

        file_uploader.send_keys(video_path)

        caption = bot.find_element_by_xpath(
            '//*[@id="main"]/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/span')

        bot.implicitly_wait(10)
        ActionChains(bot).move_to_element(caption).click(
            caption).perform()

        with open(r"caption.txt", "r") as f:
            tags = [line.strip() for line in f]

        for tag in tags:
            ActionChains(bot).send_keys(tag).perform()
            time.sleep(2)
            ActionChains(bot).send_keys(Keys.RETURN).perform()
            time.sleep(1)

        time.sleep(5)
        bot.execute_script("window.scrollTo(150, 300);")
        time.sleep(5)

        post = WebDriverWait(bot, 100).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]/div[5]/button[2]')))

        post.click()
        time.sleep(30)

        if check_exists_by_xpath(bot, '//*[@id="portal-container"]/div/div/div[1]/div[2]'):
            reupload = WebDriverWait(bot, 100).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="portal-container"]/div/div/div[1]/div[2]')))

            reupload.click()
        else:
            print('Unknown error cooldown')
            while True:
                time.sleep(600)
                post.click()
                time.sleep(15)
                if check_exists_by_xpath(bot, '//*[@id="portal-container"]/div/div/div[1]/div[2]'):
                    break

        if check_exists_by_xpath(bot, '//*[@id="portal-container"]/div/div/div[1]/div[2]'):
            reupload = WebDriverWait(bot, 100).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="portal-container"]/div/div/div[1]/div[2]')))
            reupload.click()

        time.sleep(1)


    

# ================================================================
# Here is the path of the video that you want to upload in tiktok.
# Plese edit the path because this is different to everyone.
upload(r"C:\Users\redi\Videos\your-video-here.mov")
# ================================================================
