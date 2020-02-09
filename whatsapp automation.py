from selenium import webdriver
import time
from pip._vendor.distlib.compat import raw_input
import sys


class ToSendMessage:
    def scheduled_message(self):
        msg = input('enter a message: ')
        count = int(input("no of times the messages to be sent: "))
        while True:
            set_time = raw_input("set the time when the message to be send in format HHMM:  ")
            t = time.localtime()
            current_time = time.strftime("%H%M", t)
            if set_time <= current_time:
                print("Time has expired! Try again")
            else:
                break
        print("your message will be sent in the alloted time")
        while True:
            t = time.localtime()
            current_time = time.strftime("%H%M", t)
            if set_time == current_time:
                break
        select2 = site.find_element_by_class_name('_13mgZ')
        select2.click()
        time.sleep(5)
        while count:
            select2.send_keys(msg.title())
            select3 = site.find_element_by_class_name('_3M-N-')
            select3.click()
            count = count - 1
        print("your message is sent successfully")
        site.close()
        sys.exit()

    def sendmessage(self):
        while True:
            msg = input('enter a message: ')
            count = int(input("no of times the messages to be sent: "))
            select2 = site.find_element_by_class_name('_13mgZ')
            select2.click()
            time.sleep(1)
            while count:
                select2.send_keys(msg.title())
                time.sleep(1)
                select3 = site.find_element_by_class_name('_3M-N-')
                select3.click()
                count = count - 1
            while True:
                data = input("do you want to send another message(Y/N): ")
                if data.lower() == 'y' or data.lower() == 'n':
                    break
                else:
                    print("enter valid input")
            if data.lower() == "n":
                break
            else:
                print("invalid input try again")


class ToAttachImage:
    def scheduled_sendimage(self):
        file_path = input("enter path of the file(image or video): ")
        while True:
            set_time = raw_input("set the time when the message to be send in format HHMM:  ")
            t = time.localtime()
            current_time = time.strftime("%H%M", t)
            if set_time <= current_time:
                print("Time has expired! Try again")
            else:
                break
        print("your image will be sent in the alloted time")
        while True:
            t = time.localtime()
            current_time = time.strftime("%H%M", t)
            if set_time == current_time:
                break
        site.find_element_by_xpath('//*[@title="Attach"]').click()
        time.sleep(2)
        select = site.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        select.send_keys(file_path)
        time.sleep(5)
        site.find_element_by_xpath('//span[@data-icon="send-light"]').click()
        print("your image is sent successfully")
        site.close()
        sys.exit()

    def sendimage(self):
        while True:
            file_path = input("enter path of the file(image or video): ")
            site.find_element_by_xpath('//*[@title="Attach"]').click()
            time.sleep(2)
            select = site.find_element_by_xpath(
                '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            select.send_keys(file_path)
            time.sleep(5)
            try:
                site.find_element_by_xpath('//span[@data-icon="send-light"]').click()
            except:
                print("something went wrong try again")
                continue
            while True:
                data = input("do you want to send another file (Y/N)")
                if data.lower() == 'y' or data.lower() == 'n':
                    break
                else:
                    print("enter valid input")
            if data.lower() == 'n':
                break


class ToSendDocument:
    def attachdocument(self):
        while True:
            file_path = input("enter path of the document: ")
            site.find_element_by_xpath('//*[@title="Attach"]').click()
            time.sleep(2)
            select = site.find_element_by_xpath('//input[@accept="*"]')
            select.send_keys(file_path)
            time.sleep(3)
            try:
                site.find_element_by_xpath('//span[@data-icon="send-light"]').click()
            except:
                print("Oops! something went wrong try again")
                continue
            while True:
                data = input("Do you want to send another document (y/n): ")
                if data.lower() == 'y' or data.lower() == 'n':
                    break
                else:
                    print("invalid input try again")
            if data.lower() == 'n':
                break


site = webdriver.Chrome()
site.get('https://web.whatsapp.com/')
site.maximize_window()
input("press enter after scanning qr code")
while True:
    choice = input(
        "To send message press 'm' \nTo send a photo or video press 'p' \nTo send any Document press 'f'\nTo exit press 'q': ")
    try:
        name = input("enter name of user: ")
        site.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
    except:
        print("user not found Try again")
        continue
    if choice.lower() == 'm':
        while True:
            decision = input("To send normal message press n: \nTo send scheduled message press s: ")
            if decision.lower() == 'n' or decision.lower() == 's':
                break
            else:
                print("invalid input try again")
        message = ToSendMessage()
        if decision.lower() == 'n':
            message.sendmessage()
        if decision.lower() == 's':
            message.scheduled_message()
    elif choice.lower() == 'p':
        while True:
            decision = input("To send normal message press n: \nTo send scheduled message press s: ")
            if decision.lower() == 'n' or decision.lower() == 's':
                break
            else:
                print("invalid input try again")
        image = ToAttachImage()
        if decision.lower() == 'n':
            image.sendimage()
        if decision.lower() == 's':
            image.scheduled_sendimage()
    elif choice.lower() == 'f':
        document = ToSendDocument()
        document.attachdocument()
    elif choice.lower() == 'q':
        break
    else:
        print("invalid input try again")
    time.sleep(5)
