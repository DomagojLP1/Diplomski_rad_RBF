from oct2py import octave
from oct2py import Oct2Py
import os
import numpy as np
import pandas as pd
from scipy import integrate
import matplotlib.pyplot as plt
import math



steps = [5, 10, 15, 20, 30, 40]  # in khz
hz_from_to = [50, 400]  # in khz
AE_data_dict = {'name': []}
for step in steps:
    for i in range(math.ceil(350 / step)):
        start = 50 + i * step
        end = 50 + step + i * step
        if end > 400:
            end = 400
        AE_data_dict['{}-{}'.format(int(start), int(end))] = []