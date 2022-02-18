weight = 2

def cost_calculator(weight, price, flat_rate = 20):
    cost = weight * price + flat_rate
    return cost

# ground shipping
def ground_price(weight):
    if weight <= 2:
        return(cost_calculator(weight, 1.5))
    elif 2 < weight <= 6:
        return(cost_calculator(weight, 3))
    elif 6 < weight <= 10:
        return(cost_calculator(weight, 4))
    elif weight > 10:
        return(cost_calculator(weight, 4.75))


premium_ground_flatrate= 125
def premium_ground_price(weight):
    return((weight * 0) + premium_ground_flatrate)

#
            #drone shipping
def drone_price(weight):
    if weight <= 2:
        return(cost_calculator(weight, 4.5, 0))
    elif 2 < weight <= 6:
        return(cost_calculator(weight, 9, 0))
    elif 6 < weight <= 10:
        return(cost_calculator(weight, 12, 0))
    elif weight > 10:
        return(cost_calculator(weight, 14.25, 0))

if ground_price(weight) < premium_ground_price(weight) and ground_price(weight) < drone_price(weight):
    print("Howdy! your best option is ground delivery and your price is $" + str(ground_price(weight)))
elif premium_ground_price(weight) < ground_price(weight) and premium_ground_price(weight) < drone_price(weight):
    print("Howdy! your best option is premium ground delivery and your price is $" + str(premium_ground_price(weight)))
elif drone_price(weight) < ground_price(weight) and drone_price(weight) < premium_ground_price(weight):
    print("Howdy! your best option is drone delivery and your price is $" + str(drone_price(weight)))