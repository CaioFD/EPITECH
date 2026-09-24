# (42 > 12)             -> True:  42 is greater than 12
# (12 = 12)             -> SyntaxError: "=" assigns a value, it does not compare
# (12 == 12)            -> True:  "==" checks if both sides are equal
# ("hello" == "world")  -> False: the two strings are different
# (218 >= 118)          -> True:  218 is greater than or equal to 118
# ("a".upper() == "A")  -> True:  "a".upper() turns "a" into "A"
# (1 * 2 * 3 * 4 <= 9)  -> False: 1*2*3*4 = 24, and 24 is not <= 9
# ("z" in "azerty")     -> True:  the letter "z" is inside "azerty"