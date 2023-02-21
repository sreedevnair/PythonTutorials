########-------File Handling------########

f = open('F:\pyhton tutorial idle\demo.py','r')



### At first we have to mention the path of the document and in the next parameter we have to mention what we have to do
### r = read
### w = write
### a = append
### rb = readbinary
### wb = writebinary

print(f.read()) ### this will print the whole document

print(f.readline()) ### this will print the first line of the document
print(f.readline())

### This will leave a line space between each line , and to remoe it w have to do the following

print(f.readline(),end="")
print(f.readline(),end="")
print(f.readline(),end="")

print("")

print(f.readline(4),end="") ### Mentioning some number inside the () will give as the value till that index number of that line

### How to use the (w) write function

f1 = open('abc.py', 'w') ### Using 'w' , we are creating a new file named as abc
f1.write("people")
f1.write("Hello World") ### This will write something new

f1 = open('abc.py', 'a') ### using a we can add somthinf to the existing file
f1.write("newly added")

### we have to fetch something from a file by using for loop

for data in f:
    print(data)

### When we have to copy somthing from first file and paste it on another file

for data in f:
    f1.write(data)

### when we have to read a image we can only read it in a binary form
### we can convert read binary to write binary and get the image
    
