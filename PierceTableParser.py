#Developed By Carick Brandt 2/2023
import pdfplumber
import pandas as pd
import ChangeFileName

Page1Settings = {
    "vertical_strategy" : "text",
    "horizontal_strategy" : "text",
    "snap_y_tolerance" : 6,
    "min_words_vertical" : 2,
    "text_tolerance": 10
}

PageXSettings = {
    "vertical_strategy" : "explicit",
    "horizontal_strategy" : "text",
    "explicit_vertical_lines": [30, 80, 200, 270, 375, 440, 510, 570],
    "snap_y_tolerance" : 6,
    "min_words_vertical" : 2,
    "text_tolerance": 10,
}

BiggerTableSettings = {
    "vertical_strategy" : "explicit",
    "horizontal_strategy" : "text",
    "explicit_vertical_lines": [30, 80, 188, 260, 370, 440, 510, 570],
    "snap_y_tolerance" : 6,
    "min_words_vertical" : 2,
    "text_tolerance": 10
}

def Parse(FileName):
    Frames = []
    with pdfplumber.open(FileName) as pdf:
       for Page in pdf.pages:
            if Page.page_number == 1:
                Table = Page.extract_table(Page1Settings)
                df = pd.DataFrame(Table[1:], columns=Table[0])
                df = df.drop(index=len(df.index)-1)
                df = df.reset_index(drop=True)
                #print(df)
                Frames.append(df)
            else:
                Table = Page.extract_table(PageXSettings)
                df = pd.DataFrame(Table[1:], columns=Table[0])
                df = df.drop(index=len(df.index)-1)
                df = df.reset_index(drop=True)
                #print(df)
                Frames.append(df)
    Result = pd.concat(Frames)
    Result.drop_duplicates(inplace=True)
    Result.drop(index=0, inplace=True)
    # if parcel number is not an int like 7742200232 then drop it
    Result = Result[Result['Parcel'].str.isnumeric()]
    Result = Result.reset_index(drop=True)
    NewFile = ChangeFileName.ChangeFileNamePierceTableParse(FileName)
    print(NewFile)
    Result.to_csv(NewFile)
    print("Created: " + NewFile)
    print(Result)

#Slightly Bigger Table
def ParseBiggerTable(FileName):
    Frames = []
    with pdfplumber.open(FileName) as pdf:
       for Page in pdf.pages:
            if Page.page_number == 1:
                Table = Page.extract_table(BiggerTableSettings)
                df = pd.DataFrame(Table[2:], columns=Table[2])
                df = df.drop(index=len(df.index)-2)
                df = df.reset_index(drop=True)
                #print(df)
                Frames.append(df)
            else:
                Table = Page.extract_table(BiggerTableSettings)
                df = pd.DataFrame(Table[1:], columns=Table[0])
                df = df.drop(index=len(df.index)-1)
                df = df.reset_index(drop=True)
                #print(df)
                Frames.append(df)
    Result = pd.concat(Frames)
    Result.drop_duplicates(inplace=True)
    Result.drop(index=[0, 1], inplace=True)
    # if parcel number is not an int like 7742200232 then drop it
    Result = Result[Result['Parcel'].str.isnumeric()]
    Result.reset_index(drop=True, inplace=True)
    NewFile = ChangeFileName.ChangeFileNamePierceTableParse(FileName)
    print(NewFile)
    Result.to_csv(NewFile)
    print("Created: " + NewFile)
    print(Result)
