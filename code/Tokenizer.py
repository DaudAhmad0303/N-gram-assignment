import os
def processing(path):
      '''
      Accepts path to a file.
      - Removing all types URLs 
      - Adding Space before and after following punctuations:
      
          ``` [. : , ? [ ] ( ) { } | > < + = " ' “ ” ` @ # $ & * / \ ; ] ‘ ’```
      - Removing extra spaces 
      - Adding space with new 
      '''
      import re
      matches = []
      pattern = re.compile("(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])")
      for i, line in enumerate(open(path)):
            for match in re.finditer(pattern, line):
                  matches.append(match.group())
      with open(path, 'r') as file :
        filedata = file.read()

      # Replace the URL string with Null string
      for i in range(len(matches)):
          filedata = filedata.replace(matches[i], '')
      # print(matches)
      # Replacing and correcting Punctuations
      filedata = filedata.replace(".", ' . ')
      filedata = filedata.replace(',', ' , ')
      filedata = filedata.replace(':', ' : ')
      filedata = filedata.replace(';', ' ; ')
      filedata = filedata.replace('&', ' & ')
      filedata = filedata.replace('*', ' * ')
      filedata = filedata.replace('?', ' ? ')
      filedata = filedata.replace('+', ' + ')
      filedata = filedata.replace('=', ' = ')
      filedata = filedata.replace(']', ' ] ')
      filedata = filedata.replace('[', ' [ ')
      filedata = filedata.replace('{', ' { ')
      filedata = filedata.replace('}', ' } ')
      filedata = filedata.replace('(', ' ( ')
      filedata = filedata.replace(')', ' ) ')
      filedata = filedata.replace('@', ' @ ')
      filedata = filedata.replace('#', ' # ')
      filedata = filedata.replace('!', ' ! ')
      filedata = filedata.replace('/', ' / ')
      filedata = filedata.replace('|', ' | ')
      filedata = filedata.replace('>', ' > ')
      filedata = filedata.replace('<', ' < ')
      filedata = filedata.replace("\\", ' \ ')
      filedata = filedata.replace("\n ", ' \n')
      
      filedata = filedata.replace('`', ' ` ')
      filedata = filedata.replace('”', ' ” ')
      filedata = filedata.replace('“', ' “ ')
      filedata = filedata.replace('‘', ' ‘ ')
      filedata = filedata.replace('’', ' ’ ')
      filedata = filedata.replace('"', ' " ')
      filedata = filedata.replace("'", " ' ")
      
      # Replacing double space with single one
      filedata = filedata.replace("  ", " ")
      
      # Write the file out again
      with open(path, 'w') as file:
        file.write(filedata)
      pass
tokens = dict()

path = r"D:\\Daud Ahmad\\6th Semester\\NLP\\Assignment 2\\Corpus\\"
# Change the directory
os.chdir(path)
pathlist = os.listdir(path)
all_paths = []
for x in pathlist:
    all_paths.append(path + x + '\\')

# iterate through all files
for folder in all_paths:
    for file in os.listdir(folder):
        os.chdir(folder)
        if file.endswith(".txt"):
            file_path = folder + '\\' + file
            # Performing text pre-processing like URL Removal and space adding etc.
            processing(file_path)
            # print(file_path)
            f = open(file_path, 'r')
            # print(f.read())
            for x in f:
                lst = x.split(' ')
                for t in lst:
                    if t not in tokens:
                        tokens[t] = 1
                    else:
                        tokens[t] += 1
            f.close()
path = r"D:\\Daud Ahmad\\6th Semester\\NLP\\Assignment 2\\code\\Result.txt"
f = open(path, 'w')
f.write('Count\t\tWords\n')
for x, y in tokens.items():
    f.write(str(y))
    f.write('\t\t')
    f.write(x)
    f.write('\n')
# f.close()
print(f'Total types in the provided directory are {len(tokens)} and total tokens are {sum(tokens.values())}')
print(f'Result has been written to file "Result.txt"')