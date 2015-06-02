#!/usr/bin/python

import sys
import os
import subprocess
import filecmp

#argument 1 contains the directory 1
parentFolder_1 = sys.argv[1]

#argument 2 contains the directory 2
parentFolder_2 = sys.argv[2]

#walk through the tree structure of files (directory)
for dirName_1, subdirs_1, fileList_1 in os.walk(parentFolder_1):
	print('Scanning %s...' % dirName_1)
	#walk through the files in a directory
	for filename_1 in fileList_1:
		# Get the path to the file1
		path_1 = os.path.join(dirName_1, filename_1)
		#walk through the tree structure of files (directory)
		for dirName_2, subdirs_2, fileList_2 in os.walk(parentFolder_2):
			print('Scanning %s...' % dirName_2)
			#walk through the files in a directory
			for filename_2 in fileList_2:
				# Get the path to the file2
				path_2 = os.path.join(dirName_2, filename_2)
				# Checking if file path is different
				if path_1 != path_2:
				#Compare contents of both the files
					compResult = filecmp.cmp(path_1, path_2)   
					if compResult == True:
						print('Files %s and %s have same content' %(path_1, path_2))
						print('Press 1 to delete %s' %path_1)
						print('Press 2 to delete %s' %path_2)
						print('Press 3 to continue')
						print('Press 0 to exit')
						var = raw_input()
						if int(var) == 1:
							os.remove(path_1)
							#break to move ahead by one file in outer for loop as path1 file was deleted
							break
						elif int(var) == 2:
							os.remove(path_2)
						elif int(var) == 3:
							continue
						else:
							exit()
