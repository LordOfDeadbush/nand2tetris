x=input("put line here with $ as placeholder and \\n as endl >>>")
y=input("how many lines >>>")
for i in range(int(y)):
    print(x.replace('$', str(i)).replace('\\n','\n'))