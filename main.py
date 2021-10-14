import smtplib
from emails import receivers
from email.mime.text import MIMEText

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

sender = "edwardcordero98.stockdrops@gmail.com"
user = 'edwardcordero98.stockalerts@gmail.com'
password = 'Uncannyedward98!'

test = "https://www.target.com/p/california-costumes-gator-man-adult-costume/-/A-80422215?preselect=80422214#lnk=sametab"
MicrosoftXboxEliteController = "https://www.microsoft.com/en-us/d/xbox-elite-wireless-controller-series-2-halo-infinite-limited-edition/90z8k1dbj8zd"
MicrosoftTest = "https://www.microsoft.com/en-us/d/xbox-wireless-controller-daystrike-camo-special-edition/901jf2zptlxq"
BestBuyTest = "https://www.bestbuy.com/site/borderlands-3-standard-edition-xbox-one-digital/6346564.p?skuId=6346564"
BestBuyTest1 = "https://www.bestbuy.com/site/microsoft-xbox-series-s-512-gb-all-digital-console-disc-free-gaming-white/6430277.p?skuId=6430277"
BestBuyXboxSeriesX = "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324"
BestBuyXboxSeriesX_HaloEdition = "https://www.bestbuy.com/site/microsoft-xbox-series-x-halo-infinite-limited-edition-black/6477938.p?skuId=6477938"
TargetTest = "https://www.target.com/p/grand-theft-auto-v-premium-edition-playstation-4/-/A-53711597#lnk=sametab"
TargetXboxSeriesX = "https://www.target.com/p/xbox-series-x-console/-/A-80790841"
TargetXboxSeriesX_HaloEdition = "https://www.target.com/p/xbox-series-x-halo-infinite-limited-edition-bundle/-/A-84169784?sharedid=s16300536704476n0za53055"
GameStopTest = "https://www.gamestop.com/consoles-hardware/xbox-series-x%7Cs/gaming-accessories/controllers/products/microsoft-xbox-series-x-wireless-controller-carbon-black/11108954.html?condition=Pre-Owned"
GameStopXboxSeriesX = "https://www.gamestop.com/consoles-hardware/xbox-series-x%7Cs/consoles/products/xbox-series-x/B224744V.html"
GameStopHaloEliteController = "https://www.gamestop.com/gaming-accessories/controllers/xbox-series-x%7Cs/products/microsoft-xbox-elite-series-2-wireless-controller-for-xbox-series-x-halo-infinite/11157418.html?condition=New"

TARGET_SERIESX_INSTOCK = False
TARGET_HALO_INSTOCK = False

def send_email(body, subject):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(receivers)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(sender, receivers, msg.as_string())
        print("Email sent")
    except:
        print("Failed to send email")
    finally:
        server.close()


def setUp():
    PATH = "/Users/edwardcordero/Downloads/chromedriver"
    # code to use chrome with python anywhere
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    chrome_options = Options()
    chrome_options.add_argument('user-agent={user_agent}')
    chrome_options.add_argument('window-size=1200x1040')
    chrome_options.headless = True
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(PATH, options=chrome_options)
    return driver


def target_seriesx(driver):
    global TARGET_SERIESX_INSTOCK
    body = "Target has xbox series x in stock <a href=" + TargetXboxSeriesX + "> link to Target </a>"
    subject = "Target xbox series x stock-drops"
    driver.get(TargetTest)
    driver.implicitly_wait(30)
    try:
        driver.find_element_by_xpath("//*[@id='viewport']/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[2]/button")
        print("target has series x")
        # send_email(body, subject)
    except NoSuchElementException:
        return


def target_halo_seriesx(driver):
    global TARGET_HALO_INSTOCK
    body = "Target has halo xbox series x in stock <a href=" + TargetXboxSeriesX_HaloEdition + "> link to Target </a>"
    subject = "Target xbox Halo series x stock-drops"
    driver.get(test)
    driver.implicitly_wait(30)
    target_fulfillment_container = driver.find_elements_by_xpath('//*[@data-test="PDPFulfillmentSection"]/div/div')
    print(len(target_fulfillment_container))
    # iterates through each btn container
    for x in range(len(target_fulfillment_container)):
        print (x)
        child_num = x + 1
        # check btn for first child, since it has an extra div add it to the xpath
        if x < 1:
            print('running if')
            print (child_num)
            # //*[@data-test="PDPFulfillmentSection"]/div/div[1]/div/div/div[2]/button "child 1"
            btn_xpath = '//*[@data-test="PDPFulfillmentSection"]/div/div["%s"]/div/div/div[2]/button' %child_num
            target_btn = driver.find_elements_by_xpath(btn_xpath)
            print(len(target_btn))
            if len(target_btn) <= 0:
                # btn_xpath = '//*[@data-test="PDPFulfillmentSection"]/div/div["%s"]/div/div[2]/button' % child_num
                # target_btn = driver.find_elements_by_xpath(btn_xpath)
                # print(target_btn[0].text)
                print('null')
            else:
                print(target_btn[0].text)
        else:
            print('running else')
            print (child_num)
            # // *[ @ data - test = "PDPFulfillmentSection"] / div / div[2 or 3] / div / div[2] / button  "child 2-3"
            btn_xpath = '//*[@data-test="PDPFulfillmentSection"]/div/div["%s"]/div/div[2]/button' %child_num
            target_btn = driver.find_elements_by_xpath(btn_xpath)
            print(len(target_btn))
            print(target_btn[0].text)

    # try:
    #     driver.find_element_by_xpath("//*[@id='viewport']/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[2]/button")
    #     print("target has halo series x")
    #     # send_email(body, subject)
    # except NoSuchElementException:
    #     return


def bestbuy_seriesx(driver):
    body = "Best Buy has xbox series x in stock <a href=" + BestBuyXboxSeriesX + "> link to BestBuy </a>"
    subject = "Best Buy xbox series x stock-drops"
    driver.get(BestBuyXboxSeriesX)
    driver.implicitly_wait(30)
    best_btn = driver.find_element_by_xpath('//*[@class="fulfillment-add-to-cart-button"]/div/div/button')
    print(best_btn.text)
    if best_btn.text != 'Coming Soon' and best_btn.text != 'Sold Out':
        print('in stock, sending notifications')
        #     send_email(body, subject)
    else:
        print('out of stock')


def bestbuy_halo_seriesx(driver):
    body = "Best Buy has Halo Edition xbox series x in stock <a href=" + BestBuyXboxSeriesX_HaloEdition + "> link to BestBuy </a>"
    subject = "Best Buy Halo Edition xbox series x stock-drops"
    driver.get(BestBuyXboxSeriesX_HaloEdition)
    driver.implicitly_wait(30)
    best_btn = driver.find_element_by_xpath('//*[@class="fulfillment-add-to-cart-button"]/div/div/button')
    print(best_btn.text)
    if best_btn.text != 'Coming Soon' and best_btn.text != 'Sold Out':
        print('in stock, sending notifications')
        #     send_email(body, subject)
    else:
        print('out of stock')

def gamestop_seriesx(driver):
    body = "GameStop has xbox series x in stock <a href=" + GameStopXboxSeriesX + "> link to GameStop </a>"
    subject = "GameStop xbox series x stock-drops"
    driver.get(GameStopXboxSeriesX)
    driver.implicitly_wait(30)
    gamestop_btn = driver.find_element_by_xpath('//*[@id="add-to-cart-buttons"]/div/div/button')
    print(gamestop_btn.text)
    # text for out of stock = "NOT AVAILABLE"
    if gamestop_btn.text == "NOT AVAILABLE":
        print('out of stock')
    # text for in stock = "ADD TO CART"
    else:
        print('in stock, send notifications')
        # send_email(body, subject)


def gamestop_halocontroller(driver):
    body = "GameStop has Halo Elite controllers <a href=" + GameStopHaloEliteController + "> link to GameStop </a>"
    subject = "GameStop Halo Elite Controllers"
    driver.get(GameStopHaloEliteController)
    driver.implicitly_wait(30)
    gamestop_btn = driver.find_element_by_xpath('//*[@id="add-to-cart-buttons"]/div/div/button')
    print(gamestop_btn.text)
    # text for out of stock = "NOT AVAILABLE"
    if gamestop_btn.text == "NOT AVAILABLE":
        print('out of stock')
    # text for in stock = "ADD TO CART"
    else:
        print('in stock, send notifications')
        # send_email(body, subject)


def microsoft_halocontroller(driver):
    body = "Microsoft has Halo xbox elite controllers in stock <a href=" + MicrosoftXboxEliteController + "> link to Microsoft </a>"
    subject = "Microsoft Halo xbox elite controller"
    driver.get(MicrosoftXboxEliteController)
    driver.implicitly_wait(30)
    micro_btn = driver.find_element_by_xpath('//*[@class="pi-button-panel"]/div/div[2]/button/span')
    print(micro_btn.text)
    if micro_btn.text == 'Out of stock':
        print('product is out of stock')
    else:
        print('in stock, sending notifications')
        # send_email(body, subject)


def main():
    driver = setUp()
    # target_seriesx(driver)
    # target_halo_seriesx(driver)
    bestbuy_seriesx(driver)
    # bestbuy_halo_seriesx(driver)
    # gamestop_seriesx(driver)
    # gamestop_halocontroller(driver)
    microsoft_halocontroller(driver)
    # Clean up
    driver.quit()


if __name__ == "__main__":
    main()
