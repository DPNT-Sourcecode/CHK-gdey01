

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

    Ideally I'd like to keep the models separate - Use a separate one for special offers.
    If there was an actual db I think it makes much more sense to separate the models

    - param[0] = a String containing the SKUs of all the products in the basket
     Okay assuming it's a space separated string?! 3A 4B 2C kinda thing? 
     I mean in fairness it kinda doesn't matter -
     how this string is formatted (or even if it is delimitted?)
     otherwise I think just splitting it and then using this makes much more sense

     Now I'm thinking what if the the qty is a float? (Realistically it makes no sense)
    """
    SKU_dict = initialize_SKUs()

    stack = []
    for item in skus:
        if item.isnum():
            stack.append(item)
        elif item.isalpha():
            if item not in SKU_dict.keys():
                # The item is invalid
                return -1
            else:
                # It's a Valid item
                if len(stack) > 0:
                    # The stack is valid?
                    str_num = ''.join(stack)


    pass





