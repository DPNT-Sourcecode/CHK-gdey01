

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
    total_cost = 0
    for item in skus:
        if item.isnum():
            stack.append(item)
        elif item.isalpha():
            if item not in SKU_dict.keys():
                # The item is invalid
                return -1
            else:
                # It's a Valid item
                cost = 0
                if len(stack) > 0:
                    # The stack is valid?
                    str_num = ''.join(stack)
                else:
                    # Maybe it's just qty =1 
                    str_num = 1

                sku = SKU_dict[item]
                if sku.special_offers:
                    # We should check if the num is a multiple of special offers
                    quotent = int(str_num) // sku.special_offers.qty
                    remainder = int(str_num) % sku.special_offers.qty

                    cost = quotent * sku.special_offers.price + remainder * sku.price
                    
                else:
                    cost = sku.price * int(str_num)
                
                total_cost += cost
                
        else:
            # dunno if we should return -1 here? depending on the delim it might be invalid
            pass

    return total_cost

