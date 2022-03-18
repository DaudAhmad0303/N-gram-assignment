import  codecs
import os
tokens = dict()

# print(f.read())         # reading all file content
path = r"D:\\Daud Ahmad\\6th Semester\\NLP\\Assignment 2\\Corpus\\Sports"
# Change the directory
os.chdir(path)
# iterate through all files
for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        f = codecs.open(file_path,'r','UTF-8')
        for x in f:
            lst = x.split(' ')
            for t in lst:
                if t not in tokens:
                    tokens[t] = 1
                else:
                    tokens[t] += 1
        f.close()
path = r"D:\\Daud Ahmad\\6th Semester\\NLP\\Assignment 2\\Result.txt"
f = codecs.open(path, 'w', 'UTF-8')
f.write('Count\t\tWords\n')
for x, y in tokens.items():
    f.write(str(y))
    f.write('\t\t')
    f.write(x)
    f.write('\n')
f.close()
print(f'Total types in the provided directory are {len(tokens)} and total tokens are {sum(tokens.values())}')
print(f'Result has been written to file "Result.txt"')