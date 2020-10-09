"""Classes for melon orders."""
class AbstractMelonOrder():
    '''Abstract base class that other melon orders inherit from'''
    #init: include species, qty, shipped, order type, tax
    country_code = None
    def __init__(self, species, qty, order_type, tax=0.08): #possibly input default values if domestic
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    #add another method to abstract parent: get_total and mark_shipped
    def get_total(self):
        base_price = 5
        flat_fee = 0
        if self.species == "Christmas Melon":
            base_price = base_price * 1.5
        if self.order_type == "International" and self.qty < 10:
            flat_fee = 3
        total = (1 + self.tax) * self.qty * base_price + flat_fee
        return total
    
    def mark_shipped(self):
        self.shipped = True
    

    #create 2 classes: domestic melon order and international melon order
        #create a super class for get country code - mixin
    #define methods here!

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    #call methods!
    # def __init__(self, pspecies, pqty, ptax=0.08): #tax, shipped, order_type? because it is defined within init and not passed in?
    #     """Initialize melon order attributes."""
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

        #use super in the init to add country code
        #add country code to init?
    def __init__(self, pspecies, pqty, porder_type, pcountry_code, ptax=0.17): #unsure if this is correct to add instances
        super().__init__(pspecies, pqty, porder_type, ptax) #calls the init from abstract melon order
        self.country_code = pcountry_code

    def get_country_code(self):

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, pspecies, pqty, porder_type, ptax=0):
        super().__init__(pspecies, pqty, porder_type, ptax)
        self.ppassed = False
  
    def get_mark_inspection(self):
        self.ppassed = True

Government = GovernmentMelonOrder('Christmas Melon', 5, 'Domestic')
print(Government.get_mark_inspection())