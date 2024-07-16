

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

class SpecialOffers:

    def __init__(self, qty, price):
        self.qty = qty
        self.price = price


def initialize_SKUs():
    SKU_dict = {}
    SKU_dict['A'] = SKUPriceMap(50, SpecialOffers(3, 130))
    SKU_dict['B'] = SKUPriceMap(30, SpecialOffers(2, 45))
    SKU_dict['C'] = SKUPriceMap(20, None)
    SKU_dict['D'] = SKUPriceMap(15, None)
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
    """
    SKU_dict = initialize_SKUs()
    total_cost = 0


    for item, value in SKU_dict.items():

        if item in skus:
            count = skus.count(item)
            skus = skus.replace(item, '')
            if value.special_offers:
                # We should check if the num is a multiple of special offers
                quotent = count // value.special_offers.qty
                remainder = count % value.special_offers.qty

                cost = quotent * value.special_offers.price + remainder * value.price
                
            else:
                cost = value.price * count
            
            total_cost += cost

    if skus:
        return -1

    return total_cost

