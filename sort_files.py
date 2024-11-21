import os
file_path = os.path.join(os.getcwd(), 'sorted')
os.chdir(file_path)

filesdict = {}
with open('1.txt','r',encoding='utf-8') as f:
    filesdict['1.txt'] = len(f.readlines())
    
with open('2.txt','r',encoding='utf-8') as f:
    filesdict['2.txt'] = len(f.readlines())
    
with open('3.txt','r',encoding='utf-8') as f:
    filesdict['3.txt'] = len(f.readlines())
    
fileslist = sorted(filesdict.items(), key=lambda x: x[1])
sortdict = dict(fileslist)

with open('result.txt','w',encoding='utf-8') as rf:
    for file in sortdict:
        rf.write(file)
        rf.write('\n')
        rf.write(str(sortdict[file]))
        rf.write('\n')
        with open(file,'r',encoding='utf-8') as f:
            for line in f:
                rf.write(line)
        rf.write('\n')