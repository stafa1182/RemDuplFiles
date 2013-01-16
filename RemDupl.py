import glob
import filecmp
import os
import sys

dupl=[]
lista=glob.glob("*.pdf")
for fi1 in lista:
    for fi2 in lista:
        if cmp(os.path.basename(fi1),os.path.basename(fi2))!=0: 
                f1=open(fi1).read()
                f2=open(fi2).read()
                if cmp(f1,f2)==0:
                    print"fi1 is %s and fi2 is %s" %(fi1, fi2)
                    dupl.append(fi2)
                    lista.remove(fi2)
        else:
            exit
        
