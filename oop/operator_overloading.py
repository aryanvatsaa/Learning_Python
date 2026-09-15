# OPERATOR OVERLOADING : - WITH OPERATOR OVERLOADING, WE CAN DEFINE HOW OPERATORS (LIKE +,-, *, /) WORK WITH OBJECTS OF A CLASS. WE CAN PROVIDE OUR OWN DEFINITIONS. 

# EXAMPLE 1:- WAP TO ADD TWO COMPLEX NUMBERS USING OPERATOR OVERLOADING.

# class Complex:
#     def __init__(self):
#         self.real = 0
#         self.img = 0
#     def setValue(self, real, img):
#         self.real = real
#         self.img = img
#     def __add__(self, other):                            # Overloading the + operator
#         Temp = Complex()
#         Temp.real = self.real + other.real
#         Temp.img = self.img + other.img
#         return Temp
#     def display(self):
#         print("( ", self.real, "j " " + ", self.img, "i" " )")
# other1 = Complex()
# other1.setValue(1,2)
# other2 = Complex()
# other2.setValue(3,4)
# other3 = Complex()
# other3 = other1 + other2
# print("SUM = ")
# other3.display()

#Q1. WAP TO COMPARE TWO DATE OBJECTS.

# class Date:
#     def __init__(self):
#         d = m = y = 0
#     def get(self):
#         self.d = int(input("Enter the day : "))
#         self.m = int(input("Enter the month : "))
#         self.y = int(input("Enter the year : "))
#     def __eq__(self, D):
#         flag = False
#         if self.d == D.d:
#             if self.m == D.m:
#                 if self.d == D.y:
#                     flag = True
#         return flag
#     def __lt__(self, D):
#         flag = False
#         if self.y < D.y:
#             if self.m < D.m:
#                 if self.d < D.d:
#                     flag = True
#         return flag
# D1 = Date()
# D1.get()
# D2 = Date()
# D2.get()
# print("D1 == D2", D1 == D2)
# print("D1 < D2", D1 < D2)

#Q2. WAP TO OVERLOAD THE -= OPERATOR TO SUBTRACT TWO DISTANCE OBJECTS.

# class Distance:
#     def __init__(self):
#         self.km = 0
#         self.m = 0
#     def set(self, km , m):
#         self.km = km
#         self.m = m
#     def __isub__(self, D):                                    # Overloading the - operator
#         self.m = self.m - D.m
#         if self.m < 0:
#             self.m += 1000
#             self.km -= 1
#         self.km = self.km - D.km
#         return self
#     def convert_to_meters(self):
#         return (self.km*1000 + self.m)
#     def display(self):
#         print(self.km, "kms", self.m, "mtrs")

# D1 = Distance()
# D1.set(21, 70)
# D2 = Distance()
# D2.set(18, 123)
# D1 -= D2
# print("D1 - D2 :- ")
# D1.display(),
# print("that is ", D1.convert_to_meters(), "meters")

#Q3. WAP THAT OVERLOADS THE *, / AND > OPERATORS SO THAT IT CAN MULTIPLY, DIVIDE AND COMPARE TWO OBJECTS OF CLASS FRACTION.

import math
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        
        gcd = math.gcd(numerator, denominator)          #simplify
        self.num = numerator // gcd
        self.den = denominator // gcd
        
        if self.den < 0:
            self.num = -self.num
            self.den = -self.den

    def __mul__(self, other):                  # Overloading the * operator
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __truediv__(self, other):                 # Overloading the / operator
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by a fraction equal to zero.")
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __gt__(self, other):                             # Overloading the > operator      
        # Compare cross-multiplied values to avoid floating-point issues
        return self.num * other.den > other.num * self.den

    def __str__(self):                         # String representation for clean output
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

def get_fraction_input(prompt):                    # valid fraction input from the user
    print(prompt)
    num = int(input("  Enter numerator: "))
    den = int(input("  Enter denominator: "))
    return Fraction(num, den)

if __name__ == "__main__":                   # Main Execution
    print("--- Fraction Operator Overloading ---")
    try:
        # Taking inputs
        f1 = get_fraction_input("\nFor Fraction 1:")
        f2 = get_fraction_input("\nFor Fraction 2:")

        print(f"\nFraction 1: {f1}")
        print(f"Fraction 2: {f2}")

        result_mul = f1 * f2                         
        result_div = f1 / f2
        is_greater = f1 > f2

        print("\n--- Results ---")                             
        print(f"Multiplication ({f1} * {f2}) = {result_mul}")
        print(f"Division ({f1} / {f2})       = {result_div}")
        print(f"Is Fraction 1 > Fraction 2?   = {is_greater}")

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")