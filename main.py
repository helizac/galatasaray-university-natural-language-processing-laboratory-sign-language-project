import time
from selenium import webdriver
from selenium.webdriver import ActionChains
import urllib.request

PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
LETTERS = ["A", "B", "C", "Ç", "D", "E", "F", "G", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş",
           "T", "U", "Ü", "V", "W", "Y", "Z"]

website_link = "https://tidsozluk.ailevecalisma.gov.tr"

for letter in LETTERS:
    driver.get(website_link + "/tr/Alfabetik/Arama/" + letter + "?")
    time.sleep(.5)
    number_of_pages = len(driver.find_elements_by_xpath("//ul[@class='pagination']/li"))

    links = []
    for i in range(1, number_of_pages):
        driver.get(website_link + "/tr/Alfabetik/Arama/" + letter + "?p=" + str(i))
        time.sleep(.1)
        for j in [my_elem.get_attribute("href") for my_elem in
                  driver.find_elements_by_xpath("//div[@class='rezult_item row']/a")]:
            links.append(j)

    for link in links:
        try:
            driver.get(link)
            time.sleep(1.5)
            number_of_videos = len(driver.find_elements_by_xpath("//div[@class='row']/div/div/video"))
            word = driver.find_element_by_xpath("//div[@class='row']/div/div/h2").text
            multi_words = word.split(", ")
            driver.find_element_by_xpath(
                "//div[@id='sonsayfa_anlam_degiskeleri']/div/div/i[@class='fa fa-expand fa-lg vid_modal']").click()
            video = driver.find_element_by_id("modal_video")
            video_url = video.get_property('src')
            video_url1 = video_url[:video_url.find("-0")]
            video_url2 = video_url[video_url.find("-0") + 4:]
            for i in range(1, number_of_videos + 1):
                for j in multi_words:
                    print(j)
                    try:
                        urllib.request.urlretrieve(f"{video_url1}-0{str(i)}_{video_url2}", j + " " + str(i) + ".mp4")
                    except:
                        print(j + " kelimesinde hata!")
        except Exception as e:
            print(link + " linkinde bir sıkıntı oluştu!\n"+f"Exception : {e}")

driver.quit()
