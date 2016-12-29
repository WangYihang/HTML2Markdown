#!/usr/bin/env python
# coding:utf-8

import requests
import sys
import bs4


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


def handle_ul(soup):
    al_all = soup.findAll("ul")
    for al in al_all:
        li_all = al.findAll("li")
        for li in li_all:
            print "* " + str(li.contents)


def handle_ol(soup):
    al_all = soup.findAll("ol")
    for al in al_all:
        li_all = al.findAll("li")
        for li in li_all:
            print "* " + str(li.contents)


def handle_h1(soup):
    h1s = soup.findAll("h1")
    for h1 in h1s:
        print "# " + str(h1.contents)
    return ""


def handle_h2(soup):
    h2s = soup.findAll("h2")
    for h2 in h2s:
        print "## " + str(h2.contents)
    return ""


def handle_h3(soup):
    h3s = soup.findAll("h3")
    for h3 in h3s:
        print "### " + str(h3.contents)
    return ""


def handle_h4(soup):
    h4s = soup.findAll("h4")
    for h4 in h4s:
        print "#### " + str(h4.contents)
    return ""


def handle_h5(soup):
    h5s = soup.findAll("h5")
    for h5 in h5s:
        print "##### " + str(h5.contents)
    return ""


def handle_em(soup):
    ems = soup.findAll("em")
    for em in ems:
        print "*" + str(em.contents) + "*"
    return ""


def handle_strong(soup):
    strongs = soup.findAll("strong")
    for strong in strongs:
        print "**" + str(strong.contents) + "**"
    return ""


def handle_img(soup):
    imgs = soup.findAll("img")
    for img in imgs:
        describe = ""
        if img.has_attr('alt'):
            describe = img['alt']
        else:
            describe = "Picture"
        print "![" + describe + "](" + img['src'] + ")"
    return ""


def handle_code(soup):
    codes = soup.findAll("code")
    for code in codes:
        # deault one tag only has one attr
        if code.has_attr('class'):
            if code['class'][0] == "prettyprint":
                print "`" + str(code.contents) + "`"
            else:
                print "```\r\n" + str(code.contents) + "\r\n```"
        else:
            print "```\r\n" + str(code.contents) + "\r\n```"
    return ""


def handle_blockquote(soup):
    blockquotes = soup.findAll("blockquote")
    for blockquote in blockquotes:
        for line in blockquote:
            lineContent = str(line)
            if len(lineContent) == 0:
                continue
            elif len(lineContent) < 2:
                if lineContent == "\n":
                    continue
                if lineContent == "\r":
                    continue
                if lineContent == "\r\n":
                    continue
            else:
                for line in lineContent.split("\n"):
                    print "> " + line
    return ""


def handle_hr(soup):
    blockquotes = soup.findAll("blockquote")
    for blockquote in blockquotes:
        print "\r\n-\r\n"
    return ""


def convert(content):
    markdown = ""
    soup = bs4.BeautifulSoup(content, "html.parser")
    print "-----------------"
    handle_ul(soup)
    print "-----------------"
    handle_ol(soup)
    print "-----------------"
    handle_h1(soup)
    print "-----------------"
    handle_h2(soup)
    print "-----------------"
    handle_h3(soup)
    print "-----------------"
    handle_h4(soup)
    print "-----------------"
    handle_h5(soup)
    print "-----------------"
    handle_em(soup)
    print "-----------------"
    handle_strong(soup)
    print "-----------------"
    handle_img(soup)
    print "-----------------"
    handle_code(soup)
    print "-----------------"
    handle_blockquote(soup)
    print "-----------------"
    handle_hr(soup)
    return markdown


def appendLineToFile(fileName, line):
    file = open(fileName, "a+")
    file.write(line + "\r\n")
    file.close()


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
