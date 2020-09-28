# No 1
def letter_catalog(items, letter='A'):
    a = []
    for i in items:
        if i[0].upper() == letter:
            a.append(i)
            continue
    return a
    
print(letter_catalog(['Apple', 'Avocado', 'Banana', 'Blackberries', 'Blueberries', 'Cherries'], letter='A'))


# No 2
def counter_item(items):
    counter = {}
    for i in items:
        counter[i] = counter.get(i, 0)+1
    return counter
    
print(counter_item(['Apple','Apple','Apple','Blueberries','Blueberries','Blueberries']))


# No 3
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

fruit_price = dict(zip(fruits, prices))

def counter_item(items):
    counter = {}
    for i in items:
        counter[i] = counter.get(i, 0)+1
    return counter

def total_price(dcounter,fprice):
    total = 0
    for key, value in dcounter.items():
            value *= fprice[key]
            total += value
    return total

print(total_price(counter_item(chart),fruit_price))
    

# No 4
def counter_item(items):
    counter = {}
    for i in items:
        counter[i] = counter.get(i, 0)+1
    return counter

def total_price(dcounter,fprice):
    total = 0
    for key, value in dcounter.items():
            value *= fprice[key]
            total += value
    return total

def discounted_price(total, discount, minprice=100):
    if total >= minprice:
        total = (total - (total*discount/100))
        return total
    else:
        return total

print(discounted_price(total_price(counter_item(chart),fruit_price),10,minprice=100))


# No 5
def print_summary(items,fprice):

    minprice = 100
    count = {}
    price = 0

    for belanjaan in items:
        if belanjaan in count:
            count[belanjaan] += 1
        else:
            count[belanjaan] = 1

    for key, value in sorted(count.items()):
        print("{} {}".format(value, key),':',(value*fprice[key]))

    for item in items:
        item  = fprice[item]
        price += item 
    print("total :", price)
    
    if price >= minprice:
        price = (price - (price*10/100))
        print("discount price :", price)
    else:
        print("discount price :", price)
    
print_summary(chart,fruit_price)

    # alternatif
#     barang = counter_item(items)
#     total = total_price(barang,fprice)
#     diskon = discounted_price(total,10,minprice=100)
    

#     for k, v in sorted(barang.items()):
#         print("{} {}".format(v, k),':',(v*fprice[k]))

#     print("total :", total)

#     print("discount price :", diskon)

# print_summary(chart,fruit_price)


