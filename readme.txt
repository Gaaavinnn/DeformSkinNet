In the DefomSkinNet folder, create a new file directory:
|---dataset
	|---train
		|---images
		|---labels
	|---val
		|---images
		|---labels
The data set is divided according to the ratio of training set to verification set 8:2. 
The images go into the images folder, and the labels file in txt format goes into the labels folder.

Use command python train.py to start train.