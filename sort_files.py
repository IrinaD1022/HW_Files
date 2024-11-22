import os

def sort_files():
    files_txt = [f for f in os.listdir() if f.endswith('.txt')]
    filesdict = {}
    for filename in files_txt:
        if filename != 'result.txt':
            with open(filename,'r',encoding='utf-8') as f:
                 filesdict[filename] = len(f.readlines())
      
    fileslist = sorted(filesdict.items(), key=lambda x: x[1])
    return dict(fileslist)

def write_file():
    file_path = os.path.join(os.getcwd(), 'sorted')
    os.chdir(file_path)
    sortdict = sort_files()
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
    print('Check file RESULT.TXT')
        
write_file()