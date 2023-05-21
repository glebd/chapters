# Chapters

This is a command-line utility to convert files containing YouTube chapters into other formats.

YouTube-style chapter markers have timestamps in the format `mm:ss text`, but Audacity expects
timestamps as float values, and [Podcast Chapters](https://chaptersapp.com/) needs a CSV file
with each line in the format `Title,timestamp`.

My workflow is as follows:

* Add chapter markers to DaVinci Resolve project
* Export MP3 (CBR) from DaVinci Resolve
* Export YouTube chapters to a text file from DaVinci Resolve using 
  [the script](https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=149311) created by
  Roger Magnusson
* Convert the chapters text file to CSV format
* Load the MP3 file into Podcast Chapters.
* Import chapters CSV file into Podcast Chapters.
* Export MP3 with chapters from Podcast Chapters.
