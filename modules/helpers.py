#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import print_function

def load_kernel(fn, name):

  from pycuda.compiler import SourceModule

  with open(fn, 'r') as f:
    k = f.read()

  mod = SourceModule(k)
  return mod.get_function(name)

  return k
