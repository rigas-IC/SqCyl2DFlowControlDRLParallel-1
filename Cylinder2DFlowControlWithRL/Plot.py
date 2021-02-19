import pandas as pd
import termplotlib as tpl
import numpy as np 
import os 
dir_path=os.path.dirname(os.path.realpath(__file__))


data=pd.read_csv(dir_path+'/saved_models/returns_tf.csv',delimiter=';')
r=np.array(data['Return'])
e=np.array(data['Episode'])
fig=tpl.figure()
fig.plot(list(e),list(r))
fig.show()
