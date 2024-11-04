weight = input("Enter the weight")

# case1: ground shipping
weight = float(weight)
flat_charge = 20.00
if weight <= 2.0:
    price_per_pound = 1.50
    ground_shipping = flat_charge + (weight * price_per_pound)

elif weight > 2.00 and weight <= 6.00:
    price_per_pound = 3.00
    ground_shipping = flat_charge + (weight * price_per_pound)
elif weight > 6.00 and weight <= 10.00:
    price_per_pound = 4.00
    ground_shipping = flat_charge + (weight * price_per_pound)
else:
    price_per_pound = 4.75
    ground_shipping = flat_charge + (weight * price_per_pound)

    print("Cost of shipping through ground", ground_shipping)

# case2: ground shipping premium

ground_shipping_premium = 125.00
print("Cost of shipping through ground premium", ground_shipping_premium)

# case3: drone shipping

if weight <= 2.0:
    price_per_pound = 4.50
    drone_shipping = weight * price_per_pound
elif weight > 2.00 and weight <= 6.00:
    price_per_pound = 9.00
    drone_shipping = weight * price_per_pound
elif weight > 6.00 and weight <= 10.00:
    price_per_pound = 12.00
    drone_shipping = weight * price_per_pound
else:
    price_per_pound = 14.25
    drone_shipping = weight * price_per_pound

print("Cost of shipping through drone", drone_shipping)

