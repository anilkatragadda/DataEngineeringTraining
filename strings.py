

s = "string"
s.capitalize()

s = "rrrtttttffffggggggg"
s.count('t', 5, 9)

s = "rrrtttttffffggggggg"
s.endswith('ggg')  # s.endswith('ggg', start, end)

s = "rrrtttttffffggggggg"
s.startswith('rrr')  # s.startswith(x, start,end)

s = "Arthur"
s.index('t') # , start, end

s = "354rtery"
s.isalnum()

s = "jhgjh"
s.isalpha()

s = "6"
s.isdigit()

s = "False"
s.islower()

s = "5635476"
s.isnumeric()

s = "True"
s.isupper()

s = ['this ', 'is ', 'python ', 'language']
' - '.join(s)
# 'this  - is  - python  - language'

s = "this is python language"
s.split(' ')

s = "   this is python language    "
s.strip()

s = "this is python languagemmm"
s.strip('m')

s= 'upper'
s.upper()

s= 'LOWER'
s.lower()

s = "ttttttttttttt"
s.replace('t', 'u' )

s = "lower CASE"
s.swapcase()
