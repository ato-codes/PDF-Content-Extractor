import os
import json
import platform
import pkg_resources

extractedPathName = os.getcwd() + "\\Extracted"
pdfPath = "./pdf-files"    

# todo: installRequiredModules
def installPreRequestModules(run=False):
    if (run == True):
        os.system("pip install PyPDF2 PyPDF2[image]")
        pdfExtraction()
    else:
        os.system("pip install PyPDF2 PyPDF2[image]")

# todo: check and install PyPDF2 if not installed 
def checkAndInstallRequiredModule():
    installedModules = [installedModule for installedModule in pkg_resources.working_set if installedModule.project_name == "pypdf2"]
    if len(installedModules) == 0:
        installPreRequestModules(run=True)       
        return 


def pdfExtraction():

    from PyPDF2 import PdfReader

    print("-"*50 + "\n")  # ? Decoration

    # todo: creating Folder For Extracted Contents
    if os.path.exists(extractedPathName) == False:
        os.mkdir(os.path.realpath(extractedPathName))

    pdfFiles = [pdfFile for pdfFile in os.listdir(
        pdfPath) if ".pdf" in pdfFile]
    countPdfFile = 1

    # todo: Extraction...
    for pdfFile in pdfFiles:
        print(f"Extracting {pdfFile}....")

        folderName = str(pdfFile).replace(".", "")
        extractedFolderName = extractedPathName + f"\\{folderName}"
        extractedImagesPath = extractedFolderName + "\\Images"
        textFileName = f"{extractedFolderName}\\{folderName}.txt"
        pdfJsonFile = extractedFolderName + "\\file_info.json"

        if os.path.exists(extractedFolderName) == False:
            os.mkdir(extractedFolderName)
            os.mkdir(extractedImagesPath)

        reader = PdfReader(f"{os.getcwd()}\\{pdfPath}\\{pdfFile}")
        
        metadata = reader.metadata
        fileInfoDictionary = {
            "countImages": 0,  # ? total Images in pdf
            "countPages": len(reader.pages),  # ? total Pages in pdf
            "title": metadata.title,
            "author": metadata.author,
            "content": "",
        }

        for page in range(fileInfoDictionary["countPages"]):
            textContent = reader.pages[page].extract_text()
            images = reader.pages[page].images
            for image in images:  # todo: Extracting And Saving images
                with open(f"{extractedImagesPath}\\{image.name}", "wb") as pageImage:
                    pageImage.write(image.data)
                fileInfoDictionary["countImages"] += 1  # total Images in pdf

            fileInfoDictionary["content"] += f"{textContent}\n"

        with open(pdfJsonFile, "w", encoding="utf-8") as jsonFile:
            json.dump(fileInfoDictionary, jsonFile,
                      ensure_ascii=True, indent=6)
        with open(textFileName, "w", encoding="utf-8") as textFile:
            textFile.write(fileInfoDictionary["content"])

        print("Completed")
        print(f"\tConverting {countPdfFile}/{len(pdfFiles)}\n")
        countPdfFile += 1

    print("-"*50 + "\n")  # ? Decoration
    print(
        f"Extraction Completed {countPdfFile - 1}/{len(pdfFiles)}\nYou Can Find Extracted Files In\n=> {extractedPathName}")

# todo: options 
def prompt():
    print("\nPDF Content Extractor\n")
    print("-"*50)  # ? Decoration
    print(
        """
        NB: all Your PDF Files you wish to EXTRACT must be in \"pdf-files\" folder specified 
        in the root folder of the code
        If NOT CREATE ONE WITH THE SAME NAME
        """)
    print("-"*50 + "\n")  # ? Decoration

    print(
        """1.Install Pre Request Modules And Run Code
        \n2.Start Extraction
        \n3.Exit\n"""
    )
    try:
        selectedEnv = input("Enter Option Number: ")
    except KeyboardInterrupt:
        return

    try:
        number = int(selectedEnv)
    except ValueError:
        print("\nIncorrect Value\nTry Again")
        prompt()

    if number == 1:
        try:
            installPreRequestModules(run=True)
        except KeyboardInterrupt:
            return
    elif number == 2:
        try:
            pdfExtraction()
        except KeyboardInterrupt:
            return
    elif number == 3:
        return


def main():
    if os.path.exists(pdfPath) == False:
        os.mkdir(pdfPath)
    checkAndInstallRequiredModule()
    prompt()


main()
