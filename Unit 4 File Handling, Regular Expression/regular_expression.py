# Regular Expression (Regex)
# search()
# import re

# txt = "The rain in Germany"
# x = re.search("^The.*Spain$", txt)

# if x:
#     print("YES! We have a match!")
# else:
#     print("No match")




# findall()
# import re

# #Return a list containing every occurrence of "ai":

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)





# search()
# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start()) 



# # The split() Function
# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)



# sub() : Replace every white-space character with the number 9:
# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)


# match() - checks if pattern matches **at the beginning**
# import re

# txt = "Python is awesome"
# x = re.match("Python", txt)

# print(x)           # <re.Match object; span=(0, 6), match='Python'>
# print(x.group())   # Output: Python







# finditer() - returns an iterator with match objects
# import re

# txt = "The rain in Spain"
# matches = re.finditer("ai", txt)

# for m in matches:
#     print(m.group(), m.start())





# compile() - precompile pattern to reuse multiple times
# import re

# pattern = re.compile("[A-Z][a-z]+")
# txt = "Python Java C++"

# matches = pattern.findall(txt)
# print(matches)



# subn() - like sub(), but also returns number of replacements
import re

txt = "I love apples and apples are sweet"
result = re.subn("apples", "oranges", txt)

print(result)   # ('I love oranges and oranges are sweet', 2)
