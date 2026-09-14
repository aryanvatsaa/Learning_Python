# ENCAPSULATION : - IT REFERS TO THE BUNDLING OF DATA (ATTRIBUTES) AND METHODS (FUNCTIONS) THAT OPERATE ON THE DATA INTO A SINGLE UNIT, CALLED A CLASS. 
# ENCAPSULATION ALSO INVOLVES RESTRICTING ACCESS TO CERTAIN COMPONENTS OF AN OBJECT, WHICH IS ACHIEVED THROUGH ACCESS MODIFIERS (PUBLIC, PRIVATE, PROTECTED).

#1. PUBLIC ACCESS : - PUBLIC MEMBERS OF A CLASS ARE ACCESSIBLE FROM OUTSIDE THE CLASS. THEY CAN BE ACCESSED DIRECTLY USING THE OBJECT OF THE CLASS. SYNTAX : - object_name.member_name

#2. PROTECTED ACCESS : - PROTECTED MEMBERS OF A CLASS ARE INTENDED TO BE USED ONLY WITHIN THE CLASS AND ITS SUBCLASSES. THEY ARE INDICATED BY A SINGLE UNDERSCORE PREFIX (_) BEFORE THE MEMBER NAME. SYNTAX:- object_name._member_name   

#3. PRIVATE ACCESS : - PRIVATE MEMBERS OF A CLASS ARE NOT ACCESSIBLE FROM OUTSIDE THE CLASS. THEY ARE INTENDED TO BE USED ONLY WITHIN THE CLASS. IN PYTHON, PRIVATE MEMBERS ARE INDICATED BY A DOUBLE UNDERSCORE PREFIX (__) BEFORE THE MEMBER NAME. SYNTAX : - object_name.__member_name

# EXAMPLE : -
class Example:
    def __init__(self):
        self.public_var = "I am public"                 # Accessible
        self._protected_var = "I am protected"           # Accessible but not recommended
        self.__private_var = "I am private" 

print(Example().public_var)          
print(Example()._protected_var)      
# print(Example().__private_var)     # Not accessible from outside the class - Gives Error

example = Example()
print(example._Example__private_var)      #private variable is accessed using name mangling technique