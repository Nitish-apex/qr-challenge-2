#prices of items
prices = {'apple': 10, 'tomato':5, 'banana': 1, 'potato':5}

#items purchased
my_purchase = {
    'apple': 1,
    'banana': 6,
    'potato': 5
}

grocery_bill = 0

for purchase in my_purchase:
	grocery_bill += my_purchase[purchase] * prices[purchase]

#total bill
print ('I owe the grocer %.2f rupees' % grocery_bill)
