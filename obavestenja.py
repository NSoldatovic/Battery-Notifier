import psutil
import time
import json
import ctypes
from notifypy import Notify


def main_app():
    notification = Notify(


        default_notification_title="Battery Notification",
        default_notification_application_name="Battery Notifier",
        default_notification_audio="zvuk.wav"
    )
    with open("config.json", "r") as jsonFile:
        config = json.load(jsonFile)
        #print(config)
    min=config["min"]
    max=config["max"]

    if int(min)<2 or int(max)>100 or int(min)>int(max):
        ctypes.windll.user32.MessageBoxW(0, u"Uneli ste pogrešan min/max!!!", u"Error", 0)
        quit()
    def obavestenje(string,procenat,ikonica):
        notification.title=string
        notification.icon=ikonica
        notification.message=("Battery is" + ' '+procenat+'%')
        notification.send()

    #baterija=psutil.sensors_battery()

    #print(baterija)
    #testiranje
    while True:
        #print("radi")
        baterija=psutil.sensors_battery()
        #print(baterija)
        #obavestenje('Aloo',str(69))
        if baterija.power_plugged:
            if baterija.percent >= int(max):
                obavestenje(config["unplug"], str(baterija.percent),"max_icon.png")
                #print('vece od maxa')
        else:
            if baterija.percent <= int(min):
                obavestenje(config["plug"], str(baterija.percent),"min_icon.png")
                #print('manje od min')

        time.sleep(int(config['vreme']))
#main_app()