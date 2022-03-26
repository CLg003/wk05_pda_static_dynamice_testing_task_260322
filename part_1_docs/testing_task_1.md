### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

# the class of which "card", "card1" and "card2" are objects needs to be imported

class CardGame:
  # The class needs to be initiated here with def __init__(self) ???????

  def check_for_ace(self, card):
    if card.value = 1: # 1. The class of which object "card" is an instance needs to be imported, 2. "==" needed to check equality in conditional statement
      return True
    else # Missing colon
      return False
   

  dif highest_card(self, card1 card2): # 1. Def has been misspelled as "dif", 2. class of which card1 and card2 are objects needs to be imported, 3. missing comma between "card1" and "card2"
  if card1.value > card2.value: # Body of the function should be indented
    return card # "card" has not been defined, should be "card1"
  else:
    return card2
  


def cards_total(self, cards): # Entire method needs to be indented
  total # "total" needs to be assigned to 0
  for card in cards:
    total += card.value # The class of which object "card" is an instance needs to be imported
    return "You have a total of" + total # 1. Cannot concatenate strings and integers - string formatting needed or "total" needs to be converted to a string plus a space added after "of", 2. This line should be at the same level of indentation as the for loop statement.
  
```
