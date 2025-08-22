# break: stop the execution
# continue: skips the iteration

# Continue: WAP to print 1-10 but skips the number 5
for i in range(1,11):
    if(i==5):
        continue
    print(i)


# break: WAP to print 1-10 but when the number is 4 then stop the execution
for i in range(1,11):
    if(i==4):
        break
    print(i)