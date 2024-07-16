

# noinspection PyUnusedLocal
# skus = unicode string

class SKUPriceMap:

    """
    item: String
    price: float/int
    special_offers: dict
    Keeps the item, the price and a dictionary to store special offers
    The dict keeps them in a qty: price format 
    """
    def __init__(self, price, special_offers):
        self.price = price
        self.special_offers = special_offers


def initialize_SKUs():
    SKU_dict = {}
    SKU_dict['A'] = SKUPriceMap(50, {3: 130})
    SKU_dict['B'] = SKUPriceMap(30, {2: 45})
    SKU_dict['C'] = SKUPriceMap(20, {})
    SKU_dict['D'] = SKUPriceMap(15, {})
    return SKU_dict

def parse_string(skus):
    pass

def checklite(skus):
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

     - param[0] = a String containing the SKUs of all the products in the basket
     Okay assuming it's a space separated string?! 3A 4B 2C kinda thing? 

    Ideally I'd like to keep the models separate - Use a separate one for special offers.
    If there was an actual db I think it makes much more sense to separate the models
    """
    SKU_dict = initialize_SKUs()
    pass


