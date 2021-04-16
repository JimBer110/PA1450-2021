"""Main module of the application"""

from argparse import ArgumentParser

import case

import os

from application.commands import serve, greet

def main():
    """Main method of the application."""
    # Create an argument parser for parsing CLI arguments
    parser = ArgumentParser(description="An example application")
    # Create collection of subparsers, one for each command such as "download"
    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True 

    # Add the parser for each specific command
    serve.create_parser(subparsers)
    greet.create_parser(subparsers)
    
    # Parse the arguments and execute the chosen command
    options = parser.parse_args()
    options.command(options)

    cases = []
    for fileName in os.listdir(os.path.dirname(__file__)+"/covid_case_data/"):
        with open(os.path.dirname(__file__)+"/covid_case_data/"+fileName) as f:
            for line in f:
                covid_case=splitLine(line)
                cases.append(case.Case(covid_case[0],covid_case[1],covid_case[2],covid_case[3],covid_case[4],covid_case[5],covid_case[6],covid_case[7],covid_case[8],covid_case[9],covid_case[10],covid_case[11],covid_case[12],covid_case[13]))
    print(len(cases))
    
def splitLine(lines):
    if(lines.find('"')!=-1):
        newlist = lines.split(",")
        newlist[len(newlist)-1]=newlist[len(newlist)-1].rstrip("\n")
        index= []

        for word in range(len(newlist)):
            if(newlist[word].find('"')!=-1):
                index.append(word)
                newlist[word]=newlist[word].replace('"',"")
                
        while (len(index)>0):
            newlist[index[-2]:index[-1]+1]=[''.join(newlist[index[-2]:index[-1]+1])]
            index.pop(-1)
            index.pop(-1)

    else:
        newlist = lines.split(",")
        newlist[len(newlist)-1]=newlist[len(newlist)-1].rstrip("\n")
    
    return newlist

if __name__ == "__main__":
    main()
