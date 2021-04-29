#    RECURSIVE FUNCTION TO CHECK IF A GIVEN WORD IS A PALINDROME
def is_palindrome(word):
     #    IF A STRING HAS 0 LETTERS, IT IS A PALINDROME
     if len(word) == 0: 
          return True
     
     # NOW, WE CHECK IF THE FIRST LETTER AND THE LAST LETTER DONT MATCH
          #    IF YES, THEN, ITS NOT A PALINDROME
     if word[0] != word[-1]: 
          return False
     
     return is_palindrome(word[1:-1])


print(is_palindrome('madam'))

