import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from glob import glob

full_data = pd.read_csv("Loc1_session1_group1_2025-04-16_16-05-24.csv")
display(full_data)
spectrum_data = pd.read_csv("Spectrum_Loc1_session1_group1_2025-04-16_16-05-24.csv")
display(spectrum_data)
