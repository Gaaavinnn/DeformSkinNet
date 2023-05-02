import numpy as np
from sklearn.decomposition import PCA
import os
import ast 
from sklearn import preprocessing
import numpy as np

label_7_list=[]
label_8_list=[]
str_list=[]
for root, dirs, files in os.walk("./dataset/train/mid_labels/", topdown=False):
    for name in files:
        txt_path = os.path.join(root, name)
        # print(txt_path)
        with open(txt_path, "r") as txt_f:
            for line in txt_f:
                #print(line)
                list_8 = line[-72:]
                #print(list_8)
                list_8 = ast.literal_eval(list_8)
                
                list_7 = line[-133:-73]
                #print(list_7)
                list_7 = ast.literal_eval(list_7) 
                
                
                label_7_list.append(list_7)
                str_1 = line[18:41]
                str_list.append(str_1)
                
                #print(str_1)
                
                label_8_list.append(list_8)
                
def Pca_inv(X,n_com):
    
    pca = PCA(n_components=n_com)
    newX = pca.fit_transform(X)     #等价于pca.fit(X) pca.transform(X)

 

     
    min_max_scaler = preprocessing.MinMaxScaler()
    newX = min_max_scaler.fit_transform(newX)
    #print(type(newX))

    return newX
def science_float(str_s):
    if 'e' in str_s:
        str_list = str_s.split('e')
        carry_bit = str_list[-1]
        str_num = str_list[0].split('.')
        if float(carry_bit)<0:
            zero_expend = '0'*(-int(carry_bit)-1)
        
            str_comp = '0.'+zero_expend+str_num[0]+str_num[0]
    else:
        str_comp = str_s
    return str_comp
X = np.array(label_7_list)
newX_7 = Pca_inv(X,3)
X = np.array(label_8_list)
newX_8 = Pca_inv(X,3)
print(newX_8.shape)
new_root = "./dataset/train/labels/"
key_file = 0

for name in files:
    txt_path = os.path.join(new_root, name)
    #print(newX_7[key_file,0])
    new_7_0 = science_float(str(float(newX_7[key_file,0])))
    new_7_1 = science_float(str(float(newX_7[key_file,1])))
    new_7_2 = science_float(str(float(newX_7[key_file,2])))
    new_8_0 = science_float(str(float(newX_8[key_file,0])))
    str_write = '0 '+ new_7_0 +' '+new_7_1+' '+new_7_2+' '+ new_8_0+' '+ science_float(str(float(newX_8[key_file,1])))+' '+science_float(str(float(newX_8[key_file,2])))+' '+str_list[key_file]
    key_file+=1
    if 0<=float(new_7_0)+float(new_7_2)/2<=1 or  0<=float(new_7_1)+float(new_8_0)/2<=1:
        #print(float(new_7_0)+float(new_7_2)/2)
        with open(txt_path, "w") as txt_w:
            txt_w.writelines(str_write)
    else:
        print('error')
        print(new_7_0,new_7_1,new_7_2,new_8_0)
    
print(key_file)
# print(X)
#     # [[-1 -1]
#     #  [-2 -1]
#     #  [-3 -2]
#     #  [ 1  1]
#     #  [ 2  1]
#     #  [ 3  2]]
# print(newX)
#     # array([[ 1.38340578,  0.2935787 ],
#     #        [ 2.22189802, -0.25133484],
#     #        [ 3.6053038 ,  0.04224385],
#     #        [-1.38340578, -0.2935787 ],
#     #        [-2.22189802,  0.25133484],
#     #        [-3.6053038 , -0.04224385]])
# print(invX)
#     # [[-1 -1]
#     #  [-2 -1]
#     #  [-3 -2]
#     #  [ 1  1]
#     #  [ 2  1]
#     #  [ 3  2]]
# print(pca.explained_variance_ratio_)
    # [ 0.99244289  0.00755711]