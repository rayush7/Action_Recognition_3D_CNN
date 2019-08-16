import pandas as pd 
import numpy as np 
import os
import sys
import shutil

def move_videos(source_folder,target_folder):
	for path, subdirs, files in os.walk(source_folder):
		for name in files:
			source_name = os.path.join(path, name)
			target_name = os.path.join(target_folder,name)

			#print('source name: ', source_name)
			#print('target_name: ', target_name)

			shutil.copy(source_name, target_name) 

def main():
	source_folder = '/home/ayush/Activity_Recognition/Action-Recognition/data/UCF-101/'
	target_folder = '/home/ayush/Activity_Recognition/3DCNN/UCF101/'

	move_videos(source_folder,target_folder)

	print('Finished Copying!!')

if __name__ == '__main__':
	main()