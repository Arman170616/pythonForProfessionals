#general
 
filename = "readFileDefault.py"
f = open(filename)
lines = []
 
for line in f:
   lines.append(line.strip())
 
print(lines)
 
 
 
#one-liner
 
print([line.strip() for line in open("readFileDefault.py")])
