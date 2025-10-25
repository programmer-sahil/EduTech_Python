# # how to append a file in write mode?
# with open("abc.txt", "r") as f:
#     f.read()


# 📄 1. readline() – Read One Line at a Time
# Read first line from a file
# f = open("last.txt", "r")
# line = f.readline()
# print(line)
# f.close()





# 📄 2. readlines() – Read All Lines as List
# Read all lines as list
# f = open("last.txt", "r")
# lines = f.readlines()
# print(lines)
# f.close()







# ✍️ 3. writelines() – Write List of Strings
# Writing multiple lines
# lines = ["Python\n", "Java\n", "C++\n"]
# f = open("last.txt", "w")
# f.writelines(lines)
# f.close()





# 🖨️ 4. Redirect print() Output to a File
# f = open("last.txt", "w")
# print("Hello students!", file=f)
# f.close()




# # 🧭 5. tell() – Get Current File Pointer Position
# f = open("last.txt", "r")
# print(f.tell())  # 0 at beginning
# f.read(5)
# print(f.tell())  # 5 after reading 5 characters
# f.close()






# ↩️ 6. seek() – Move the Pointer to Any Position
# f = open("last.txt", "r")
# f.seek(7)
# print(f.read())  # Reads from 8th character
# f.close()




# 🛠️ 7. flush() – Force Write to File Immediately
# f = open("last.txt", "w")
# f.write("Python")
# f.flush()  # Makes sure content is written now
# f.close()




# 📟 8. fileno() – Get OS File Descriptor Number
# f = open("last.txt", "r")
# print(f.fileno())
# f.close()

'''
The fileno() function returns the file descriptor number assigned by your operating system when a file is opened.

Think of it like this:

📂 Opening a file is like getting a ticket number at a bank.
Every open file gets a unique number (called a file descriptor) used internally by Python and your OS to manage files.


This means → The operating system assigned file descriptor number 3 to this open file.
'''


# ❓ 9. isatty() – Check if File is Connected to Terminal
# f = open("last.txt", "r")
# print(f.isatty())  # Usually False
# f.close()




# 🔁 10. next() with File – Read Line-by-Line
# f = open("last.txt", "r")
# print(next(f))  # Read first line
# print(next(f))  # Read second line
# f.close()


'''
📄 11. File Modes Summary Table (important for MCQ)

| Mode  | Meaning                 |
| ----- | ----------------------- |
| `r`   | Read (default)          |
| `w`   | Write (overwrites file) |
| `a`   | Append                  |
| `r+`  | Read + Write            |
| `w+`  | Write + Read            |
| `a+`  | Append + Read           |
| `rb`  | Read in binary          |
| `wb`  | Write in binary         |
| `r+b` | Read/Write binary       |

'''





