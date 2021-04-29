#    FUNCTION TO CHECK IF A NUMBER IS ODD OR EVEN BY RETURNING TRUE OR FALSE
def odd_or_even(number):
     #    FIRST WE CHECK IF THE number IS LESS THAN 2 OR NOT
     if (number < 2):
          #    IF IT IS, WE USE THE MODULUS OPERATOR TO SEE F IT IS EVEN OR NOT
          return (number % 2 == 0)
     
     # IF THE number IS MORE THAN 2, THEN RUN THE odd_or_even(number - 2)
     return (odd_or_even(number - 2))