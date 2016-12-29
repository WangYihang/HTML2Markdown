#!/usr/bin/env python
# coding:utf-8

import requests
import sys


def getScriptFileName():
    return sys.argv[0].split("/")[-1]


def showHelp():
    print "Usage : "
    print "\tpython " + getScriptFileName() + " input.html output.html"
    print "\tpython " + getScriptFileName() + " \"http://www.wangyihang.net/index.html\" output.html"


def checkInput():
    if len(sys.argv) != 3:
        showHelp()
        exit(1)
    else:
        return (sys.argv[1], sys.argv[2])


def main():
    print checkInput()


if __name__ == '__main__':
    main()
