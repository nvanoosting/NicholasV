import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

df = pd.DataFrame(sns.load_dataset("penguins"))

print(df.shape)