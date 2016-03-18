# -*- coding: utf-8 -*-
# CC by 4.0 Hiram Ring, November 2015, www.hiramring.com, hiram1@e.ntu.edu.sg
# http://creativecommons.org/licenses/by/4.0/
# designed for making Toolbox .txt files from Transcriber .trs files
# for usage refer to the accompanying README.txt file
import glob
import datetime
import re
import io

config = io.open('trs2txt.cfg', 'r') # open the config file located in the same directory

ref = '' # create a blank string to store the 'ref' tag from the config file for processing
tbeg = '' # create a blank string to store the 'tbeg' tag from the config file for processing
tend = '' # create a blank string to store the 'tend' tag from the config file for processing
tpart = '\ELANParticipant ' # create a string to store the 'tpart' tag for processing
sound = '\sound ' # create a string to store the 'sound' tag for processing
audiostart = 'audio_filename="' # this string identifies the audio file in Transcriber
audioend = '" version="' # this string identifies the end of the audio file name
syncbeg = '<Sync time="' # this string identifies the beginning of each time-alignment
section = '<Section type="' # this string identifies the beginning of the file/section
turnbeg = '<Turn' # this string identifies the beginning of a speaker turn
speakstart = ' speaker="' # this string identifies the speaker
starttime = ' startTime="'  # this string identifies the beginning of a timecoded speaker's turn
startend = '" endTime="'  # this string identifies the end of a timecoded speaker's turn
speakend = '" startTime' # this string identifies the beginning of a timecoded speaker's turn in a slightly different format
syncend = '"/>' # this string identifies the end of a sync point
endtime = 'endTime="' # this string identifies the end of a timecoded speaker's turn in a slightly different format
endsep = '" '  # this string identifies a separated end
endings = '"' # this string identifies the end of a timecode
ver = '' # create a blank string to store the 'text' tag from the config file for processing
trans = '' # create a blank string to store the 'trans' tag from the config file for processing

for line in config: # read all the lines and look for the correct tags
    if line[0:18] == 'reference number: ': # read the reference number tag
        ref += line[18:-1]+' ' # append it to the 'ref' string
    if line[0:20] == 'timecode beginning: ': # read the tag that identifies the beginning of a timecode
        tbeg += line[20:-1]+' ' # append it to the 'tbeg' string
    if line[0:17] == 'timecode ending: ': # read the tag that identifies the end of a timecode
        tend += line[17:-1]+' ' # append it to the 'tend' string
    if line[0:29] == 'text for language subtitles: ': # read the tag that identifies the subtitles in the vernacular language
        ver += line[29:-1]+' ' # append it to the 'text' string
    if line[0:22] == 'text for translation: ': # read the tag that identifies the translation subtitles
        trans += line[22:-1]+' ' # append it to the 'trans' string

filenames = [] # create an empty list called 'filenames' to keep track of the .txt files in the directory

for index, file in enumerate(glob.glob("*.trs")): # use glob to create an enumerated list of the .txt files in the directory
    filenames.append(file) # append the names of the .txt files in the directory to a list

for infile in filenames: # create a 'for' loop to iterate through all the .txt files in the directory as listed in the 'filenames' list
    trsfile = open(infile,'r') # Open each .trs file in 'read' mode

    textfile = open(str(infile[0:-3])+'txt','w') # create a corresponding .txt file in 'write' mode to store the values we want from the .trs file

    count = 0 # create a count value to keep track of lists

    timecodes = [] # create a list value to keep track of timecodes
    speaker = [] # create a list value to keep track of speakers
    speakturn = '' # create a string value to keep track of speaker turns
    speakvalstart = [] # create a list value to keep track of speaker start times
    speakvalend = [] # create a list value to keep track of speaker end times
    lines = []  # create a list value to keep track of text lines

    textfile.write(str('\\_sh v3.0  400  ELAN\n\\_DateStampHasFourDigitYear\n\n')) # write the header of the Toolbox file

    for line in trsfile: # get all the lines we want from the .trs file and write them into a corresponding (new) .txt file
        try: # these 'try' loops are basically to ensure that if there are any lines that don't exist in the .trs file, they get ignored. Without these loops, those .trs files where different speakers weren't annotated would break the program.
            if audiostart in line: # get the filename for the audio
                result = re.search('%s(.*)%s' % (audiostart, audioend), line).group(1)
                audioname = result.replace(' ', '_') # replace spaces in the audio filename with underscores
                textfile.write('\\id '+result+'\n') # write the \id of the file using the audio filename
        except:
            pass
        try:
            if section in line: # get the endtime of the sound file
                complete = re.search('%s(.*)%s' % (endtime, endings), line).group(1) # story it in the 'complete' variable
        except:
            pass
        try:
            if turnbeg+starttime in line: # get the first speaker's turn
                spone = re.search('%s(.*)%s' % (starttime, endings+' '), line).group(1) # get the start of the speaker's turn
                speakvalstart.append(spone) # store it in a list
                sptwo = re.search('%s(.*)%s' % (endtime, endings+' '), line).group(1) # get the end of the speaker's turn
                speakvalend.append(sptwo) # store it in another list
                speak = re.search('%s(.*)%s' % (speakstart, endings+'>\n'), line).group(1) # get the name of the speaker
                speakturn = speak # set the current value of the string variable 'speakturn' to the speaker name
        except:
            pass
        try:
            if turnbeg+speakstart in line: # get a non-first speaker's turn
                speak = re.search('%s(.*)%s' % (speakstart, endings+' start'), line).group(1) # get the name of the speaker
                speakturn = speak # set the current value of the string variable 'speakturn' to the speaker name
                spone = re.search('%s(.*)%s' % (starttime, endings+' '), line).group(1) # get the start of the speaker's turn
                speakvalstart.append(spone) # store it in a list
                sptwo = re.search('%s(.*)%s' % (endtime, endings), line).group(1) # get the end of the speaker's turn
                speakvalend.append(sptwo) # store it in another list
        except:
            pass
        try:
            if '<Sync' in line: # if there is a sync point
                speaker.append(speakturn) # add the name of the speaker to the 'speaker' list - this ensures that every turn has a corresponding speaker name
        except:
            pass
        try:
            if syncbeg in line: # if there is a sync point
                sync = re.search('%s(.*)%s' % (syncbeg, syncend), line).group(1) # get the timecode
                timecodes.append(sync) # store it in the 'timecodes' list
        except:
            pass
        try:
            if '<' not in line: # if there is non-html tagged text, this is the text associated with a turn
                lines.append(line) # add it to the 'lines' list
        except:
            pass

    blue = len(timecodes)
    # count = 0

    for line in timecodes: # for each of the time-coded segments identified in the 'timecodes' list, do the following
        # count += 1

        # if blue != count+1:
        #     # print blue
        #     print count
        #     print timecodes[count]
        #     print len(lines)
        #     print ver
        #     print lines[count]
        #     count += 1
        # elif blue == count+1:
        #     print count
        #     print timecodes[count]
        #     print len(lines)
        #     print ver
        #     print lines[count]
            # print timecodes[blue]

        if blue != count+1: # if the counter number doesn't correspond to the number of the last timecode
            textfile.write(ref+audioname+'_'+str(count+1).zfill(3)+'\n') # write the 'ref' string and the modified file name
            textfile.write(tbeg+str(timecodes[count])+'\n') # write the 'tbeg' string and the first timecode
            textfile.write(tend+str(timecodes[count+1])+'\n') # write the 'tend' string and the second timecode
            textfile.write(tpart+speaker[count]+'\n') # write the 'tpart' string and the name of the speaker in this turn
            textfile.write(sound+audioname+'.wav '+str(timecodes[count])+' '+str(timecodes[count+1])+'\n') # write the 'sound' string and the name of the linked .wav file along with in and out points of the linked segment
            textfile.write(str(ver)+str(lines[count])) # write the 'ver' string and the corresponding line of text
            textfile.write(trans+'\n\n') # write the 'trans' line - this line will always be empty. If you have a corresponding free translation, you can copy it here in Toolbox
            count += 1 # advance the counter by 1
        elif blue == count+1: # if the counter number corresponds to the number of the last timecode
            textfile.write(ref+audioname+'_'+str(count+1).zfill(3)+'\n') # write the 'ref' string and the modified file name
            textfile.write(tbeg+str(timecodes[count])+'\n') # write the 'tbeg' string and the first timecode
            textfile.write(tend+str(complete)+'\n') # write the 'tend' string and the second timecode
            textfile.write(tpart+speaker[count-1]+'\n') # write the 'tpart' string and the name of the speaker in this turn
            textfile.write(sound+audioname+'.wav '+str(timecodes[count])+' '+str(complete)+'\n') # write the 'sound' string and the name of the linked .wav file along with in and out points of the linked segment
            textfile.write(str(ver)+str(lines[count])) # write the 'ver' string and the corresponding line of text
            textfile.write(trans+'\n\n') # write the 'trans' line - this line will always be empty. If you have a corresponding free translation, you can copy it here in Toolbox
    textfile.write('\ELANMediaURL '+audioname+'.wav\n'+'\ELANMediaMIME audio/x-wav'+'\n') # write the footer

    trsfile.close() # close the trsfile now that all the data has been written to the 'textlines' lists/database
    textfile.close() # close the textfile as well

# return to the head of the for loop and continue as long as there is a .trs file in the 'filenames' list
