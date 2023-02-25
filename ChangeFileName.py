#Developed By Carick Brandt 2/2023
import os
import re
import time

working_directory = os.getcwd()

def ChangeFileNamePierceWebList(FileName: str):
    core_re = re.compile(r'\d{18}')
    ListNumber = core_re.findall(FileName)
    NewFileName: str = working_directory + "/CSV/" + "Pierce-" + FileName[11:11] + ListNumber[0] + ".csv"
    FileName = NewFileName
    return FileName

def ChangeFileNamePierceTableParse(FileName: str):
    NewFileName: str = working_directory + "/CSV/" + FileName[33:-4] + ".csv"
    FileName = NewFileName
    return FileName

def ChangeFileNameSkagitTableParse(FileName: str):
    NewFileName: str = working_directory + "/CSV/" + FileName[34:-4] + ".csv"
    FileName = NewFileName
    return FileName

# Change the SnohomishType1 File Name like the following using wokring_directory:
# "C:\\Users\\caric\\WashingtonBot\\CSV\\SnohomishCountyType2-" + time.strftime("%m-%d-%Y-%H-%M") + ".csv"
def ChangeFileNameSnohomishType1():
    NewFileName: str = working_directory + "/CSV/SnohomishCountyType2-" + time.strftime("%m-%d-%Y-%H-%M") + ".csv"
    return NewFileName

def ChangeFileNameSnohomishType2():
    NewFileName: str = working_directory + "/CSV/SnohomishCountyType2-" + time.strftime("%m-%d-%Y-%H-%M") + ".csv"
    return NewFileName


