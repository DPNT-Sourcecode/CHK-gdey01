

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
    SKU_dict['C'] = SKUPriceMap(20, {})
    SKU_dict['D'] = SKUPriceMap(15, {})
    SKU_dict['E'] = SKUPriceMap(40, {
                        2: 'B'
                    })
    SKU_dict['F'] = SKUPriceMap(10, {
                        3: 20
                    })
    SKU_dict['G'] = SKUPriceMap(20, {})
    SKU_dict['H'] = SKUPriceMap(10, {
                        5: 45,
                        10: 80
                    })
    SKU_dict['I'] = SKUPriceMap(35, {})
    SKU_dict['J'] = SKUPriceMap(60, {})
    SKU_dict['K'] = SKUPriceMap(80, {
                        2: 150
                    })
    SKU_dict['L'] = SKUPriceMap(90, {})
    SKU_dict['M'] = SKUPriceMap(15, {})
    SKU_dict['N'] = SKUPriceMap(40, {
                        3: 'M'
                    })
    SKU_dict['O'] = SKUPriceMap(10, {})
    SKU_dict['P'] = SKUPriceMap(50, {
                        5: 200
                    })
    SKU_dict['Q'] = SKUPriceMap(30, {
                        3: 80
                    })
    SKU_dict['R'] = SKUPriceMap(50, {
                        3: 'Q'
                    })
    SKU_dict['S'] = SKUPriceMap(30, {})
    SKU_dict['T'] = SKUPriceMap(20, {})
    SKU_dict['U'] = SKUPriceMap(40, {
                        4: 120
                    })
    SKU_dict['V'] = SKUPriceMap(50, {
                        2: 90,
                        3: 130
                    })
    SKU_dict['W'] = SKUPriceMap(20, {})
    SKU_dict['X'] = SKUPriceMap(90, {})
    SKU_dict['Y'] = SKUPriceMap(10, {})
    SKU_dict['Z'] = SKUPriceMap(50, {})
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

    
    Our price table and offers: 
    +------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    | F    | 10    | 2F get one F free      |
    +------+-------+------------------------+




    +------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    | F    | 10    | 2F get one F free      |
    | G    | 20    |                        |
    | H    | 10    | 5H for 45, 10H for 80  |
    | I    | 35    |                        |
    | J    | 60    |                        |
    | K    | 80    | 2K for 150             |
    | L    | 90    |                        |
    | M    | 15    |                        |
    | N    | 40    | 3N get one M free      |
    | O    | 10    |                        |
    | P    | 50    | 5P for 200             |
    | Q    | 30    | 3Q for 80              |
    | R    | 50    | 3R get one Q free      |
    | S    | 30    |                        |
    | T    | 20    |                        |
    | U    | 40    | 3U get one U free      |
    | V    | 50    | 2V for 90, 3V for 130  |
    | W    | 20    |                        |
    | X    | 90    |                        |
    | Y    | 10    |                        |
    | Z    | 50    |                        |
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

    # apply group offer

    applicable_items = [SKU_dict['S'], SKU_dict['T'], SKU_dict['X'], SKU_dict['Y'], SKU_dict['Z']]
    applicable_items.sort(key=lambda x: x.price, reverse=True)

    for item in applicable_items:
        pass

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
            count_dict[item] = 0
    
        total_cost += cost

    return total_cost


print(checkout("FFFFF"))
