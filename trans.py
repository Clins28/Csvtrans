#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs

def find_csv(dir):
    dir = os.path.normpath(dir)
    files = os.listdir(dir)
    for file in files[:]:
        if not file[-3:] == 'csv':
            files.remove(file)
    return files

def convertUTF8ToANSI(oldfile):

    #open utf8 file
    f = codecs.open(oldfile,'r','utf8')
    utfstr = f.read()
    f.close()
    
    #trans to ansi
    outansestr = utfstr.encode('mbcs')


    #save
    newfile = os.path.join('./trans/' + oldfile)
    if not os.path.exists('./trans/'):
        os.makedirs('./trans/')
    f = open(newfile,'wb')
    f.write(outansestr)
    f.close()
    print(oldfile + 'Converted')
    
if __name__=="__main__":
    files = find_csv(os.getcwd())
    for ofile in files:
        convertUTF8ToANSI(ofile)
    print('"尝试"提需求请联系we-chat：clins288')
