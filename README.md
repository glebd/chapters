# Chapters

This is a command-line utility to convert file containing YouTube chapters into Audacity Labels format.

YouTube-style chapter markers have timestamps in the format `mm:ss text`, but Audacity expects timestamps as float values.

The workflow is as follows:

* Add chapter markers to your DaVinci Resolve project
* Export YouTube chapters to a text file from DaVinci Resolve using [the script created by Roger Magnusson](https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=149311)
* Convert the chapters text file to Audacity Labels format
* Load the audio file into Audacity
* Load the labels file into Audacity as a Labels track
* Export WAV with labels from Audacity
* Import and convert the WAV file to MP3 using [Forecast by Marco Arment](https://overcast.fm/forecast)
