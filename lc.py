#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
for using leetcode easily
author: Lucian
"""
#%% import and setup
import os
import sys
import time
import shutil # for copyong file
import json
import numpy as np
import progressbar as pb
import pandas as pd

os.chdir(sys.path[0])
dc = os.path.expanduser('~/.lc/') # dir of cache of leetcode
d='./source/' #dir of saved source files
dsave='./cache/' # dir of the cache of this program

if not os.path.exists(dc):
    os.makedirs(dc)
if not os.path.exists(d):
    os.makedirs(d)
if not os.path.exists(dsave):
    os.makedirs(dsave)

welcome='''
#######################################
LeetCode Helper
Version 1.0
By Lucian
Basing on leetcode-cli v0.10.1-dfa8759
#######################################
'''


hlp='''
exit: exit this program
h/help: get the help infomation  
d/do: do an excercise! Some letters can follow, including:
    e(easy),m(medium),h(hard),d(done),s(starred)
    Uppercase means negative, e.g. D(not done)
    If not, it will automatically choose the easiest level left.
sh: execute a command after 'sh'.
download: download all souce files to the dir 'source'.

You can also input the following codes:
'''

#%% functions for print
def pry(string):
    'print in yellow'
    print('\033[1;33m' +string+ '\033[0m')
def addy(string):
    'add yellow to a string'
    return '\033[1;33m' +string+ '\033[0m'
def prr(string):
    'print in red'
    print('\033[1;31m' +string+ '\033[0m')
def addr(string):
    'add red to a string'
    return '\033[1;31m' +string+ '\033[0m'

#%% checking dependence
pry('Checking leetcode-cli and xed...')
if os.system("leetcode version")!=0:
    prr('Can not find leetcode!')
    prr('Please read:')
    print('https://skygragon.github.io/leetcode-cli/install')
    exit()
if os.system("xed --version")!=0:
    prr('Can not find xed!')
    exit()

#%% functions about file (or command) 
def store(fname,data):
    if os.path.exists(fname):
        shutil.copy(fname, fname+'.bak')
    with open(fname, 'w') as json_file:
        json_file.write(json.dumps(data))
def load(fname):
    with open(fname) as json_file:
        data = json.load(json_file)
    return data
def readfile(fname):
    with open(fname) as f:
        text = f.read()
    return text
def get_cmd(cmd):
    'get the output of shell code "cmd"'
    with os.popen(cmd) as f:
        texts = f.readlines()
    return texts
#%% get the list
def get_list(n=0,q=''):
    '''
    n=index
    q=
    e(easy),m(medium),h(hard),d(done),l(locked),s(starred)
    Uppercase means negative, e.g. D(not done)
    '''
    if not os.path.exists(dc+'all.json'):
        get_cmd('leetcode list')
    all_ = load(dc+'all.json')
    if n>0:
        for i in all_:
            if i['id']==n:
                return i
    else:
        lst = all_
        if 'e' in q:
            lst = [i for i in lst if i['level']=='Easy']
        if 'E' in q:
            lst = [i for i in lst if i['level']!='Easy']
        if 'm' in q:
            lst = [i for i in lst if i['level']=='Medium']
        if 'M' in q:
            lst = [i for i in lst if i['level']!='Medium']
        if 'h' in q:
            lst = [i for i in lst if i['level']=='Hard']
        if 'H' in q:
            lst = [i for i in lst if i['level']!='Hard']
        if 'D' in q:
            lst = [i for i in lst if i['state']=='None']
        if 'd' in q:
            lst = [i for i in lst if i['state']!='None']
        if 's' in q:
            lst = [i for i in lst if i['starred']]
        if 'S' in q:
            lst = [i for i in lst if not i['starred']]
        if 'l' in q:
            lst = [i for i in lst if i['locked']]
        if 'L' in q:
            lst = [i for i in lst if not i['locked']]
    return lst

    
#%% refresh a dir
def rm_dir(dire,exception=[]):
    if not input('Refresh '+dire+'? (y/n) ').startswith('y'):
        return -1
    if dire == dc:
        exception.append('.user.json')
    if os.path.exists(dire+'bak/'):
        shutil.rmtree(dire+'bak/')
    os.mkdir(dire+'bak/')
    for i in os.listdir(dire):
        if (i!='bak') and (i not in exception):
            shutil.move(dire+i,dire+'bak/')

#%% define class
class problem(object):
    def __init__(self,n):
        # n can be both int or str!
        self.id = int(n) # index - int
        self.ids = str(n) # index -str
        self.__dict__.update(get_list(self.id))
        self.loaded = False
    def load(self):
        'load all information about the problem'
        f1 = dc+self.key+'.json'
        f2 = d + self.ids+'.json'
        if os.path.exists(f1):
            self.__dict__.update(load(f1))
        else:
            if os.path.exists(f2):
                self.__dict__.update(load(f2))
            else:
                get_cmd('leetcode show '+self.ids)
                self.__dict__.update(load(f1))
        self.loaded=True
    def download(self):
        'if cannot find json file in path d, save it'
        f1 = dc+self.key+'.json'
        f2 = d + self.ids+'.json'
        if not os.path.exists(f1):
            get_cmd('leetcode show '+self.ids)
        if not os.path.exists(f2):
            shutil.copy(dc+self.key+'.json', d+self.ids+'.json')
    def cache(self):
        if not self.loaded:
            self.load()
        store(dsave+self.ids+'.json',self.__dict__)
    def show(self):
        if not self.loaded:
            self.load()
        pry('['+self.ids+'] '+self.name)
        print(addy(' *'),self.level,'('+str(round(self.percent,2))+'%)')
        print('')
        print(self.desc.strip())
    def write(self):
        pass


#%% functions for the codes accepted
def h():
    'help'
    print(hlp)
    os.system('leetcode help')

def down():
    'download all source files'
    rm_dir(dc)
    rm_dir(d)
    #rm_dir(dsave)
    lst = get_list()
    idlst = [i['id'] for i in lst if not i['locked']]
    pry('Downloading...')
    pba = pb.progressbarClass(len(idlst), '=')
    pba.progress(0)
    for ni,i in enumerate(idlst):
        p = problem(i)
        p.download()
        p.cache()
        pba.progress(ni+1)
    pry('Finished.')

 
def do_all(ps,p):
    'automatically solve a question'
    pry('Checking the question list...')
    if len(ps)>0:
        lst = get_list(q=p)
    else:
        lst = get_list(q='LDe')
        if len(lst)==0:
            lst = get_list(q='LDm')
            if len(lst)==0:
                lst = get_list(q='LDh')
    if len(lst)==0:
        prr('No unlocked questions are found!')
        return 
    ind = np.random.choice([i['id'] for i in lst]) # index of question
    prob = problem(ind)
    prob.load()
    
    
    
    if os.path.exists(d+nq+'.json'):
        dic = load(d+nq+'.json')
        fname = dic['filename']
        if os.path.exists(fname):
            prr('File '+fname+' exists, please check!')
            return
        if os.path.exists('./submitted/'+fname):
            prr('File '+fname+' exists in "./submitted", please check!')
            return
        shutil.copy(d+fname, fname)
        fname = './'+fname
        print(''.join(dic['text']))
    else:
        fs0 = os.listdir()
        os.system('leetcode show '+nq+' -g -x -l python')
        fname = './'+[f for f in os.listdir() if f not in fs0][0] # file name
    while True:
        pry('Please write your codes in xed, remember to save it...')
        # the time used
        time0 = time.time()
        os.system('xed '+fname)
        tall = time.time()-time0
        # store the time used
        times = load('time.json') 
        if nq not in times: times[nq]=[]
        times[nq].append(tall)
        store('time.json',times)
        
        test_code = get_test_code(fname)
        os.system('leetcode test '+fname+' -t '+test_code)
        pry('What do you want next?')
        pry('c/[Enter] = change codes, s = submit, e = exit')
        ip2 = input(addy('?> '))
        if ip2.startswith('c') or ip2=='':
            continue
        elif ip2.startswith('e'):
            return
        elif ip2.startswith('s'):
            os.system('leetcode submit '+fname)
            if not os.path.exists('./submitted/'):
                os.makedirs('./submitted/')
            shutil.move(fname,'./submitted/'+fname)
            pry('Change your answer?')
            pry('y=yes, n=no')
            if input(addy('?> ')).startswith('y'):
                continue
            else:
                break
    os.system('leetcode stat')
    os.system('leetcode stat -g')

  

    
    



#%%############################
# the main part of the program
###############################
pry(welcome)
while(True):
    ip = input(addy('\nleetcode >>> '))
    ips = ip.split()
    if ips==[]:
        continue
    cmd = ips[0]
    pars = ips[1:]
    par = " ".join(pars)
    if cmd=='exit':
        break
    elif cmd in ['h','help']:
        h()
    elif cmd in ['d','do']:
        do_all(pars,par)
    elif cmd=='sh':
        os.system(par)
    elif cmd=='download':
        down()
    elif cmd=='cwd':
        print(sys.path[0])
    else:
        os.system('leetcode '+ip)
