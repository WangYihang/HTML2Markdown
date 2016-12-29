#!/usr/bin/env python
# coding:utf-8

import requests
import sys


def getScriptFileName():
    return sys.argv[0].split("/")[-1]


def isUrl(fileName):
    return ("/" in fileName)


def showHelp():
    scriptFileName = getScriptFileName()
    print "Usage : "
    print "\tpython " + scriptFileName + " input.html output.html"
    print "\tpython " + scriptFileName,
    print " \"http://www.wangyihang.net/index.html\" output.html"


def checkInput():
    if len(sys.argv) != 3:
        showHelp()
        exit(1)
    else:
        return (sys.argv[1], sys.argv[2])


def createFileNameByUrl(url):
    if url.endswith("/"):
        return "index.html"
    else:
        return url.split("/")[-1]


def downloadFile(url):
    response = requests.get(url)
    fileName = createFileNameByUrl(url)
    with open(fileName, "w") as file:
        file.write(response.content)
    return fileName


def convert(content):
    markdown = ""
    return markdown


def writeFile(fileName, content):
    file = open(fileName, "w")
    file.write(content)
    file.close()


def getContentOfFile(fileName):
    return open(fileName).read()


def getRealFileName(fileName):
    temp = fileName.split(".")[0:-1]
    result = ""
    for segment in temp:
        result += segment
    return result


def getMarkdownFileName(realFileName):
    return realFileName + ".md"


def main():
    (inputFile, outputFile) = checkInput()
    fileName = ""
    if isUrl(inputFile):
        fileName = downloadFile(inputFile)
    else:
        fileName = inputFile
    content = getContentOfFile(fileName)
    markdownContent = convert(content)
    writeFile(getMarkdownFileName(getRealFileName(fileName)), markdownContent)


if __name__ == '__main__':
    main()
