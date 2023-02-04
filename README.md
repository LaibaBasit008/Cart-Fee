# Cart-Fee

## Technology Stack
* Python
* Flask (Python web framework)
* Swagger


## Description
Implemented HTTP API in python using flask. It calculates the delivery fee in `cents` such that
``100 cents = 1€``and distance in meters such that `1000 meters = 1km`. Followed Controller service approach. ``app.py`` contains route and ``delivery.py`` contains function that calculates delivery fee. Errors have also been handled in which 
400, 401, 404 and 500 are handled. Logs were also added which can be viewed on the console. Request payload is in JSON and calculated delivery fee in the response payload is also in JSON format.

### Specification
Following rules are followed while calculating delivery fee
* If the cart value is less than 10€ / 1000 cents, a small order surcharge is added to the delivery price. The surcharge is the difference between the cart value and 10€ / 1000 cents. For example if the cart value is 8.90€/ 89 cents, the surcharge will be 1.10€ / 11 cents.
* A delivery fee for the first 1000 meters (=1km) is 2€ / 200 cents. If the delivery distance is longer than that, 1€/100 cents is added for every additional 500 meters that the courier needs to travel before reaching the destination. Even if the distance would be shorter than 500 meters, the minimum fee is always 1€/100 cents.
  * Example 1: If the delivery distance is 1499 meters, the delivery fee is: 2€ / 200 cents base fee + 1€ / 100 cents for the additional 500 m => 3€ /300 cents
  * Example 2: If the delivery distance is 1500 meters, the delivery fee is: 2€ / 200 cents base fee + 1€ / 100 cents for the additional 500 m => 3€ /300 cents
  * Example 3: If the delivery distance is 1501 meters, the delivery fee is: 2€ / 200 cents base fee + 1€ / 200 cents for the first 500 m + 1€/100 cents for the second 500 m => 4€ / 400 cents
* If the number of items is five or more, an additional 50 cent surcharge is added for each item above and including the fifth item. An extra "bulk" fee applies for more than 12 items of 1,20€/12000 cents
  * Example 1: If the number of items is 4, no extra surcharge
  * Example 2: If the number of items is 5, 50 cents surcharge is added
  * Example 3: If the number of items is 10, 3€/300 cents surcharge (6 x 50 cents) is added
  * Example 4: If the number of items is 13, 5,70€/570000 surcharge is added ((9 * 50 cents) + 1,20€/12000 cents)
* The delivery fee can __never__ be more than 15€/150 cents, including possible surcharges.
* The delivery is free (0€/0 cents) when the cart value is equal or more than 100€/10000. 
* During the Friday rush (3 - 7 PM UTC), the delivery fee (the total fee including possible surcharges) will be multiplied by 1.2x. However, the fee still cannot be more than the max (15€/1500).

#### Note
**When delivery fee is greater than 150 cents/ 15€ the deliver fee will be 150 cents/ 15€ and ) when cart value is greater than 10€ / 10000 cents.**

## How to execute code

### Using Build
* Go to  `dist` folder and double click on `app.py`
* Go to your browser and hit following link
`` http://127.0.0.1:5000/swagger ``
* Click on `try it out` and add values to the given variables and hit execute

### Command Line / Terminal
``pip install -r requirements.txt``


``python app.py``

Hit following link in the browser
`` http://127.0.0.1:5000/swagger ``

Click on `try it out` and add values to the given variables and hit execute

#### Note
**Postman can be used to test the api. For postman api will be ``http://127.0.0.1:5000/deliveryFee`` with `POST` option.**

### Result
#### Swagger
![image](https://user-images.githubusercontent.com/45163279/216773778-aa97e200-e9f2-4d17-9aab-49d9d616251c.png)

##### Logs
![image](https://user-images.githubusercontent.com/45163279/216773876-1ee31898-6d24-429a-a4fd-c9cff5f8aa57.png)

##### Error Handling
![image](https://user-images.githubusercontent.com/45163279/216773832-01c8ca99-68ea-409f-88ca-f255dc66f2a4.png)

#### Postman
![image](https://user-images.githubusercontent.com/45163279/216773683-48a272e1-f18d-4613-b1d8-f6cd2ff96571.png)

#### Given data Result / Example
![image](https://user-images.githubusercontent.com/45163279/216774726-315f0173-91ff-4d61-a582-afe926d48604.png)

#### JSON Payload
```json
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
```
