import os
import sys
import googleVisionOCR
import dateExtraction
import dataTemplate

from os import listdir, mkdir
from os.path import isfile, join
from copy import deepcopy

def main(argv):
    filePath = sys.argv[1]

    googleVisionOCR.OCR(filePath)
    
    jsonPath = filePath + "\\GoogleVisionData\\"
    tempPath = filePath + "\\tempFiles\\"
    if not os.path.isdir(tempPath):
        os.mkdir(tempPath)

    emptyData = dataTemplate.data_template
    
    fileList = [f for f in listdir(jsonPath) if isfile(join(jsonPath, f))]
    for f in fileList:
        data = deepcopy(emptyData)
        dates = dateExtraction.extractDates(filePath + "\\GoogleVisionData\\" + f)
                
        for d in dates:
            data[d] = dates[d]
        
        # Add autofill modules here

        outputFilePath = tempPath + f.split(".")[0] + ".tmp"
        
        file = open(outputFilePath, "w+")
        
        file.write("")
        
        for i in data:
            file.write(i + ":" + data[i] + "\n")

        file.close()
                    
if __name__ == "__main__":
    main(sys.argv)
