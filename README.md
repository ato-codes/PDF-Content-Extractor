# PDF Content Extractor

. Project based simple python code for extracting contents of given pdf file. Based on [PyPDF2](https://pypi.org/project/PyPDF2/) module.

. if [PyPDF2](https://pypi.org/project/PyPDF2/) is not installed you can install it through this code from the options.


## . Instructions

1. PDF Files that needed to be extracted must be putted on on the folder named ```pdf-files``` in the root folder of the code. (it comes with sample pdf files in it)

2. Then in terminal type
```bash
$ python main.py
```

3. Then Choose the options given by the output

> you can find the extracted pdf files in the root folder Named ```Extracted\pdfFileName```

## . Extracted PDF File Structure

```
|- Extracted/
|   |-PDFFileName1/
|   |   |-Images/
|   |   |   |-pdfImage1.png
|   |   |   |-pdfImage2.png
|   |   |
|   |   |-file_info.json
|   |   |-pdfFileName2.txt
|   |   |   
|   |-PDFFileName2/
|   |   |-Images/
|   |   |   |-pdfImage1.png
|   |   |   |-pdfImage2.png
|   |   |
|   |   |-file_info.json
|   |   |-pdfFileName2.txt
|   |   
└──
```

. Every Images on the pdf file will be stored on `Extracted/PDFFileName/Images/` folder

. `pdfFileName.txt` : Contains all the text inside the pdf

. `file_info.json` : the json contains the pdf information like the `author`,`title`,`pages` and `images` extracted from the pdf.
