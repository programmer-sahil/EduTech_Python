f = open("cst.txt", "r")

content = f.read()
print(content)

f.close()
# file modes: w (write) r (read) a (append)


# f = open("message.txt", "r")

# content = f.read(6)
# print(content)

# f.close()














# more optimize code & here u don't need to close the file, it works automatically
# with open("message.txt", "r") as f:
#
#     content = f.read()
#     print(content)
