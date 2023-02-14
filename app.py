#Developed By Carick Brandt 2/2023
import os
import time
import SnohomishParser
import PierceWebListParser
import PierceTableParser
import SkagitTableParser

Menu_Options = {
    1: "Pierce County",
    2: "Snohomish County",
    3: "Skagit County",
    4: "Quit"
}

# Skagit County Data Parser
def Skagit():
    print("Skagit County Data Parser.")
    # Find all the pdfs in PDF/Skagit Folder
    for FileName in os.listdir("D:\WashingtonBot\PDF\Skagit"):
        if FileName.endswith("pdf"):
            File = "D:\WashingtonBot\PDF\Skagit\\" + FileName
            print(File)
            try:
                SkagitTableParser.Parse(File)
                print("\n")
            except:
                print("Skagit Ran into an error.\n")
                continue

# Snohomish County Data Parser
def Snohomish():
    print("Snohomish County Data Parser.")
    # Find all the pdfs in PDF/Snohomish
    for FileName in os.listdir("D:\WashingtonBot\PDF\Snohomish"):
        if FileName.endswith("txt"):
            File = "D:\WashingtonBot\PDF\Snohomish\\" + FileName
            print(File)
            try:
                SnohomishParser.Type1(File=File)
                print("\n")
            except:
                print("Was not the first known type of Snohomish County \nTrying Next Known Format")
                time.sleep(2)
                try:
                    SnohomishParser.Type2(File=File)
                    print("\n")
                except:
                    print("Unknown Format of File")
                    time.sleep(2)
                    continue
                continue

# Pierce County Data Parser
def Pierce():
    print("Pierce County Data Parser.")
    # Find all the pdfs in PDF/Pierce
    for FileName in os.listdir("D:\WashingtonBot\PDF\Pierce"):
        if FileName.endswith("pdf"):
            File = "D:\WashingtonBot\PDF\Pierce\\" + FileName
            print(File)
            print("Converting List.")
            time.sleep(2)
            try:
                PierceWebListParser.Run(File)
            except:
                print("Not a WebList Trying next known format.")
                time.sleep(2)
                PierceTableParser.Parse(File)
                continue



def Automated():
    print("Tax Collection Data Parser")
    print("Files in PDF Folder must start with a Capital Letter to prevent issues with the windows file system.")
    print("If File Start with a Number such as '2022 WebList' Add any uppercase letter before 2022.")
    print("Example\n 2022 WebList.pdf -> A2022Weblist.pdf")
    print("PDF Folder can be found in C:\\Users\\caric\\WashingtonBot\\PDF")
    print("Open each file and check to see if you can highlight text in the pdf.")
    print("If the file cant be highlighted please open it in google docs and download it as a .txt file")
    print("Contact CarickBrandt@gmail.com if you have any questions or technical issues")
    next = input("Press Enter to start the automation process")
    for FileName in os.listdir("C:\\Users\\caric\\WashingtonBot\\PDF"):
        File = "C:\\Users\\caric\\WashingtonBot\\PDF\\" + FileName
        if File.endswith("pdf"):
            print(File)
            try:
                SkagitTableParser.Parse(File)
            except:
                try:
                    PierceTableParser.Parse(File)
                except:
                    try:
                        PierceWebListParser.Run(File)
                    except:
                        print("Unknown Format")
        time.sleep(4)
        if File.endswith("txt"):
            print(File)
            try:
                SnohomishParser.Type1(File)
            except:
                try:
                    SnohomishParser.Type2(File)
                except:
                    print("Unknown Format")
        time.sleep(4)


          


# Start Menu and loop till quit
def Menu():
    Active = True
    while(Active):
        Option = 0
        print("Washington State File Parser")
        print("Files in PDF Folder must start with a Capital Letter to prevent issues with the windows file system.")
        print("If File Start with a Number such as '2022 WebList' Add any uppercase letter before 2022.")
        print("Example\n 2022 WebList.pdf -> A2022Weblist.pdf")
        print("__________________________ ")
        for Key in Menu_Options.keys():
            if Key == 1:
                print("|          MENU          |")
                print("| ", Key, "--", Menu_Options[Key], "   |")
            if Key == 2:
                print("| ", Key, '--', Menu_Options[Key], "|")
            if Key == 3:
                print("| ", Key, '--', Menu_Options[Key], "   |")
            if Key == 4:
                print("| ", Key, '--', Menu_Options[Key], "            |")
                print("|________________________| ")
        Option = int(input("Enter you Choice: "))
        if Option == 1:
            try:
                print("Pierce County requires the PDF Files to be inserted into the PDF\Pierce folder. 3\nThe Resulting CSV files can be found in CSV\Pierce folder.")
                Next = input("press Enter to continue.")
                Pierce()
                Next = input("press Enter to continue.")
            except:
                print("Pierce Encounted Error.\n")
                Next = input("press Enter to continue.")
                continue
        if Option == 2:
            try:
                print("Snohomish requires you to throw the pdf into google drive. \nOpen the file using google docs and delete all of the pages before the first APN.")
                print("Then Download the file as a .txt from google drive using the drop down and put the file into the Folder PDF\Snohomish.")
                print("The CSV file can be found in the folder CSV\Snohomish.")
                Next = input("press Enter to continue.")
                Snohomish()
                Next = input("press Enter to continue.")
            except:
                print("Snohomish Encountered Error.\n")
                Next = input("press Enter to continue.")
                continue       
        if Option == 3:
            try:
                print("Skagit County requires the PDF Files to be inserted into the PDF\Skagit folder.\n The Resulting CSV files can be found in CSV\Skagit folder.")
                Next = input("press Enter to continue.")
                Skagit()
                Next = input("press Enter to continue.")
            except:
                print("Skagit Encountered Error\n")
                Next = input("press Enter to continue.\n")
                continue
        if Option == 4:
            Active = False
    exit()

#Menu()
Automated()