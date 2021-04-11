
# Symbols meanings in regular expression

# .         - Any character except new line
# \d        - digit (0-9)
# \D        - Not a digit (0-9)
# \w        - Word character (a-z, A-Z, 0-9, _)
# \W        - not a word character
# \s        - whitespace (space, tab, newline)
# \S        - not a whitespace character

# Reg ex quantifiers

# *         - 0 or more
# +         - 1 or more
# ?         - 0 or one
# {3}       - exact number
# {3, 4}    - range of number (minimum, maximum)

# Reg ex Groups

# ()        - Group
# |         - Either Or

# ========================================================================================

#                                    CODE BEGINS HERE...

# ========================================================================================
import re

print("\n================== RESTRICTION SITE EXAMPLE 1 ==================\n")
dna = "ATCGCGAATTCAC"
EcoRI = r'GAATTC'

if re.search(EcoRI, dna):
    print("EcoRI restriction site found!")

print("\n================== RESTRICTION SITE EXAMPLE 2 ==================\n")
# This defines a group in which there are multiple characters inside
sitoW = r'GG(A|T)CC'
#       r'GG[AT]CC'
if re.search(sitoW, dna):
    print("W site found :)")
else:
    print("W site not found :(")

print("\n================== PROTEIN EXAMPLE 1 ==================\n")
prot = "MATTKLAAQSSYDPQQMFSSRZ"
m = re.search(r'[BJOUXZ]', prot)

if m:
    print("This is not a protein! :( \n"
          "Found '{}' in the sequence".format(m.group()))
else:
    print("This is a protein! :)")

print("\n================== RESTRICTION SITE EXAMPLE 3 ==================\n")
dna = "ATCGGACCCGAATTCAC"
m = re.search(r'GGAT?CC', dna)

if m:
    print("Match found: " + m.group() + " | starts at: " + str(m.start()))
else:
    print("No match")

print("\n================== RESTRICTION SITE EXAMPLE 4 ==================\n")
dna = "ATCGGACCCGAATTCAC"
m = re.search(r'GG(AT)CC', dna)

# There are NO match for this pattern because I have defined a GROUP and not a set of characters within [ ] !!!
if m:
    print("Match found: " + m.group() + " | starts at: " + str(m.start()))
else:
    print("No match")

print("\n================== RESTRICTION SITE EXAMPLE 5 ==================\n")
dna = "ATCGGCCCGAATTCACGGATCC"
m = re.search(r'GG(AT)?CC', dna)

# This way the group in between is OPTIONAL!!
if m:
    print("Match found: " + m.group() + " | starts at: " + str(m.start()))
else:
    print("No match")

print("\n================== RESTRICTION SITE EXAMPLE 6: FINDITER ==================\n")
dna = "ATCGGCCCGAATTCACGGATCC"
matches = re.finditer(r'GG(AT)?CC', dna)

# using FINDITER allows me to get all matches and NOT ONLY the first one
if matches:
    for m in matches:
        print("Match found: " + m.group() + " | starts at: " + str(m.start()))
else:
    print("No match")

print("\n================== RESTRICTION SITE EXAMPLE 7: FINDITER ==================\n")
dna = "ATCGGCCCGGAAAAAAAAAAAAAACCAAAAAAATTCACGGATCC"
matches = re.finditer(r'GGA+CC', dna)

# using FINDITER allows me to get all matches and NOT ONLY the first one
if matches:
    for m in matches:
        print("Match found: " + m.group() + " | starts at: " + str(m.start()))
else:
    print("No match")

print("\n================== IDENTITY MATCH EXAMPLE 1 ==================\n")
s = "x=x"
pattern = re.compile(r'^([a-z]+)=\1$')
matches = re.search(pattern, s)
if matches:
    print(matches.group())
else:
    print("Identity not found")

print("\n================== IDENTITY MATCH EXAMPLE 2 ==================\n")
s = "X = X"
pattern = re.compile(r'^([A-Z]+)(\s*)=\2\1$')
matches = re.search(pattern, s)

if matches:
    print(matches.group())
else:
    print("Identity not found")
