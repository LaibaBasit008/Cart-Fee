
from flask import *
import json, time
from deliveryfee import deliveryFee
app = Flask(__name__)
@app.route('/')
@app.route('/user',methods=['GET'])
def calculateDeliveryFee():
   
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json
        cartValue=data.get('cart_value')
        deliveryDistance=data.get('delivery_distance')
        noOfItems=data.get('number_of_items')
        time=data.get('time')
        deliveryCost=deliveryFee(cartValue,deliveryDistance,noOfItems,time)
    return {"delivery_fee":deliveryCost}
    
if __name__ =='__main__':
    app.run()
    