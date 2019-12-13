# QualCoder
QualCoder is a qualitative data analysis application written in python3 and pyqt5.

QualCoder projects are stored in a Sqlite database. Text files can be typed in manually or loaded from txt, odt, docx, epub and  pdf files. Images, video and audio can also be imported for coding. Codes can be assigned to text, images and a/v selections and grouped into categories in hierarchical fashion. Various types of reports can be produced including visual coding graphs, coder comparisons and coding frequencies.

This project has been tested under Ubuntu, Linux Mint 18 and Windows 10, partly tested on Lubuntu 16. It has not been throughly tested on Mac OS.
Instructions and other information are available here: https://qualcoder.wordpress.com/ and on the Github Wiki.

## INSTALLATION
You will need to have a python3.x version installed.
You will also need to have a vlc player installed - for audio and video. 

### Linux:

You can install the latest debian package from (https://github.com/ccbogel/QualCoder-Debians)[https://github.com/ccbogel/QualCoder-Debians]

You might need to run this command from the terminal for pdf importing:

`sudo pip install pdfminer.six`

If not using the debian pacakge:

Make the install.sh executable and run the install.sh script from the terminal. Make sure the qualcoder folder is in the same directory as the install.sh script (i.e. as it appears when you download the QualCoder-master folder). 

`./install.sh`

The qualcoder folder should be in the same directory as the install.sh script.

This will install QualCoder in the /usr/share directory and create a launcher. Alternatively move to the qualcoder directory and run the qualcoder.py file in a terminal: python3 qualcoder.py

### Windows: 

Install [Python3](https://www.python.org/downloads/) and [VLC](https://www.videolan.org/vlc/download-windows.html) or from the Windows Store. On Windows, the bit version of VLC, 32 or 64 must match the bit version of python 3.

Install dependencies in the command prompt:

`python -m pip install pyqt5 lxml Pillow ebooklib ply chardet pikepdf pdfminer.six`

To launch, you can create a shortcut to the qualcoder.py file to start QualCoder.

Alternatively move to the qualcoder directory and run the qualcoder.py file in a terminal: python3 qualcoder.py


### MacOS

Install [Python3](https://www.python.org/downloads/) and [VLC](https://www.videolan.org/vlc/).

Install the Python dependencies using `pip`:

`pip install pyqt5 lxml pillow six ebooklib ply chardet pikepdf pdfminer.six`

There is no desktop icon launch right now for QualCoder. Open a new Terminal window in the directory and launch with `python qualcoder.py`.

Another option is shown here [https://www.maketecheasier.com/run-python-script-in-mac/](https://www.maketecheasier.com/run-python-script-in-mac/). This means you can right-click on the qualcoder.py file and open with --> python launcher.
 You can make an alias to the file and place it on your desktop.
 
## Dependencies
Required

* Python 3.x version

* PyQt5

* lxml

* Pillow

* six

* eboklib

* ply

* chardet

* pikepdf

* pdfminer.six

* vlc

## Issues
* Testing has mostly been performed on Ubuntu, Linux Mint and Windows 10. Some usage conducted with Lubuntu and Apple MacOSX.

## Future plans
* Reports:
    * Word count report
    * Possibly look at text mining
* Text mining
    * word cloud, word visualisations
* General
    * Translations for GUI (some translations in Gernam and French).

## License
QualCoder is distributed under the MIT LICENSE.

## Debian packages
See [https://github.com/ccbogel/QualCoder-Debians](https://github.com/ccbogel/QualCoder-Debians)
