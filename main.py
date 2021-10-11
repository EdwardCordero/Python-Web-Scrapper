import smtplib
import datetime
from emails import receivers
from email.mime.text import MIMEText

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

sender = "edwardcordero98.stockdrops@gmail.com"
user = 'edwardcordero98.stockalerts@gmail.com'
password = 'Uncannyedward98!'

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
    PATH = "/Users/edwardcordero/Selenium/chromedriver"
    # code to use chrome with python anywhere
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    chrome_options = Options()
    chrome_options.add_argument('user-agent={user_agent}')
    # chrome_options.headless = True
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(PATH, options=chrome_options)
    return driver


def target_seriesx(driver):
    global TARGET_SERIESX_INSTOCK
    body = "Target has xbox series x in stock <a href=" + TargetXboxSeriesX + "> link to Target </a>"
    subject = "Target xbox series x stock-drops"
    driver.get(TargetTest)
    driver.implicitly_wait(10)
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
    driver.get(TargetXboxSeriesX_HaloEdition)
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_xpath("//*[@id='viewport']/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[2]/button")
        print("target has halo series x")
        # send_email(body, subject)
    except NoSuchElementException:
        return


def bestbuy_seriesx(driver):
    body = "Best Buy has xbox series x in stock <a href=" + BestBuyXboxSeriesX + "> link to BestBuy </a>"
    subject = "Best Buy xbox series x stock-drops"
    driver.get(BestBuyXboxSeriesX)
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_xpath(".//div[contains(@id, 'fulfillment-add-to-cart-button')]")
        # send_email(body, subject)
    except NoSuchElementException:
        return


def bestbuy_halo_seriesx(driver):
    body = "Best Buy has Halo Edition xbox series x in stock <a href=" + BestBuyXboxSeriesX_HaloEdition + "> link to BestBuy </a>"
    subject = "Best Buy Halo Edition xbox series x stock-drops"
    driver.get(BestBuyXboxSeriesX_HaloEdition)
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_xpath(".//div[contains(@id, 'fulfillment-add-to-cart-button')]")
        send_email(body, subject)
    except NoSuchElementException:
        return


def gamestop_seriesx(driver):
    body = "GameStop has xbox series x in stock <a href=" + GameStopXboxSeriesX + "> link to GameStop </a>"
    subject = "GameStop xbox series x stock-drops"
    driver.get(GameStopXboxSeriesX)
    driver.implicitly_wait(10)
    try:
        addToCart = driver.find_element_by_id("add-to-cart")
        if addToCart.text == 'ADD TO CART':
            send_email(body, subject)
        else:
            return
    except NoSuchElementException:
        return


def gamestop_halocontroller(driver):
    body = "GameStop has Halo Elite controllers <a href=" + GameStopHaloEliteController + "> link to GameStop </a>"
    subject = "GameStop Halo Elite Controllers"
    driver.get(GameStopTest)
    driver.implicitly_wait(10)
    try:
        addToCart = driver.find_element_by_id("add-to-cart")
        if addToCart.text == 'ADD TO CART':
            send_email(body, subject)
            print("gamestop has control in stock", addToCart.text)
        else:
            print("out of stock", addToCart.text)
            return
    except NoSuchElementException:
        return


def microsoft_halocontroller(driver):
    body = "Microsoft has Halo xbox elite controllers in stock <a href=" + MicrosoftXboxEliteController + "> link to Microsoft </a>"
    subject = "Microsoft Halo xbox elite controller"
    driver.get(MicrosoftXboxEliteController)
    driver.implicitly_wait(60)
    try:
        microsoft_button = driver.find_element_by_xpath('//*[@id="buttons_AddToCartButton"]')
        print("In stock at microsoft", microsoft_button.text)
    except NoSuchElementException:
        # send_email(body, subject)
        print("Out of stock at microsoft")
        return


def main():
    # current_time = datetime.datetime.now()
    # in_stock_wait_min = 30
    # added_min = datetime.timedelta(minutes=in_stock_wait_min)
    # start_time = current_time + added_min

    driver = setUp()
    # target_seriesx(driver)
    # target_halo_seriesx(driver)
    # bestbuy_seriesx(driver)
    # bestbuy_halo_seriesx(driver)
    # gamestop_seriesx(driver)
    # gamestop_halocontroller(driver)
    microsoft_halocontroller(driver)
    # Clean up
    driver.quit()


if __name__ == "__main__":
    main()
