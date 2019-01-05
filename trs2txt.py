# -*- coding: utf-8 -*-
# CC by 4.0 Hiram Ring, November 2015 & January 2019, www.hiramring.com, hiram1@e.ntu.edu.sg
# http://creativecommons.org/licenses/by/4.0/
# designed for making Toolbox .txt files from Transcriber .trs files
# for usage refer to the accompanying README.txt file
import glob
import datetime
import re
import os.path
import io

ref = '' # create a blank string to store the 'ref' tag from the config file for processing
tbeg = '' # create a blank string to store the 'tbeg' tag from the config file for processing
tend = '' # create a blank string to store the 'tend' tag from the config file for processing
tpart = '\\ELANParticipant ' # create a string to store the 'tpart' tag for processing
sound = '\\sound ' # create a string to store the 'sound' tag for processing
audiostart = 'audio_filename="' # this string identifies the audio file in Transcriber
syncbeg = '<Sync time="' # this string identifies the beginning of each time-alignment
section = '<Section ' # this string identifies the beginning of the file/section
turnbeg = '<Turn ' # this string identifies the beginning of a speaker turn
idtag = 'id="'
nametag = 'name="'
speakstart = 'speaker="' # this string identifies the speaker
endtime = 'endTime="' # this string identifies the end of a timecoded speaker's turn in a slightly different format
endings = '"' # this string identifies the end of a timecode
ver = '' # create a blank string to store the 'text' tag from the config file for processing
trans = '' # create a blank string to store the 'trans' tag from the config file for processing

configlist = []

if os.path.isfile("CONFIG"): # check if there is a CONFIG file
    config = io.open('CONFIG', 'r') # if so, open the config file located in the same directory (io.open)
    for line in config:
        configlist = line.split(' ')
        ref = str(configlist[0]) + ' '
        tbeg = str(configlist[1]) + ' '
        tend = str(configlist[2]) + ' '
        # tpart = str(configlist[3])
        ver = str(configlist[3]) + ' '
        trans = str(configlist[4]) + ' '
    config.close()
else: # if there is no CONFIG file, create one from user input
    print "There is no configuration file. You must add new tags.\n"
    ref = '\\' + raw_input("What is the reference number? (often 'ref') > ") + ' '
    tbeg = '\\' + raw_input("What marks the beginning of your timecodes? (often 'ELANBegin') > ") + ' '
    tend = '\\' + raw_input("What marks the end of your timecodes? (often 'ELANEnd') > ") + ' '
    # removed user input for participants, made ELANParticipant the default marker
    # tpart = '\\' + raw_input("How do you want your participants marked? (often 'ELANParticipant') > ")
    ver = '\\' + raw_input("What marks a string of vernacular text? (often 'tx') > ") + ' '
    trans = '\\' + raw_input("What marks your free translation? (often 'ft') > ") + ' '
    config = open('CONFIG', 'w')
    config.write(ref + tbeg + tend + ver + trans)
    config.close()

filenames = [] # create an empty list called 'filenames' to keep track of the .trs/txt files in the directory

for index, file in enumerate(glob.glob("*.trs")): # use glob to create an enumerated list of the .trs files in the directory
    filenames.append(file) # append the names of the .trs files in the directory to a list

for infile in filenames: # create a 'for' loop to iterate through all the .trs files in the directory as listed in the 'filenames' list
    # Some of the files have blank carriage returns in the transcription, which is
    # only a problem if the carriage returns accompany an existing transcription
    # tagged to a timecode. The following code cleans this up by replacing the
    # excess newlines.
    tempfile = open(infile) # open the file
    contents = tempfile.read() # read it as text
    # print(contents)
    s = re.compile(r'(?<!\>)\n\n', re.DOTALL) # use regex across double newlines not preceded by a '>' character (ending html bracket)
    temptrs = re.sub(s, "\n", contents) # replace double newlines
    temptext = open(str(infile),'w') # write over the original trs file
    temptext.write(temptrs) # replace the contents with the new find/replaced contents
    temptext.close() # close the file we're writing to
    tempfile.close() # close the tempfile we stored data in

    # the newly cleaned trs files can now be opened
    trsfile = open(infile,'r') # Open each .trs file in 'read' mode
    textfile = open(str(infile[0:-3])+'txt','w') # create a corresponding .txt file in 'write' mode to store the values we want from the .trs file

    count = 0 # create a count value to keep track of lists
    b_count = 0 # create a count value to keep track of sync points

    b_timecodes = [] # create a list value to keep track of beginning timecodes
    e_timecodes = [] # create a list to keep track of ending timecodes
    speakdict = {} # create a dict to keep track of spaker tags and names
    speaker = [] # create a list value to keep track of speakers
    speak = '' # create a string value to keep track of speakers
    speaklist = [] # create a list to keep track of speakers within turns
    spend = '' # create a string to keep track of speaker ending turns
    sync = '' # create a string to keep track of sync points
    complete = '' # create a string to keep track of the final sync point
    lines = []  # create a list value to keep track of text lines

    textfile.write(str('\\_sh v3.0  400  ELAN\n\\_DateStampHasFourDigitYear\n\n')) # write the header of the Toolbox file
    # The following loop finds relevant tags and stores speaker information
    # along with timecodes and speech in several lists which are then used to
    # create a new Toolbox file. It uses regex to find the information rather
    # than an xml reader since the xml created by Transcriber has non-closed tags.
    for line in trsfile: # get all the lines we want from the .trs file and write them into a corresponding (new) .txt file
        # these 'try' loops are basically to ensure that if there are any lines that don't exist in the .trs file, they get ignored. Without these loops, those .trs files where different speakers weren't annotated would break the program.
        try: # this loop attempts to create a dictionary of speakers
            if '<Speaker ' in line:
                sptag = re.search('%s(.*?)%s' % (idtag, endings), line).group(1) # get the tag
                spname = re.search('%s(.*?)%s' % (nametag, endings), line).group(1) # get the name
                speakdict[sptag] = spname # create a dict entry with the tag as the key and name as value
        except:
            pass
        try: # this loop attempts to identify the audio filename, used for the 'id' field
            if audiostart in line: # get the filename for the audio
                result = re.search('%s(.*?)%s' % (audiostart, endings), line).group(1) # get the filename
                print(result) # print the filename of the current file being processed
                audioname = result.replace(' ', '_') # replace spaces in the audio filename with underscores
                textfile.write('\\id '+result+'\n') # write the \id of the file using the audio filename
        except:
            pass
        try: # this loop attempts to identify the length of the sound file (used for the final ending timecode)
            if section in line: # get the endtime of the sound file
                complete = re.search('%s(.*?)%s' % (endtime, endings), line).group(1) # store it in the 'complete' variable
                # complete = complete.replace('\"', '')
        except:
            pass
        try: # this loop identifies the speakers within turns
            if turnbeg in line: # check if the line marks the beginning of a turn
                speaklist = [] # if so, recreate a blank list to track the speakers
                speak = re.search('%s(.*?)%s' % (speakstart, endings), line).group(1) # get the name of the speaker
                # print(speak)
                spend = re.search('%s(.*?)%s' % (endtime, endings), line).group(1) # get the end of the speaker's turn
                if len(speak.split(' ')) > 1: # check if there is more than one speaker
                    for spl in speak.split(' '): # if so
                        speaklist.append(spl) # append each speaker to the recreated blank list, which is retained throughout the turn
                else: # otherwise
                    speaklist.append(speak) # append the single speaker to the list
        except:
            pass
        try: # this loop identifies timecodes and assigns speakers to each timecode
            if syncbeg in line: # if there is a sync point
                sync = re.search('%s(.*?)%s' % (syncbeg, endings), line).group(1) # get the timecode
                # print(speaklist)
                if len(speaklist) > 0: # if there is more than one speaker in the list of speakers
                    pass # do nothing
                else: # otherwise
                    speaklist = ['unknown_speaker'] # recreate the list with an unknown speaker
                speaker.append(speaklist[0]) # append the first speaker in the temporary turn list to the list of speakers
                b_timecodes.append(sync) # append the timecode of the sync point to the list of beginning timecodes
                if b_count > 0: # if the syncpoint counts are after the first one
                    e_timecodes.append(sync) # append the timecode to the list of ending timecodes
                b_count += 1 # increment the syncpoint counts by 1
        except:
            pass
        try: # this loop identifies multiple speakers in overlapping turns (currently supports up to 5 speakers)
            if '<Who nb="2' in line: # if there is an overlap with a second speaker
                speaker.append(speaklist[1]) # append the second speaker to the list
                b_timecodes.append(sync) # append the same timecode to the beginning timecodes list
                e_timecodes.append(spend) # append the speaker ending timecode to the list
            elif '<Who nb="3' in line: # if there is an overlap with a third speaker
                speaker.append(speaklist[2]) # append the third speaker to the list
                b_timecodes.append(sync) # append the same timecode to the beginning timecodes list
                e_timecodes.append(spend) # append the speaker ending timecode to the list
            elif '<Who nb="4' in line: # if there is an overlap with a fourth speaker
                speaker.append(speaklist[3]) # append the fourth speaker to the list
                b_timecodes.append(sync) # append the same timecode to the beginning timecodes list
                e_timecodes.append(spend) # append the speaker ending timecode to the list
            elif '<Who nb="5' in line: # if there is an overlap with a fifth speaker
                speaker.append(speaklist[4]) # append the fifth speaker to the list
                b_timecodes.append(sync) # append the same timecode to the beginning timecodes list
                e_timecodes.append(spend) # append the speaker ending timecode to the list
            else:
                pass
        except:
            pass
        try: # this loop identifies speech tagged to sync points
            if '<' not in line: # if there is non-html tagged text, this is the text associated with a turn
                lines.append(line) # add it to the 'lines' list
        except:
            pass

    e_timecodes.append(complete)

    for num, item in enumerate(speaker): # go through the list of speakers
        if item in speakdict: # check if the speaker is in the dictionary of nametags
            speaker[num] = speakdict[item] # if so, replace it with the name
        else:
            pass

    # Print some information for each file
    print("number of speaker turns", len(speaker))
    print("number of beginning timecodes", len(b_timecodes))
    print("number of ending timecodes", len(e_timecodes))
    print("number of speech lines", len(lines))
    print(lines[-1])

    # use the code below for testing
    # for num, item in enumerate(speaker, 0):
    #     print(num, item, b_timecodes[num], e_timecodes[num], lines[num])

    for num, item in enumerate(speaker, 0): # for each of the time-coded segments identified in the 'speaker' list, do the following
        textfile.write(ref+audioname+'.'+str(num+1).zfill(3)+'\n') # write the 'ref' string and the modified file name
        textfile.write(tbeg+str(b_timecodes[num])+'\n') # write the 'tbeg' string and the first timecode
        textfile.write(tend+str(e_timecodes[num])+'\n') # write the 'tend' string and the second timecode
        textfile.write(tpart+speaker[num]+'\n') # write the 'tpart' string and the name of the speaker in this turn
        textfile.write(sound+audioname+'.wav '+str(b_timecodes[num])+' '+str(e_timecodes[num])+'\n') # write the 'sound' string and the name of the linked .wav file along with in and out points of the linked segment
        textfile.write(str(ver)+str(lines[num])) # write the 'ver' string and the corresponding line of text
        textfile.write(trans+'\n\n') # write the 'trans' line - this line will always be empty. If you have a corresponding free translation, you can copy it here in Toolbox
    textfile.write('\ELANMediaURL '+audioname+'.wav\n'+'\ELANMediaMIME audio/x-wav'+'\n') # write the footer

    trsfile.close() # close the trsfile now that all the data has been written to the 'textlines' lists/database
    textfile.close() # close the textfile as well

# return to the head of the for loop and continue as long as there is a .trs file in the 'filenames' list
