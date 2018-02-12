import re
import csv
import fileinput
import pandas as pd
import numpy as np

## Input: single chromosome and coordinate breakpoint
CHR_position = input("Chromosome Number: ")
Coordinate = input("Coordinate Breakpoint: ")

CHR = "chromosome {}".format(CHR_position)

## File: /afs/ir.stanford.edu/class/gene211/misc/SGD_features.tab
## Downloaded to: /Users/jessicachen/Dropbox (Personal)/2018-Winter_GENE211_Genomics/Pset
with fileinput.input(files=('/Users/jessicachen/Dropbox (Personal)/2018-Winter_GENE211_Genomics/Pset/SGD_features.tab')) as infile:

    ## Subset by Chromosome of interest 
    with open('file.csv', 'w', newline = '\n') as infile_CHRsubset:
        for line in infile:
            if re.search(CHR, line):
                infile_CHRsubset.write(line)
    infile_CHRsubset.close()

## Import subset file as dataframe 
df = pd.read_csv(r'file.csv', header = 0, sep = '\t', \
    names = ['pSGDID', 'fType', 'qualifier', 'feature', 'gene', 'aliases', \
    'parent', 'sSGDID', 'chromosome', 'start', 'stop', 'strand', 'pos', \
    'cVersion', 'sVersion', 'description'])

## Calculate center location of each gene
HalfAbsDistance = (round((df['stop'] - df['start'])*0.5)).abs()

df.loc[df['strand'] == 'W', "CenterDistance"] = (df['start'] + HalfAbsDistance)
df.loc[df['strand'] == 'C', "CenterDistance"] = (df['stop'] + HalfAbsDistance)

## Calculate distance from breakpoint to center of each gene
df['Distance'] = (int(Coordinate) - df['CenterDistance']).abs()

## Sort dataframe by shortest distance
df = df.sort_values(by=['Distance'], ascending = [True])

## Drop NaN values
df = df.dropna(subset = ['Distance'])

## Subset to distances <= 5kb of breakpoint
df = df.loc[df['Distance'] <= 5000]

## Output: identifiers of genomic features closest to breakpoint
    ## Distance - rounded to nearest integer
    ## Primary SGDID
    ## Feature Name
    ## Standard Gene Name 
df.to_csv(r'output.txt', columns=['Distance', 'pSGDID', 'feature', 'gene'], \
    header = None, sep='\t', index=False)

## Input: position 788000 on CHR 16