#Developed By Carick Brandt 2/2023
import re

def ChangeFileNamePierceWebList(FileName: str):
    core_re = re.compile(r'\d{18}')
    ListNumber = core_re.findall(FileName)
    NewFileName = "D:\WashingtonBot\CSV\Pierce\\" + "Pierce-" + FileName[11:11] + ListNumber[0] +  ".csv"
    return NewFileName

def ChangeFileNamePierceTableParse(FileName: str):
    NewFileName = "D:\WashingtonBot\CSV\Pierce\\" + FileName[28:-4] + ".csv"
    return NewFileName
