def vowel(s):
   return sum(1 for c in s if c.lower() in 'aeiou')
s = input("enter the word:")
print( vowel(s))