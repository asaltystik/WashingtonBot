#Developed By Carick Brandt 2/2023
import pdfplumber
import pandas as pd

def Parse(File):
    # Open the pdf with pdfplumber
    with pdfplumber.open(File) as pdf:
        Frames = []
        for Page in pdf.pages:
            Table = Page.extract_table()
            df = pd.DataFrame(Table[1:], columns=["Parcel Number", "Owners", "Assessed Value", "Physical Address Property Description", "Estimated Minimum Bid"])
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)
            print(df)
            Frames.append(df)
        Result = pd.concat(Frames)
        NewFileName = "D:\WashingtonBot\CSV\Skagit\\"+File[28:-4] + ".csv"
        print(NewFileName)
        Result.to_csv(NewFileName)
        print("Created File: " + NewFileName + '\n')
