import glob
import os
import sys
import shutil
import re

downloadsFolder = "/mnt/f/Downloads"

for file in os.listdir(downloadsFolder):
	if file.endswith(".mkv"):
		animeVideo = downloadsFolder + "/" + file
		animeFolder = downloadsFolder + "/Anime" 
		animeTitle = re.sub("\\[HorribleSubs\\]","", file)
		animeTitle = re.sub("-.*", "", animeTitle)
		animeTitle = re.sub("^\\s", "", animeTitle)
		animeSeries = animeFolder + "/" + animeTitle
		print (animeSeries)
		if os.path.isdir(animeSeries): 
			shutil.move(animeVideo, animeSeries)
		else:
			os.mkdir(animeFolder + "/" + animeTitle)
			shutil.move(animeVideo, animeSeries)
