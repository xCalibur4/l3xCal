# Base version of file (Original File) = file_name.base
# Version control metadata(Contains deletions/appends from Base) = file_name.info
# Usage: python svc.py file_name	 <- commit 
#		 python svc.py file_name 3   <- Display version 3 of file_name

import sys
import os.path
import shutil

def main():
	arg_list = [x for x in sys.argv]

	if len(arg_list) != 2 and len(arg_list) != 3:
		sys.exit("Usage:\n python svc.py file_name <--- commit\n python svc.py file_name 3 <--- Display version 3")

	file_name = arg_list[1]
	base_filename = file_name + ".base"
	vc_filename = file_name + ".info"

	if len(arg_list) == 3:
		# Load version X

		version = int(arg_list[2])
		op = load_version(base_filename, vc_filename, version)
		print op,
	else:
		# Commit file

		current_file = open(file_name)
		str_current_file = current_file.read()

		#print "1\n" + str_current_file,

		if os.path.isfile(base_filename) == True :
			# Found base version. Thus file has been committed before.

			vc_info_file = open(vc_filename,"a")

			# Load the latest commit
			str_last_commit_file = load_version(base_filename, vc_filename, float("inf"))

			#print "2\n" + str_last_commit_file,

			# Match final commit with the file being committed
			if str_last_commit_file == str_current_file:
				sys.exit("\n----This file has not been modified since last commit. No changes to save.----\n")
			else:
				# File changed. Commit changes.
				append_versionControl(str_last_commit_file, str_current_file, vc_info_file)

			vc_info_file.close()
		else:
			# This is the first time the file is being committed. Create base.

			# Create base file
			shutil.copyfile(file_name,base_filename)
			# Create version control info file
			vc_info_file = open(vc_filename,"w")
			vc_info_file.write("*\n")
			vc_info_file.close()

		current_file.close()




# Add changes from last commit to vc file(basically save this new version)
# Arguments = str, str, file obj
def append_versionControl(str_last_commit, str_current, vc):
	#print "3\n" + str_current,
	#print "4\n" + str(len(str_last_commit)), str(len(str_current))

	if len(str_last_commit) < len(str_current):
		# Length of file has increased, thus file has been appended to.
		appended_line = str_current.split('\n')[-1]
		if appended_line == '':
			appended_line = str_current.split('\n')[-2]
		vc.write("a " + appended_line + "\n")
	else:
		# Line has been deleted
		last_commit_lines = str_last_commit.split('\n')
		if last_commit_lines[-1] == '':
			del last_commit_lines[-1]
		current_lines = str_current.split('\n')
		if current_lines[-1] == '':
			del current_lines[-1]
		i = 0
		for line in current_lines:
			if line != last_commit_lines[i] :
				vc.write("d " + str(i) + "\n")
				break
			i += 1

# Loads version v of the file and returns it as a string
def load_version(base_filename, vc_filename, v):
	base_file = open(base_filename)
	vc_file = open(vc_filename)
	list_base_lines = base_file.readlines()
	i = 1
	for line in vc_file:
		if line == "*\n":
			continue
		if i == v:
			break
		if line[0] == 'd':
			# Delete line X from base
			del list_base_lines[int(line.split(' ')[1])]
		else:
			# Append line to base
			list_base_lines.append(line[2:])
		i += 1
	final_commit = ''
	for line in list_base_lines:
		final_commit += line
	return final_commit



if __name__ == '__main__':
    main()