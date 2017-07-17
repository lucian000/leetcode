#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
for using leetcode easily
author: Lucian
"""
import os
import sys
import time
import shutil # for copyong file
import json
import numpy as np
import progressbar as pb

os.chdir(sys.path[0])

def pry(string):
    'print in yellow'
    print('\033[1;33m' +string+ '\033[0m')
def addy(string):
    'add yellow to a string'
    return '\033[1;33m' +string+ '\033[0m'
def prr(string):
    'print in red'
    print('\033[1;31m' +string+ '\033[0m')

pry('Checking leetcode-cli and xed...')
if os.system("leetcode version")!=0:
    prr('Can not find leetcode!')
    prr('Please read:')
    print('https://skygragon.github.io/leetcode-cli/install')
    exit()
if os.system("xed --version")!=0:
    prr('Can not find xed!')
    exit()

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
    e(easy),m(medium),h(hard),d(done),l(locked),s(starred)
    Uppercase means negative, e.g. D(not done)
    If not, it will automatically choose the easiest level left.
s: show a problem with python (followed by an index or name!)
sh: execute a command after 'sh'.
download: download all souce files to the dir 'source'.

You can also input the following codes:
'''
#%% json and text files
def store(fname,data):
    if os.path.exists(fname):
        shutil.copy(fname, fname+'.bak')
    with open(fname, 'w') as json_file:
        json_file.write(json.dumps(data))
def load(fname):
#    if os.path.exists(fname)==False:
#        store(fname,{})
    with open(fname) as json_file:
        data = json.load(json_file)
    return data
def readfile(fname):
    with open(fname) as f:
        text = f.read()
    return text

#%% define class
class problem(object):
    def __init__(self,n):
        self.n = int(n) # index - int
        self.ns = str(n) # index -str
        self.loaded = False
    def download(self, d='./source/'):
        'if cannot find json file in path d, download it and save it'
        if os.path.exists(d+self.ns+'.json'):
            return -1
        else:
            os.chdir(d)
            text = get_cmd('leetcode show '+self.ns+' -g -x -l python')
            fname = [j for j in os.listdir() if j.startswith(self.ns+'.') and j.endswith('.py')][0]
            store(self.ns+'.json',{'text':text,'filename':fname})
            os.chdir(sys.path[0])
    def load(self, d='./source/'):
        'load all information about the problem'
        self.download(d)
        source = load(d+self.ns+'.json')
        text = source['text']
        # py file name
        self.filename = source['filename']
        # py code text - str
        self.file = readfile(d+self.filename) 
        # title - str
        self.title = text[0].split(']')[1].split('\t')[0].strip()
        # url - str
        self.url = text[2].strip()
        # difficulty - str
        self.difficulty = text[4].split('*')[1].split('(')[0].strip()
        # ac_rate - str
        self.ac_rate = text[4].split('(')[1].split('%)')[0].strip()
        # total_accepted - str
        self.total_ac = text[5].replace('* Total Accepted:','').strip()
        # total_submissions - str
        self.total_sub = text[6].replace('* Total Submissions:','').strip()
        #test_code - str
        self.test_code = text[7].replace('* Testcase Example:','').strip()
        # description - str
        self.description = ''.join(text[8:]).strip()
        self.loaded = True
    def save(self, dsave='./save/'):
        if not self.loaded:
            self.load()
        if not os.path.exists(dsave):
            os.mkdir(dsave)
        store(dsave+self.ns+'.json',self.__dict__)
    
#%%################################
def h():
    'help'
    print(hlp)
    os.system('leetcode help')

def s(pars,par):
    'better show'
    if len(pars)<1:
        prr('Error: You may miss a parameter after "s".')
        return
    else:
        os.system('leetcode show '+par+' -g -x -d -l python')

def get_cmd(cmd):
    'get the output of shell code "cmd"'
    f = os.popen(cmd)
    lst = f.readlines()
    f.close()
    return lst
def unl(lst):
    'only choose unlocked questions'
    return [i for i in lst if i.find('🔒')==-1]

def get_test_code(fname):
    'get the test codes from the .py file'
    hint = '# Testcase Example:'
    f = open(fname)
    while True:
        line = f.readline()
        if line.startswith(hint):
            f.close()
            return line.replace(hint, '')
        if line=='':
            f.close()
            prr('Error: cannot find the test code.')
            return "''"
    
def do_all(ps,p, d = './source/'):
    'automatically solve a question'
    pry('Checking the question list...')
    if len(ps)>0:
        lst = unl(get_cmd('leetcode list -q '+ps[0]))
    else:
        lst = unl(get_cmd('leetcode list -q eD'))
        if len(lst)==0:
            lst = unl(get_cmd('leetcode list -q mD'))
            if len(lst)==0:
                lst = unl(get_cmd('leetcode list -q hD'))
    if len(lst)==0:
        prr('No unlocked questions are found!')
        return 
    nq = np.random.choice(lst).split('[')[1].split(']')[0].strip() # index of question
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

def int2(string):
    try:
        return int(string)
    except:
        return -1
    
def down(d = './source/'):
    'download all souce files in the dir "source"'
    if os.path.exists(d)==False:
        os.makedirs(d)
    os.chdir(d)
#    inds = load('index.json')
#    ns_e = inds.keys()
    f_e = os.listdir()
    ns_e = [int2(i.replace('.json','')) for i in f_e if i.endswith('.json')]
    pry('Trying to get the downloading list...')
    lst = unl(get_cmd('leetcode list'))
    ns_all = [int2(i.split('[')[1].split(']')[0]) for i in lst]
    if -1 in ns_all:
        prr('Error in the list!')
        return
    ns = [i for i in ns_all if i not in ns_e]
    pry('Downloading...')
    pba = pb.progressbarClass(len(ns), '=')
    for ni,i in enumerate(ns):
        text = get_cmd('leetcode show '+str(i)+' -g -x -l python')
        fname = [j for j in os.listdir() if j.startswith(str(i)+'.') and j.endswith('.py')][0]
        store(str(i)+'.json',{'text':text,'filename':fname})
        pba.progress(ni+1)
    os.chdir(sys.path[0])
    pry('Finished.')

#def tem():
#    fs = os.listdir('./source/')
#    fsjson = [i for i in fs if i.endswith('.json')]
#    for i in fsjson:
#        dic = load('./source/'+i)
#        fname = [j for j in fs if j.startswith(str(i.replace('.json',''))+'.') and j.endswith('.py')][0]
#        dic['filename'] = fname
#        store('./source/' +str(i),dic)

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
    elif cmd=='s':
        s(pars,par)
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
