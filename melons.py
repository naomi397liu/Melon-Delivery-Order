"""Classes for melon orders."""
class AbstractMelonOrder():
    '''Abstract base class that other melon orders inherit from'''
    #init: include species, qty, shipped, order type, tax
    def __init__(self, species, qty, order_type, tax): #possibly input default values if domestic
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    #add another method to abstract parent: get_total and mark_shipped
    def get_total(self):
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total
    
    def mark_shipped(self):
        self.shipped = True
    #create 2 classes: domestic melon order and international melon order
        #create a super class for get country code - mixin
    #define methods here!
f, species, qty
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    #call methods!
    def __init__(sel):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
