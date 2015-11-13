\+DatabaseType ELAN
\ver 5.0
\desc ELAN
\+mkrset 
\lngDefault English
\mkrRecord id

\+mkr ELANBegin
\nam ELANBegin
\desc The beginning timecode of the section in the recording that is transcribed.
\lng Default
\mkrOverThis ref
\-mkr

\+mkr ELANEnd
\nam ELANEnd
\desc The ending timecode of the segment in the recording being transcribed.
\lng Default
\mkrOverThis ref
\-mkr

\+mkr ELANMediaMIME
\nam ELANMediaMIME
\desc The ELANMedia field for the reference marker in export to ELAN.
\lng Default
\mkrOverThis ref
\-mkr

\+mkr ELANMediaMiME
\nam ELANMediaID
\desc The ELANMediaMIME field for the \id field in ELAN export.
\lng English
\mkrOverThis id
\-mkr

\+mkr ELANMediaURL
\nam ELANMediaURL
\desc The ELAN url for linked media.
\lng Default
\mkrOverThis ref
\-mkr

\+mkr ELANParticipant
\nam ELANParticipant
\desc The participant identification marker for ELAN export.
\lng Default
\mkrOverThis ref
\-mkr

\+mkr ft
\nam Free Translation
\desc Free translation of the referenced text unit. This is not used or modified during interlinearization. It is information to clarify the meaning of the text.
\lng English
\mkrOverThis ref
\mkrFollowingThis ref
\-mkr

\+mkr ftso
\nam *
\lng English
\mkrOverThis id
\-mkr

\+mkr ftthere
\nam *
\lng English
\mkrOverThis id
\-mkr

\+mkr ge
\nam Gloss
\desc English gloss of each morpheme in the morpheme breaks line.
\lng English
\mkrOverThis ph
\-mkr

\+mkr id
\nam Text Name
\desc Identifying name for the text in this record.
\lng English
\-mkr

\+mkr mb
\nam Morphemes
\desc Source text unit divided into morphemes.
\lng vernacular
\mkrOverThis tx
\-mkr

\+mkr nt
\nam Notes
\desc Notes on the referenced text unit. Useful for explanation, clarification, questions, etc.
\lng English
\mkrOverThis ref
\-mkr

\+mkr nt.'
\nam *
\lng English
\mkrOverThis id
\-mkr

\+mkr nt..'
\nam *
\lng English
\mkrOverThis id
\-mkr

\+mkr ph
\nam phonetic
\lng Default
\mkrOverThis mb
\-mkr

\+mkr ps
\nam Part of Speech
\desc Part of speech of each morpheme in the morpheme breaks line.
\lng English
\+fnt 
\Name Times New Roman
\Size 11
\Italic
\charset 00
\rgbColor 0,0,0
\-fnt
\mkrOverThis tx
\-mkr

\+mkr ref
\nam Reference
\desc Reference for the following text unit. References are used for word list and concordance, plus other purposes.  A reference usually consists of a short abbreviation of the text name, followed by a dot and a number. Text numbering and renumbering automatically update references in this form.
\lng English
\mkrOverThis id
\mkrFollowingThis tx
\-mkr

\+mkr sound
\nam Soundfile
\desc This line contains the name of the linked sound file and accompanying in and out points of the transcribed segment.
\lng English
\mkrOverThis id
\-mkr

\+mkr tx
\nam Text
\desc Source text unit for interlinearization. Usually a sentence or clause. After interlinearization there may be multiple text lines in a referenced text unit.
\lng vernacular
\mkrOverThis ref
\-mkr

\+mkr tx.'
\nam *
\lng English
\mkrOverThis id
\-mkr

\-mkrset

\iInterlinCharWd 8

\+intprclst 
\fglst {
\fglend }
\mbnd +
\mbrks -=

\+intprc Lookup
\bParseProc
\mkrFrom tx
\mkrTo mb

\+triLook 
\+drflst 
\-drflst
\-triLook

\+triPref 
\dbtyp MDF 4.0
\+drflst 
\+drf 
\File C:\ToolboxFiles\Pnar\Dictionary.txt
\-drf
\-drflst
\+mrflst 
\mkr lx
\mkr a
\-mrflst
\mkrOut lx
\-triPref

\+triRoot 
\dbtyp MDF 4.0
\+drflst 
\+drf 
\File C:\ToolboxFiles\Pnar\Dictionary.txt
\-drf
\-drflst
\+mrflst 
\mkr lx
\mkr a
\-mrflst
\mkrOut lx
\-triRoot
\GlossSeparator ;
\FailMark *
\bShowFailMark
\bShowRootGuess
\bPreferPrefix
\+wdfset 
\wdfPrimary Word
\+wdf Word
\+wdplst 
\wdp loc name
\wdp loc loc
\wdp loc n
\wdp loc clitic
\wdp clitic n
\wdp clitic hon
\wdp der v
\wdp der English
\wdp der aspect
\wdp clitic nmz v
\wdp case clitic deixis
\wdp case clitic v
\wdp case clitic n
\wdp case loc
\wdp der prefix v
\wdp clitic n v
\wdp clitic deixis
\wdp clitic name
\wdp clitic num
\wdp clitic English
\wdp clitic Hindi
\wdp clitic nmz prefix v
\wdp v deixis
\wdp v mod
\wdp mod
\wdp adv
\wdp nmz v
\wdp name
\wdp mood
\wdp aspect
\wdp n
\wdp v
\wdp case
\wdp conf
\wdp clitic
\wdp num
\wdp nm asp v
\wdp exc
\wdp conj clitic
\wdp conj
\wdp pn def
\wdp loc def
\wdp clitic def
\-wdplst
\-wdf
\lngPatterns vernacular
\-wdfset
\-intprc

\+intprc Lookup
\mkrFrom mb
\mkrTo ph

\+triLook 
\dbtyp MDF 4.0
\+drflst 
\+drf 
\File C:\ToolboxFiles\Pnar\Dictionary.txt
\-drf
\-drflst
\+mrflst 
\mkr lx
\-mrflst
\mkrOut ph
\-triLook
\GlossSeparator ;
\FailMark ***
\bShowFailMark
\bShowRootGuess
\-intprc

\+intprc Lookup
\mkrFrom mb
\mkrTo ge

\+triLook 
\dbtyp MDF 4.0
\+drflst 
\+drf 
\File C:\ToolboxFiles\Pnar\Dictionary.txt
\-drf
\-drflst
\+mrflst 
\mkr lx
\-mrflst
\mkrOut ge
\-triLook
\GlossSeparator ;
\FailMark ***
\bShowFailMark
\bShowRootGuess
\-intprc

\+intprc Lookup
\mkrFrom mb
\mkrTo ps

\+triLook 
\dbtyp MDF 4.0
\+drflst 
\+drf 
\File C:\ToolboxFiles\Pnar\Dictionary.txt
\-drf
\-drflst
\+mrflst 
\mkr lx
\-mrflst
\mkrOut ps
\-triLook
\GlossSeparator ;
\FailMark ***
\bShowFailMark
\bShowRootGuess
\-intprc

\-intprclst
\+filset 

\-filset

\+jmpset 
\+jmp Morphemes
\+mkrsubsetIncluded 
\mkr mb
\mkr tx
\-mkrsubsetIncluded
\+drflst 
\+drf 
\File C:\ToolboxFiles\Pnar\Dictionary.txt
\mkr lx
\-drf
\+drf 
\File C:\ToolboxFiles\Pnar\Dictionary.txt
\mkr a
\-drf
\-drflst
\match_char p
\-jmp
\-jmpset

\+template 
\fld \ref
\fld \tx
\-template
\mkrRecord id
\mkrTextRef ref
\+PrintProperties 
\header File: &f, Date: &d
\footer Page &p
\topmargin 1.00 in
\leftmargin 0.25 in
\bottommargin 1.00 in
\rightmargin 0.25 in
\recordsspace 10
\-PrintProperties
\+expset 

\+expSF Id-Ref-Sound-Tx-Ft-Nt
\exportedFile C:\ToolboxFiles\Pnar\New Texts X.txt
\+mkrsubsetIncluded 
\mkr ELANBegin
\mkr ELANEnd
\mkr ELANMediaMIME
\mkr ELANMediaMiME
\mkr ELANMediaURL
\mkr ELANParticipant
\mkr ft
\mkr id
\mkr nt
\mkr ref
\mkr sound
\mkr tx
\-mkrsubsetIncluded
\-expSF

\+expRTF Notes and ID
\exportedFile C:\ToolboxFiles\Pnar\Notes3.rtf
\InterlinearSpacing 120
\+mkrsubsetIncluded 
\mkr id
\mkr nt
\-mkrsubsetIncluded
\+rtfPageSetup 
\paperSize letter
\topMargin 1
\bottomMargin 1
\leftMargin 1.25
\rightMargin 1.25
\gutter 0
\headerToEdge 0.5
\footerToEdge 0.5
\columns 1
\columnSpacing 0.5
\-rtfPageSetup
\-expRTF

\+expRTF Rich Text Format
\InterlinearSpacing 120
\+rtfPageSetup 
\paperSize letter
\topMargin 1
\bottomMargin 1
\leftMargin 1.25
\rightMargin 1.25
\gutter 0
\headerToEdge 0.5
\footerToEdge 0.5
\columns 1
\columnSpacing 0.5
\-rtfPageSetup
\-expRTF

\+expSF Standard Format
\exportedFile C:\ToolboxFiles\Pnar\Exported Texts\MPearStoryRetellingJowai.txt
\OverwriteOutputFile
\-expSF

\+expSF TX field only
\exportedFile A:\PNAR\TX only
\+mkrsubsetIncluded 
\mkr tx
\-mkrsubsetIncluded
\-expSF

\+expSF Text and Translation
\exportedFile C:\ToolboxFiles\Pnar\Settings\Export of text and translation.txt
\+mkrsubsetIncluded 
\mkr ft
\mkr tx
\-mkrsubsetIncluded
\-expSF

\+expRTF Text and translation
\exportedFile A:\PNAR\HeadmanHistoryRaliang.rtf
\InterlinearSpaceAligned
\+mkrsubsetIncluded 
\mkr ft
\mkr ge
\mkr tx
\-mkrsubsetIncluded
\+rtfPageSetup 
\paperSize letter
\topMargin 1
\bottomMargin 1
\leftMargin 1.25
\rightMargin 1.25
\gutter 0
\headerToEdge 0.5
\footerToEdge 0.5
\columns 1
\columnSpacing 0.5
\-rtfPageSetup
\-expRTF

\expDefault Standard Format
\CurrentRecord
\-expset
\+numbering 
\mkrRef ref
\mkrTxt tx
\+subsetTextBreakMarkers 
\+mkrsubsetIncluded 
\mkr tx
\-mkrsubsetIncluded
\-subsetTextBreakMarkers
\-numbering
\-DatabaseType
