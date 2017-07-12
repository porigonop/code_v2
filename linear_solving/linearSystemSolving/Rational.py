def gcd(integer_1, integer_2):
    """
    Return the value of the gcd between the integer: integer1 and integer2
    """
    integer_1, integer_2 = abs(integer_1), abs(integer_2)
    while integer_1 % integer_2 != 0 : 
        integer_1, integer_2 = integer_2, integer_1 % integer_2 
    return integer_2

class Rational:
    """
    Class representative a rational number with a numerator and a denominator
    """
    def __init__(self, numerator, denominator = 1):

        self.numerator = int(numerator)
        self.denominator = int(denominator)
        self.simplify()
    def multiply (self, rational2):
        """
        Multiply the current rational with another and return the result
        """

        num = self.numerator * rational2.numerator
        den = self.denominator * rational2.denominator

        result = Rational(num, den)
        result.simplify()

        return result

    def opposite(self):
        """
        Return opposite of this rational
        """

        return Rational(- self.numerator,  self.denominator)

    def add(self, rational2):
        """
        Add the current rational with another and return the result
        """

        num = self.numerator * rational2.denominator +\
              rational2.numerator * self.denominator

        den = self.denominator * rational2.denominator

        result = Rational(num, den)
        result.simplify()

        return result

    def substract(self, rational2):
        return self.add(rational2.opposite())

    def reverse(self):
        """
        Return the reverse value of the current rational
        """

        return Rational(self.denominator, self.numerator)

    def divided(self, rational2):
        """
        Divided the current rational by another
        """

        result = self.multiply(rational2.reverse())
        result.simplify()
        return result

    def simplify(self):
        """
        Simplify the current rational
        """

        if self.numerator == 0:
            self.denominator = 1
        if self.numerator < 0 and self.denominator < 0:
            self.numerator, self.denominator  = -self.numerator, -self.denominator
        else:
            gcd_simple = gcd(self.numerator, self.denominator)

            self.numerator //= gcd_simple
            self.denominator //= gcd_simple

    def __repr__(self):

        return str(round(self.numerator/self.denominator, 2))
        
    def __add__(self, rational): # +
        return self.add(rational)

    def __sub__(self, rational): #-
        return self.substract(rational)

    def __mul__(self, rational): # *
        return self.multiply(rational)

    def __truediv__(self, rational): # /
        return self.divided(rational)

    def __iadd__(self, rational): # +=
        return self.add(rational)
        
    def __ne__(self, rational): # !=
        if self.numerator != rational.numerator or \
        self.denominator != rational.denominator:
            return True
        return False

        

        

if __name__ == "__main__":

    assert(gcd(1, 5) == 1)
    assert(gcd(5, 10) == 5)
    assert(gcd(37, 7) == 1)

    a = Rational(2, 3)
    b = Rational(5, 3)
    c = Rational(7, 3)
    d = Rational(3, 3)
    e = Rational(4, 13)
    
    a = Rational(-720, -180)
    print(a)

    
        

        
    
        

    
        
