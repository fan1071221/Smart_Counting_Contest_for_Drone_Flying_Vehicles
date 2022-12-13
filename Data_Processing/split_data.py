import os
import numpy as np
import shutil

# Create folder
if not os.path.exists('./datasets'):
    os.makedirs("./datasets")
    os.makedirs("./datasets/TWStreet")
    os.makedirs("./datasets/TWStreet/annotations")
    os.makedirs("./datasets/TWStreet/images")
    os.makedirs("./datasets/TWStreet/labels")

# Creating Train / Val / Test folders
root_dir = './datasets/TWStreet/images'
labels_dir = './datasets/TWStreet/labels'
if not os.path.exists(root_dir + '/train'):
    os.makedirs(root_dir + '/train')
    os.makedirs(root_dir + '/val')
    os.makedirs(labels_dir + '/train')
    os.makedirs(labels_dir + '/val')

img_src = "train"  # Folder to copy images from
yologt = "result"

allFileNames = os.listdir(img_src)
np.random.shuffle(allFileNames)
data = np.array(allFileNames)
train_num = int(len(allFileNames)*0.8)
train_FileNames, val_FileNames = data[:train_num], data[train_num:]
# print(train_FileNames, val_FileNames )

# write annotation
with open('./datasets/TWStreet/annotations/train.txt', 'w') as fw:
    for name in train_FileNames:
        fw.write('../datasets/TWStreet/images/train/'+name+'\n')
with open('./datasets/TWStreet/annotations/val.txt', 'w') as fw:
    for name in val_FileNames:
        fw.write('../datasets/TWStreet/images/val/'+name+'\n')

train_labels = [yologt+'/' +
                name.split('.')[0]+".txt" for name in train_FileNames.tolist()]
val_labels = [yologt+'/' +
              name.split('.')[0]+".txt" for name in val_FileNames.tolist()]
train_FileNames = [img_src+'/' + name for name in train_FileNames.tolist()]
val_FileNames = [img_src+'/' + name for name in val_FileNames.tolist()]


print('Total images: ', len(allFileNames))
print('Training: ', len(train_FileNames))
print('Validation: ', len(val_FileNames))

# Copy-pasting labels , images
for name in train_labels:
    shutil.copy(name, labels_dir + '/train')
for name in val_labels:
    shutil.copy(name, labels_dir + '/val')

for name in train_FileNames:
    shutil.copy(name, root_dir + '/train')
for name in val_FileNames:
    shutil.copy(name, root_dir + '/val')
