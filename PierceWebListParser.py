#Developed By Carick Brandt on 2/2023
import pdfplumber
import re
import pandas as pd
import ChangeFileName


def Run(File: str):
    #Defualt Values
    Counter = 0
    APNFound = False
    Apn_re = re.compile(r'\d{10}')
    Name_re = re.compile(r"^([A-Z ':]+$)\b", re.M)
    Situs_re = re.compile(r"Situs:")
    Holders_re = re.compile(r"Lienholders:")
    Taxes_re = re.compile(r"Taxes:")
    Apn = []
    Names = []
    AddressList = []
    Holders = []
    TaxesOwed = []

    with pdfplumber.open(File) as pdf:
        for Page in pdf.pages:
            Text = Page.extract_text()
            for Line in Text.split('\n'):
                if Apn_re.match(Line):
                    Apn.append(Line)
                    #print("Found APN")
                    APNFound = True
                if Line.isupper() &  APNFound == True:
                    APNFound = False
                    #print("Found Name")
                    Names.append(Line)
                if Situs_re.match(Line):
                    if len(AddressList) < len(Apn):
                        AddressList.append(Line.replace("Situs: ", ""))
                        #print("Found Situs")
                if Holders_re.match(Line):
                    Holders.append(Line.replace("Lienholders: ", ""))
                    #print("Found Holder(s)")
                if len(Holders) < len(Apn):
                    Holders.append("")
                if Taxes_re.match(Line):
                    TaxesOwed.append(Line.replace("Taxes: ", ""))
                    #print("Found Taxes Owed")
                    #print(len(Apn))
    del Holders[0]
    df = pd.DataFrame({
            "APN" : Apn,
            "Name" : Names,
            "Address" : AddressList,
            "Lienholders" : Holders,
            "Taxes Owed" : TaxesOwed
    })
    
    NewFileName = ChangeFileName.ChangeFileNamePierceWebList(File)
    print(df)
    df.to_csv(NewFileName)
    print("Created File: " + NewFileName + '\n')