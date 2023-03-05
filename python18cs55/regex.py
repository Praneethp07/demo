import re


# str = "this is my phone no:444-444-2222"
# regex = re.compile(r'\d{3}-\d{3}-\d{4}')
# res = regex.search(str)
# print(res.group())




# matching multiple groups with pipe
#
# regex1 = re.compile(r'batman|tina fey')
# output = regex1.search("tina fey and batman are close friends")
# print(output)
# the one which matches first will be outputed
#output= tina fey



# matching multiple groups with pipe
#
# regex2 = re.compile(r'bat(man|mobile|copter|bat)')
# result = regex2.search("a batcopter was in the way of a batmobile")
# print(result.group())

# optional matching with the question mark
# regex3 = re.compile(r'bat(wo)?(man|men)')
# result  = regex3.search("batwomen and batman with wheels")



# optional matching with   '?'


# regex4 = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
# result = regex4.search("444-4444")


# matching zero or more with *
#
# regex5= re.compile(r'bat(wo)*man')
# result = regex5.search("he is called batwowoman")


# matching zero or more with +
# If you need to match an actual plus sign character, prefix the plus
# sign with a backslash to escape it: \+.

# Matching Specific Repetitions with Curly Brackets
# regex6 = re.compile(r'(Ha){3}')
# result = regex6.search("HaHaHa")

# greedy and non greedy matching

# greedy

# regex7 = re.compile(r'(ha){3,5}')
# result = regex7.search('hahahahaha')


# ?non greedy
# regex7 = re.compile(r'(ha){3,5}?')
# result = regex7.search('hahahahaha')





# findall() method
# findall() method will return the strings of every match in the searched string.



# regex8 = re.compile(r'\d{3}-\d{3}-\d{4}')
# result = regex8.findall("Cell: 415-555-9999 Work: 212-555-0000")
# print(result)


'''
\d:  Any numeric digit from 0 to 9.
\D:  Any character that is not a numeric digit from 0 to 9.
\w:  Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
\W:  Any character that is not a letter, numeric digit, or theunderscore character.
\s:  Any space, tab, or newline character. (Think of this as matching “space” characters.)
\S:  Any character that is not a space, tab, or newline.'''

# character class

# regex9 = re.compile(r'\d+\W+\w+')
# result = regex9.findall("12 drummers ,11  pipers, 10 lords # 8 _ladies")


# ?making your own character class

# regex10 = re.compile(r'[aeiouAEIOU]')
# result = regex10.findall("my name is praneeth ")


# regex11 = re.compile(r'[a-zA-z0-9]')
# result = regex11.findall("my name is praneeth  sdsoojd97986dsds dsd")
#


# negative character class
# regex12 = re.compile(r'[^aeiou]')
# result = regex12.findall("praneeth is a thick asshole")


# caret and dollar sign


'''the caret symbol (^) at the start of a regex to indicate that a match
must occur at the beginning of the searched text.'''


'''a dollar sign ($) at the end of the regex to indicate the string must
end with this regex pattern'''


# starts with hello
# regex13 = re.compile('^hello')
# result = regex13.search("d hello guys")
# ends with hello
# regex14 = re.compile(r'\d$')
# result = regex15.search('1d hello guys hello d1')
# print(result)

# regex15 = re.compile(r'^\d+$')
# result = regex15.search('234444444')

# ?the wild card character
# regex16 = re.compile(r'.at')
# result = regex16.findall("cat rat mat bat are ate only ones who ate everything")


# matching everything using (.) and (*)

# regex17  = re.compile(r'first name:(.*) last name:(.*)')
# result = regex17.findall("first name:praneeth last name:siddhanth")

# matching new line
# regex18 = re.compile(r'.*',re.DOTALL)
# result = regex18.search("hello guys.\n hdbdfhdf.\nfdfdfd.\n")
# print(result.group())

# regex19 = re.compile(r'RoBOcop',re.IGNORECASE)
# result = regex19.search('robocop had a big head')
# print(result.group())


# substitute a word with other

# regex20 = re.compile(r'Agent \w+')
# result = regex20.sub('praneeth',"Agent is a good person and Agent was very good at math")
# print(result)






