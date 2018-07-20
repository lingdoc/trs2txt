### README for `trs2txt` python script and executable
Version 1.2
CC by 4.0 Hiram Ring, 2015-2018, www.hiramring.com, hiram1@e.ntu.edu.sg
http://creativecommons.org/licenses/by/4.0/

Freely available for use, distribution, and modification

This README.txt file is intended to be copied along with the `trs2txt` python script and executable file.

This folder contains the following files:

* `ELAN.typ` (a database file that Toolbox requires to understand the markers)
* `README.md` (this readme file)
* `Ring-The_trs2txt_script.pdf` (a PDF file explaining the usage of the script in more detail)
* `trs2txt.exe` (the executable script file)
* `trs2txt.py` (the Python script from which the executable is built)

*** CHANGES SINCE 1.1 ***

The `trs2txt.cfg` file is deprecated in favor of a program-internal creation of the configuration file. This allows users to input necessary markers for each field the first time they run the converter in a new folder. To reset the configuration, simply delete the `CONFIG` file that the converter creates.

### About

The script is inspired by Andrew Margetts' online converter (http://linguisticsoftwareconverters.zong.mine.nu/) and is designed for making Toolbox `.txt` files (http://www-01.sil.org/computing/toolbox/) from Transcriber 1.5.1 `.trs` files (http://sourceforge.net/projects/trans/files/transcriber/1.5.1/) to allow users to play segments of long sound files from within Toolbox. When the program runs for the first time, it will prompt users to create a  `CONFIG` file which will subsequently determine the markers in the Toolbox files. For example, to use the `\ref` marker for the Toolbox reference line, enter `ref` (without the backslash) at the relevant command prompt. To reset the markers, delete the `CONFIG` file. Typical Toolbox markers are given below:
 * `\ref` (line name and number)
 * `\ELANBegin` (timecode beginning)
 * `\ELANEnd` (timecode ending)
 * `\t` (vernacular text - Toolbox default is `\tx`)
 * `\f` (free translation - Toolbox default is `\ft`)

These markers should also correspond to the descriptions in the `ELAN.typ` file (a sample file is included in the `.zip`). The `ELAN.typ` file should be placed in your Toolbox project settings folder. Other markers and information that will be added are the linked sound file and participant turn information. Participant turn information will only be populated if such information is available in your Transcriber file. Otherwise this entry will be left blank - you can add this information manually in Toolbox. This information is used by ELAN to import Toolbox interlinear texts.

To use the script, run it in a directory that contains your Transcriber `.trs` files. The script/executable will create a corresponding `.txt` file for each `.trs` file in the directory, using the configuration file as a guide. Existing .txt files will be overwritten. To import the texts into Toolbox you can open each text file in a text editor, copy the content (from the header `\id` to the end) and paste it into your Toolbox `Texts.txt` file.

To play the sound file from your Toolbox project, the sound file should be in the same directory as the texts. It may be possible to put the file in a separate folder within your projects directory, and change all the paths in the generated Toolbox file, though I have not tried this.

Things to note:
1. The script populates the `\id`, `\ref`, `\ELANParticipant` and `\sound` fields (as well as the timecode information) directly from the linked file in your Transcriber session. It is a good idea to save the Transcriber timecoded file in the same directory as your sound file in order to avoid having to find/replace more information in the resulting text file.
2. Toolbox does not seem to support spaces in directory names or soundfile names, so the script replaces all spaces in a linked filename with underscores (`_`). This may mean that you will have to rename your sound file(s). Currently the script replaces no other characters, so other characters which may break Toolbox compatibility should be replaced via a find/replace command in your text editor of choice.
3. Toolbox does not support sound formats other than .WAV - since it is generally bad practice in linguistics to record in formats other than .wav, I consider this a non-issue. In the case of non-wav formats I recommend converting the file to .wav before time-aligning in Transcriber.
4. This script treats all time-aligned text as belonging to the `\tx` (`\t`) line. However, it adds an `\ft` (`\f`) line to the resulting Toolbox .txt file to facilitate easy adding of this information. If you have a file with both vernacular text and free translation, you can leave it all on the same line in your Transcriber time-alignment, and simply copy-paste from the `\tx` line to the `\ft` once it is in Toolbox.
