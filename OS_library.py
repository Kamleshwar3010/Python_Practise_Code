import os
# print(os.name) #output->nt
# print(os.getcwd()) #output->C:\Users\Admin\Programme
# os.chdir("../")
# print(os.getcwd()) #output->C:\Users\Admin
# os.mkdir("./Python/ABC")
# os.makedirs("./Python/XYZ/WWW")
# print(os.listdir())
#      # Output
# '''['.env', '.git', '.vscode', 'Blog-Backend', 'C', 'C++', 'company', 'Computer Graphics', 'Data Structure', 'Hacker Earth', 'Hacker Rank', 'Java', 'leetcode', 'package-lock.json', 'package.json', 'Python', 'R', 'React', 'SQL', 'web-devlopment']'''
# os.rmdir("./ABC")
# os.removedirs("./Python/XYZ/WWW")
# os.chdir("./Python")
# print(os.getcwd())
# fd = os.open("./Python/ABCD.py", os.O_WRONLY | os.O_CREAT)
# os.write(fd, b"print(\"Hello, world!\")")
# with open('./Python/ABCD.py', 'w') as f:
#     f.write('print(\"Hello, world!2\")')
# fd = os.open("./Python/ABCD.py", os.O_RDWR)
# os.lseek(fd, 0, os.SEEK_END)
# os.write(fd, b"\nprint(\"How are you?\")")
# with open('./Python/ABCD.py', 'a') as f:
#     f.write('\nprint(\"Jai hind\")')
# os.close(fd)
# os.remove("./Python/ABCD.py")
# print(os.path.exists("./Python/OS_library.py")) #output-> true
# with open('./Python/ABCD.txt', 'r') as f:
#     line = f.read() # read entire file
# with open('./Python/ABCD.txt', 'r') as f:
#     line = f.readline() # reads a single line at a time
#     while line:
#         print(line)
#         line = f.readline()
# print(os.path.getsize("./Python/ABCD.txt")) #output-> 18
# os.system('python -u "./Python/OS_library.py"') # recursivly run this program again anad again
# os.rename("./Python/A.txt","./Python/A.py")
print("Exist path:", os.access("./Python/ABCD.txt", os.F_OK))#output-> Exist path: True
print("It access to read the file:", os.access("./Python/ABCD.txt", os.R_OK))#output-> It access to read the file: True
print("It access to write the file:", os.access("./Python/ABCD.txt", os.W_OK))#output->It access to write the file: True
print("Check if path can be executed:", os.access("./Python/ABCD.txt", os.X_OK))#output->Check if path can be executed: True
