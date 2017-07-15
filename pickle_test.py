#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 08:09:45 2017

@author: ylx
"""

import pickle

x=[1,2,3]
pickle.dump(x)
pickle.dumps(x)
pickle.loads(pickle.dumps(x))
