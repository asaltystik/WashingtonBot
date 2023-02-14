#Developed By Carick Brandt 2/2023
import pandas as pd
import re
import time

# Type 1 Formatting NO APN Identifier
def Type1(File: str):
    # Defining Regular expressions to find relevent data
    Index_RE = re.compile(r'\#\d+')
    IndexAPN_RE = re.compile(r'#\d+ (\d{14})')
    Apn_RE = re.compile(r'\d{14}')
    Name_RE = re.compile(r"Owner: (.*)")
    Situs_RE = re.compile(r"Situs: (.*)")
    Tca_RE = re.compile(r"TCA: (.*)")
    Size_RE = re.compile(r"Size: (.*)")
    LandValue_RE = re.compile(r"Land Value: (.*)")
    ImproveValue_RE = re.compile(r"Improvement Value: (.*)")
    AmountDue_RE = re.compile(r"Amount Due as of (.*): (.*)")

    # Defining Variables
    APNList = ["NotFound"]
    NamesList = []
    SitusList = []
    TCAList = []
    SizesList = []
    LandValueList = []
    IVList = []
    TaxesDueList = []
    Taxes = []
    DueDate = []
    AddressList = []
    CityList = []

    # Parse the given file and export it to csv format after cleaning
    Document = open(File, "r")
    Text = Document.read()
    NamesList = re.findall(Name_RE, Text)
    SitusList = re.findall(Situs_RE, Text)
    TCAList = re.findall(Tca_RE, Text)
    SizesList = re.findall(Size_RE, Text)
    LandValueList = re.findall(LandValue_RE, Text)
    IVList = re.findall(ImproveValue_RE, Text)
    TaxesDueList = re.findall(AmountDue_RE, Text)
    Index = 0
    for Line in Text.split("\n"):
        if Index_RE.match(Line):
            Index += 1
        if IndexAPN_RE.match(Line):
            APNList.append(Line)
        if Apn_RE.match(Line):
            APNList.append(Line)
    
    for Tax in TaxesDueList:
        Taxes.append(Tax[1])
        DueDate.append(Tax[0])
    for Address in SitusList:
        Split = re.split(r",\s", Address)
        if len(Split) > 1:
            AddressList.append(Split[0])
            CityList.append(Split[1])
        else:
            AddressList.append(Split[0])
            CityList.append("NA")
    CityList = [City.split(" TCA:")[0] for City in CityList]
    CityList = [City.replace('near ','').replace('on ','') for City in CityList]
    #Create Pandas Dataframe
    df = pd.DataFrame({
        "APN" : APNList,
        "Owner Name" : NamesList,
        "Address List"  : AddressList,
        "City" : CityList,
        "TCA" : TCAList, 
        "Size of Lot" : SizesList,
        "Land Value" : LandValueList,
        "Improvement Value" : IVList,
        "Taxes Due" : Taxes,
        "Due Date" : DueDate
    })
    df = df.drop(index=0)
    df = df.reset_index(drop=True)
    print(df)
    NewFileName = "C:\\Users\\caric\\WashingtonBot\\CSV\\SnohomishCountyType1-" + time.strftime("%m-%d-%Y-%H-%M") + ".csv"
    df.to_csv(NewFileName)
    print("Created: " + NewFileName)

# For Snohomish County that includes an APN Identifier
def Type2(File: str):
     # Defining Regular expressions to find relevent data
    Apn_RE = re.compile(r'APN: (\d{14})')
    Name_RE = re.compile(r"TAXPAYER/OWNER: (.*?),")
    Legal_RE = re.compile(r"Legal: (.*)")
    Situs_RE = re.compile(r"SITUS/local street address if known: (.*)")
    Tca_RE = re.compile(r"TCA: (.*)")
    Size_RE = re.compile(r"Size .*: (.*)")
    LandValue_RE = re.compile(r"Land Value: (.*)")
    ImproveValue_RE = re.compile(r"Improvement Value: (.*)")
    AmountDue_RE = re.compile(r"AMOUNT DUE as of (.*): (.*)")

    #Define Variables
    APNList = []
    NamesList = []
    LegalList = []
    SitusList = []
    TCAList = []
    SizesList = []
    LandValueList = []
    IVList = []
    TaxesDueList = []
    Taxes = []
    DueDate = []
    AddressList = []
    CityList = []
    
    # Parse the given file and export it to csv format after cleaning
    Document = open(File, "r")
    Text = Document.read()
    APNList = re.findall(Apn_RE, Text)
    NamesList = re.findall(Name_RE, Text)
    SitusList = re.findall(Situs_RE, Text)
    LegalList = re.findall(Legal_RE, Text)
    TCAList = re.findall(Tca_RE, Text)
    SizesList = re.findall(Size_RE, Text)
    LandValueList = re.findall(LandValue_RE, Text)
    IVList = re.findall(ImproveValue_RE, Text)
    TaxesDueList = re.findall(AmountDue_RE, Text)
    for Tax in TaxesDueList:
        Taxes.append(Tax[1])
        DueDate.append(Tax[0])
    
    for Address in SitusList:
        Split = re.split(r",\s", Address)
        if len(Split) > 1:
            AddressList.append(Split[0])
            CityList.append(Split[1])
        else:
            AddressList.append(Split[0])
            CityList.append("NA")
    SitusList.insert(0, "NA")
    AddressList.insert(0, "NA")
    CityList.insert(0, "NA")
    CityList = [City.split(" TCA:")[0] for City in CityList]
    #Create Pandas Dataframe
    df = pd.DataFrame({
        "APN" : APNList,
        "Owner Name" : NamesList,
        "TCA" : TCAList, 
        "Address" : AddressList,
        "City" : CityList,
        "Size of Lot" : SizesList,
        "Land Value" : LandValueList,
        "Improvement Value" : IVList,
        "Taxes Due" : Taxes,
        "Due Date" : DueDate
    })
    print(df)
    NewFileName = "C:\\Users\\caric\\WashingtonBot\\CSV\\SnohomishCountyType2-" + time.strftime("%m-%d-%Y-%H-%M") + ".csv" 
    df.to_csv(NewFileName)
    print("Created: " + NewFileName)
