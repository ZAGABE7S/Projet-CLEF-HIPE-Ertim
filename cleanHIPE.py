#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:24:42 2020

@author: jc-zagabe
"""

import numpy
import os
import re
import sys

   
def main(inputfile="",outfile=""):
    if inputfile=="" or outfile=="":
        print( "vous devez passer deux fichiers en paramètre")
        exit(0)

    #fichier=/home/jc-zagabe/Documents/Ubuntu SE/STAGE-PROJET-TALAD-ERTIM-Octobre2019/Projet HIPE/data/sample-v1.0/fr/HIPE-data-v01-sample-fr.tsv

    data=None
    ch=""
    p=[]
    ch1=""
    with open(inputfile,"r") as fic:
        data=fic.read()
    ch=data.split("\n")
    ex=r"^#"
    ex1=r"^TOKEN"
    del ch[0]
    for k in ch:
        if re.match(ex,k) is None or "TOKEN" not in k:
            tmp=k.split("\t")
            p.append(tmp[0])
            if len(tmp)>=10:
                if(tmp[9].lower()=="EndOfLine".lower()):
                    ch1+=tmp[0]+" "
                elif(tmp[9].lower()=="NoSpaceAfter".lower()):
                    ch1+=tmp[0]
                else:
                    ch1+=tmp[0]+" "

            
    """ch1=re.sub(r"0_"," ",ch1)
    ch1=re.sub(r"__"," ",ch1)
    ch1=re.sub(r"_"," ",ch1)
    ch1=re.sub(r"0","",ch1)
    ch1=re.sub(r"\n","",ch1)
    ch1=ch1.replace("\n","")"""
    
    with open(outfile,"w") as f:
        f.write(ch1)
   # print(ch1)
if __name__ == "__main__":
    if len(sys.argv)<3:
        print("nombre d'arguments insuffisant")
        exit(0)
    main(sys.argv[1],sys.argv[2])