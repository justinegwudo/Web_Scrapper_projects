import requests
from bs4 import BeautifulSoup
import smtplib
import time

print("This application will let you know when iphone 11 pro 256 is less that N500,000")
email = input("What email do you want this sent to?: ")


def check_price():
    try:
        URL = "https://www.jumia.com.ng/iphone-11-pro-max-6.5-inch-super-retina-xdr-oled-4gb-ram-256gb-romios-13-12mp12mp12mp12mp-4g-lte-smartphone-silver-apple-mpg1204784.html"

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, "html.parser")
        title = soup.find(class_="-fs20 -pts -pbxs").get_text()
        price = soup.find(class_="-b -ltr -tal -fs24").get_text()
        converted_price = (price.replace("₦ ", ""))
        converted_price2 = int(converted_price.replace(",", ""))

        if converted_price2 < 500000:
            send_mail()

        print(title)
        print(converted_price2)



    except AttributeError:
        print(":( product is no longer available")


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("sender's email", password=)

    subject = "You can now afford it!"
    body = "Check the jumia link https://www.jumia.com.ng/iphone-11-pro-max-6.5-inch-super-retina-xdr-oled-4gb-ram-256gb-romios-13-12mp12mp12mp12mp-4g-lte-smartphone-silver-apple-mpg1204784.html"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        email,
        msg

    )

    print("Hey, email has been sent!")

    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60 * 60)
