#!/bin/bash

check_dir(){
	if [ -d "base_images" ]; then
		cd "base_images"
		return 0
	else
			return 1
	fi
}

check_for_zip() {
	if binwalk "$1" | grep "Zip" > /dev/null ; then
		7z x "$1"
		return 0
	fi
	return 1
}

check_for_zip "$1"

check_dir

for i in {2..20}
do 
	if check_for_zip $i"_c.jpg"; then
		if check_dir; then
			echo "in" $i"_c.jpg"
		else
			echo "done"
			cat flag.txt
			break
		fi
	fi
done