# old car = $2000

# new car = $8000

# can save $1000/month

# both cars depreciate 1.5% / month 

#depreciation increases by 0.5% after every 2 months.

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    my_car = startPriceOld
    my_money = 0
    savings = 0
    real_cost = startPriceNew
    depreciation = percentLossByMonth/100
    number_of_months = 0
    if startPriceOld >= startPriceNew:
        number_of_months = 0
        leftover = startPriceOld - startPriceNew
    else:
        while my_money < real_cost:
            number_of_months+=1
            if number_of_months > 1 and number_of_months % 2 == 0:
                depreciation+=0.005
            my_car -= my_car * depreciation
            real_cost -= real_cost * depreciation
            savings +=savingperMonth
            my_money = savings + my_car
            leftover = round(my_money - real_cost, 0)
    return [number_of_months, leftover]



print(nbMonths(2000, 8000, 1000, 1.5))
print(nbMonths(12000, 12000, 1000, 1.5))

def nbMonths(oldCarPrice, newCarPrice, saving, loss):
    months = 0
    budget = oldCarPrice
    
    while budget < newCarPrice:
        months += 1
        if months % 2 == 0:
            loss += 0.5
        
        oldCarPrice *= (100 - loss) / 100
        newCarPrice *= (100 - loss) / 100
        budget = saving * months + oldCarPrice
    
    return [months, round(budget - newCarPrice)]


