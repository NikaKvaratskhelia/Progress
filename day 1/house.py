good_credit=True
bad_credit=False
price=1_000_000
if good_credit:
    down_payment= 0.1*price
else:
    down_payment=0.2*price
print("down_payment is:$"+ str(down_payment))