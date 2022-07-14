from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import time

jpg=Image.open('ptaszor.jpg')
szarejpg=jpg.convert('L')
jpgsvd=np.array(list(szarejpg.getdata(band=0)),float)
jpgsvd.shape=(szarejpg.size[1],szarejpg.size[0])
jpgsvd=np.matrix(jpgsvd)
U,S,V=np.linalg.svd(jpgsvd,full_matrices=False)
for i in [1,5,20,100]:
    newjpg=np.matrix(U[:,:i])*np.diag(S[:i])*np.matrix(V[:i,:])
    plt.imshow(newjpg,cmap='gray')
    title='r=%s' %i
    plt.title(title)
    plt.savefig('jpg_r='+str(i)+'.jpg')
                                    
