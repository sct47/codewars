def rot13(str): 
  
  # our new string with the modified characters
  newString = ""

  # begin by looping through each character in the string
  for char in str:
    
    # check if the current character is an alphabetic character
    if char.isalpha():

      # if alphabetic character in the latter half of the alphabet:
      if char.lower() in "nopqrstuvwxyz":
        char = chr(ord(char) - 13)
      # if alphabetic character then add 1 to its ASCII value 
      # by using the built-in ord function then convert back to character
      else:
        char = chr(ord(char) + 13)

    else:
      char = char

    # add this modified character to the new string
    newString = newString + char

  return newString
       
print(rot13("money"))