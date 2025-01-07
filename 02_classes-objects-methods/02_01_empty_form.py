# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.
<<<<<<< HEAD
class Ingredient:
    """Models an Ingredient. Currently not only carrots!"""

    def __init__(self, name):
        self.name = name
        self.expired = False

    def expire(self):
        self.expired = True

    

c = Ingredient('carrot')
print(c.name)  # OUTPUT: carrot
o = Ingredient('onion')
print(o.name)
print(o.name, 'expired: ', o.expired)
o.expire()
print(o.name, 'expired: ', o.expired)
=======
class Patient:
    """this is a patient class"""
    def __init__(self, name):
        self.name = name
    
p1 = Patient('Lucy')
p2 = Patient('Mark')


print(p1.name, p2.name)

class Ingredient:


    """Models a food item used as an ingredient."""
    def __init__(self, name):
        self.name = name
        self.amount = 1
        self.url = 'https://en.wikipedia.org/wiki/Carrot'

    def expire(self):
        """Expires the ingredients."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def unexpire(self):
        """Unexpires the ingredient. """    
        print(f"Your product '{self.name}', is still fine")
        self.name = self.name[8:]

    def get_info(self):
        import webbrowser as wb
        url = 'https://en.wikipedia.org/wiki/' + self.name
        wb.open_new(url) 


    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"

i = Ingredient('peas')
c = Ingredient('carrot')
p = Ingredient('potato')
print(i)
i.expire()
print(i)
i.unexpire()
print(i)
print(repr(i))
print(str(i))
print(i.get_info())
print(c.get_info())
print(p.get_info())
>>>>>>> 72e4a576347b28644688645dc86b5f38fd14246c
