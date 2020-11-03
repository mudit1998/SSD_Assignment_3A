# Assignment 3b:
### link for git : https://github.com/mudit1998/SSD_Assignment_3A
### I had done all my code on ubuntu 20.04  and used VS code as editor.
### Used python3
### Output for q2 is in `output_2.txt` and for q3 is in `output_3.txt`
## q1:(CHANGES FROM 3a: Taken loop for taking input instead of taking 2 input directly and then taking 2 at a time and find a `leaders child` which will be again taken as 1 input with other from user and in this way finally at end our answer will be leader of our emplyeeid which we found from loop)
### * Taken name(id) as `integer`in json as mentioned in question as it should be in range `001-999`
### * If any of the input is of `level 0` then output shown would be `leader not found`
### * In all other cases , found the `closest leader` which is common among them.
### * First input is number of employee for which we have to find our leader and the other are the employee id's.
### * All input are taken from `input()` only as specified.

## q2:(CHANGES FROM 3a: Taken command line argument for 2 different format which was not in 3a and the check for command line argument if it is `dd/mm/yyyy` then only implemented my previous code and in case of `mm/dd/yyyy` made changes to gather correct date month and year and for no argument case everything is same as previous 3a code)
### * Taken input from `date_calculator.txt` and found the `absolute` difference in days among them.
### * Command line argument is provided to specify that our format is  `dd/mm/yyyy` or `mm/dd/yyyy` and for other case `no command line` argument will be provided.
### * For one of the input format  used `3 letters of words` for every month.
### * Used `import sys` for getting command line argument.

## q3:(CHANGES FROM 3a: Taken an employee folder which contain as many file as we want instead of only 2 which is implemented in 3a and then find common free slot taking all into consideration)
### * Seperate `employee folder` is created and all the `employee text files` are contained in it.
### * Converted in `json format` and then parse json.
### * For time from 9 to 1(excluding 1) input is taken as  for example `09:00AM` and for 1 to 5 it is taken as `1:00PM` like this.
### * If `Dates` are not equal in input format then simply output in file that `no slot since dates are different`
### * Used `import os` for getting all files from our new directory `employee`.

