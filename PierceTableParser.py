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

def Parse(FileName):
    Frames = []
    with pdfplumber.open(FileName) as pdf:
       for Page in pdf.pages:
            if Page.page_number == 1:
                Table = Page.extract_table(Page1Settings)
                df = pd.DataFrame(Table[1:], columns=Table[0])
                df = df.drop(index=len(df.index)-1)
                df = df.reset_index(drop=True)
                Frames.append(df)
            else:
                Table = Page.extract_table(PageXSettings)
                df = pd.DataFrame(Table[1:], columns=Table[0])
                df = df.drop(index=len(df.index)-1)
                df = df.reset_index(drop=True)
                Frames.append(df)
    Result = pd.concat(Frames)
    Result = Result.drop_duplicates()
    Result = Result.drop(index=0)
    Result = Result.reset_index(drop=True)
    NewFile = ChangeFileName.ChangeFileNamePierceTableParse(FileName)
    print(NewFile)
    Result.to_csv(NewFile)
    print("Created: " + NewFile)
    print(Result)