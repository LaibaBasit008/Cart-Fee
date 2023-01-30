import datetime
import calendar
import logging


def deliveryFee(cartValue,deliveryDistance,noOfItems,time):
    logger = logging.getLogger()
    surCharge=0
    chargePerDistance=0
    itemSurCharge=0
    if(cartValue<1000):
        surCharge=1000-cartValue
        print("Calculating Surcharge on cart value")
        
    elif(cartValue>=1000):
        return 0
    if(deliveryDistance==1000):
        chargePerDistance=200  

    if(deliveryDistance>1000):
        RemaningDistance=deliveryDistance-1000
        count=int(RemaningDistance/500)
        counterCheck=RemaningDistance-500 
        if(counterCheck!=0):
            count+=1
        chargePerDistance=2+count
        chargePerDistance=chargePerDistance*100
    if(noOfItems<=4):
        itemSurCharge=0
    elif(noOfItems==5):
        itemSurCharge=.5
    elif(noOfItems>5):
        item=noOfItems-4
        if(noOfItems<12):
            itemSurCharge=item*.5
        else:
            itemSurCharge=((item*50)+120)
    dateAndTime=time.split("T")
    day=dayOfTheWeek(dateAndTime[0])
    if(day=="Friday"):
        timeAtOrder=dateAndTime[1].split(":")
        if(timeAtOrder[1]>15 and timeAtOrder[1]<19):
            deliveryFee=(surCharge+chargePerDistance+itemSurCharge)*1.2
            return deliveryFee

    deliveryFee=surCharge+chargePerDistance+itemSurCharge
    if(deliveryFee>1500):
        return 150
    return deliveryFee

def dayOfTheWeek(dateAndTime):
    dateArr=dateAndTime.split("-")
    date=dateArr[2]+" "+dateArr[1]+" "+dateArr[0]
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[day])