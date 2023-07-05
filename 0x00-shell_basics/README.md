* `pwd` : a script that prints the absolute path name of the current working directory.
* `ls` : a script that displays the contents list of your current directory.
* `cd`: a script that changes the working directory to the user’s home directory.
* `ls -l` : a script that displays current directory contents in a long format.
* `ls -la`: a script that displays current directory contents, including hidden files (starting with (.)). Use the long format.
* `ls -na`: a script that displays current directory contents(Long format, with user and group IDs displayed numerically and hidden files (starting with .).
* `mkdir /tmp/my_first_directory`: a script that creates a directory named my_first_directory in the /tmp/ directory.
* `mv /tmp/betty /tmp/my_first_directory`: a script that moves the file betty from /tmp/ to /tmp/my_first_directory.
* `rm /tmp/my_first_directory/betty`: a script that deletes the file betty in /tmp/my_first_directory.
* `rm -r /tmp/my_first_directory`: a script that deletes the directory my_first_directory that is in the /tmp directory.
* `cd -`: a script that changes the working directory to the previous one.
* `ls -la . .. /boot`: a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
* `file tmp/iamafile`: a script that prints the type of the file named iamafile.
* `ln -s /bin/ls __ls__`: a script that creates a symbolic link to /bin/ls, named __ls__.
* `cp -u *.html ../`: a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
* `mv [[:upper::]]* /tmp/u`: a script that moves all files beginning with an uppercase letter to the directory /tmp/u.
* `rm *~`: a script that deletes all files in the current working directory that end with the character ~.
* `mkdir -p welcome/to/school`: a script that creates the directories welcome/, welcome/to/, and welcome/to/school in the current directory.
* `ls -pam`: a script that lists all the files and directories of the current directory, separated by commas (,).
