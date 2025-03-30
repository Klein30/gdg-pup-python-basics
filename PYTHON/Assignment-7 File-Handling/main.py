f = open("sample.txt", "r")
print(f.read())
f.close()

r = open("newfile.txt", "w")
r.write("This is a new file created by Python.")
r.close()

r = open("newfile.txt", "r")
print(r.read())
r.close()