# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 10:38:00 2018

@author: flavio

"""

import numpy as np

fileName = '/home/flavio/Downloads/teste_lte_ul.bin'


def read_bin_files(fileName):
  x = ()
  data = open(fileName, 'rb')
  x = np.fromfile(data,dtype=np.float32)

  signal = []

  for i in range(0, len(x)):
    if i % 2 == 0:
       real_part = x[i]
    else:
       imag_part = x[i]
       signal.append(complex(real_part, imag_part))
  return signal


my_signal = read_bin_files(fileName)
