---
title: Assignment - Introduction to Bash
author: Sara
---
The folder Assignment-data contains datasets you need to work with. Here is the scenario:
Meg is a biomedical engineering student whose project entails collecting EEG recordings and other information from subjects.
She has created a folder for each subject which include below files:
- the raw recordings which are split in 10 minutes chunks and depending the length of the session with the subject there can be a few files that are named in increasing numbers:
e.g. data.ncs, data01.ncs, data02.ncs, ...
- a few photos in Jpeg format from the EEG head cap on the subject (1.Jpeg, 2.Jpeg, 3.Jpeg, ...)
- one txt file in which she writes notes during each specific experiments
- one spreadsheet file (.csv) with the subject demographic information
Since she arranged to have more than one subject on experiment days, the template she has for folder name is date-number: e.g. 20190912-0, 20190912-1 for the first and second subjects of the date 2019 09 12 respectively.
note: the number of EEG data files and photos are different in each folder.


Help her do the following tasks in Bash efficiently:
## 1
Copy all the folders' contents except the Jpegs to another location (e.g. another drive dedicated to data analysis hence not needing the photos)

## 2
She was not consistent in naming the note files during the experiments, and sometimes even forgot to make a note.
Help her to document which folders miss a note file.
Repeat the same for the demographic spreadsheet.

## 3
Rename all the note text files to this template: notes.txt

## 4
Over the course of a few months, she gradually copied her experiment data from the PC in the examination room on an external hard drive.
She wants to do a final check that there is in fact a copy of all the folders in the hard drive. Help her compare the list of all the folders across the main computer and the hard drive.


# Answers:
Below are only one alternative of the required tasks could be done:  
We start the terminal in Desktop, with the Assignment-data folder copied there:
## 1
to copy all files over except selected type

`cp -r assignment-data assignment-data-backup`

`rm -r assignment-data-backup/*/*.jpg`

## 2
to find which folders miss a certain type of file

`cd assignment-data`

`comm -3 <(find */*note* -printf '%h\n') <(find * -type d)`

# 3
to change names to a certain template

`for f in 2018*; do cd $f; mv *not* note.txt; cd ..; done`

# 4
to compare what two directories contain

`cd ..`

`comm -3 <(ls assignment-data) <(ls assignment-data-backup)`
