

# noinspection PyUnusedLocal
# skus = unicode string

class SKUPriceMap:

    """
    item: String
    price: float/int
    special_offers: SpecialOffers
    Keeps the item, the price and the special offers
    """
    def __init__(self, price, special_offers):
        self.price = price
        self.special_offers = special_offers


def initialize_SKUs():
    SKU_dict = {}
    SKU_dict['A'] = SKUPriceMap(50, {
                        3: 130,
                        5: 200
                    })
    SKU_dict['B'] = SKUPriceMap(30, {
                        2: 45
                    })
    SKU_dict['C'] = SKUPriceMap(20, [])
    SKU_dict['D'] = SKUPriceMap(15, [])
    SKU_dict['E'] = SKUPriceMap(15, {
                        2: 'B'
                    })
    return SKU_dict



def checkout(skus):
    """
    Our price table and offers: 
    +------+-------+----------------+
    | Item | Price | Special offers |
    +------+-------+----------------+
    | A    | 50    | 3A for 130     |
    | B    | 30    | 2B for 45      |
    | C    | 20    |                |
    | D    | 15    |                |
    +------+-------+----------------+

    Ideally I'd like to keep the models separate - Use a separate one for special offers.
    If there was an actual db I think it makes much more sense to separate the models

    - param[0] = a String containing the SKUs of all the products in the basket
     Okay assuming it's a space separated string?! 3A 4B 2C kinda thing? 
     I mean in fairness it kinda doesn't matter -
     how this string is formatted (or even if it is delimitted?)
     otherwise I think just splitting it and then using this makes much more sense

     Changed it up because it wasn't that haha


    +------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    +------+-------+------------------------+


    """
    SKU_dict = initialize_SKUs()
    total_cost = 0

    count_dict = {}

    if not set(skus).intersection(set(SKU_dict.keys())) == set(skus):
        return -1

    for item in SKU_dict.keys():
        count = skus.count(item)
        count_dict[item] = count

    for item, value in SKU_dict.items():

        if value.special_offers:
            # We kinda have to check the str ones first and adjust the quantities
            for offer_quantity in value.special_offers.keys():
                if isinstance(value.special_offers[offer_quantity], str):
                    if count_dict[item] > 0:
                        quotent = count_dict[item] // offer_quantity
                        count_dict[value.special_offers[offer_quantity]] -= 1 * quotent

    for item, value in SKU_dict.items():
        cost = 0
        if value.special_offers:
            # We should check if the num is a multiple of special offers
            key_list = list(value.special_offers.keys())
            key_list.sort(reverse = True)
            for offer_quantity in key_list:
                if isinstance(value.special_offers[offer_quantity], int):
                    if count_dict[item] > 0:
                        quotent = count_dict[item] // offer_quantity
                        cost += quotent * value.special_offers[offer_quantity]
                        count_dict[item] = count_dict[item] - quotent * offer_quantity
            if count_dict[item] > 0:
                cost += count_dict[item] * value.price

        else:
            if count_dict[item] > 0:
                cost = value.price * count_dict[item]
        
        total_cost += cost

    return total_cost


print(checkout("AAAAABBEE"))

