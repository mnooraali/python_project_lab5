import random
import webbrowser


# from selenium import webdriver


def showme():
    print("-----------------------We Choose For You --------------------------")

    links = ["https://www.google.com", "https://www.facebook.com", "https://www.gmail.com"]
    # show = random.sample(links, 1)

    webbrowser.open(random.choice(links))

    # # print(str(show))
    # tab = str(show)
    #
    # # webbrowser.open(tab, new=2)
    #
    # # webbrowser.open("https://www.google.com", new=2)
    #
    # path = 'C:/Users/HP/AppData/Local/Google/Chrome/Application/chrome.exe %s'
    # print(tab)
    # webbrowser.open(tab, new=1)
    # print("doneeeee")


showme()
