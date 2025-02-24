"""This code will take the many text files that make up the TJ and FA corpora, and
then put them into the formats that GachaAlign requires


@author: Rayyan Merchant
"""

import os
import codecs
import re


corpus_path = "/Users/rayyanmerchant/Dropbox (UFL)/ParsTransliteration/data/blogs/"
align_path = "/Users/rayyanmerchant/Dropbox (UFL)/ParsTransliteration/data/aligned/gacha/data/"

farsi = []
tajiki = []

def deNoise(text): #from maxim romanov
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)
    return text

def substitute(line,code):
    line = re.sub(r'\s*[A-Za-z]+\b', '', line)
    line = re.sub(r'[!?؟;:]','.',line)
    line = line.replace('...','.')
    line = re.sub(r'[\(\)\[\]\{\}”/_=+@#$%^&*<>»«“"]', '', line)

    #COMMAS SHOULD NOT BE TREATED LIKE PERIODS/SENTENCE ENDERS, IT MESSES UP GALECHURCH ALIGNMENT SEVERELY
    line = line.replace('،',' ')
    line = line.replace(',',' ')
    line.strip(' ')
    
    line_split = line.split(' ')
    new_split = []
    
    for item in list(line_split):
        digit = False
        for char in item:
            if char.isdigit():
                digit = True
        if digit == False:
            new_split.append(item)
            


    #print(' '.join(line_split))
    line = ' '.join(new_split)
    
    #if(any(i.isdigit() for i in line)):
        #print(line)
    #print(line)
    #print(line)
    if (code == "fa"):
        line = re.sub(r"[А-яғӣқӯҷ]",'',line)
        line = line.replace("ى", "ي")
        line = line.replace("-","")#for when preposition is merged with - in tajik
        line = re.sub(r"[إأٱا]", "ا",line)
        ra = " را "
        ho = " ها " 
        hoy = " های "
        mi = " می "
        mix = mi.rstrip(' ') + "\u200c"      
        hoyx = "\u200C" + hoy.lstrip(' ')
        hox = "\u200C" + ho.lstrip(' ')
        rax = "\u200C" + ra.lstrip(' ')

        line = line.replace(ra,rax)
        line = line.replace(ho,hox)
        line = line.replace(hoy,hoyx)
        line = line.replace(mi,mix)
    elif (code == "tj"):
        line = re.sub(r'[ضصثقفغعهخحجچگمکنتالبیسشظطزرذدپوةآأإيئؤكژ؟ء٫٬]', '', line)
    line = line.replace("  ", " ")
    return line

def gacha_prep(in_lines,out_lines,code,name):
    count = 1
    for line in in_lines:
        if line.find("-=-") != -1:
            out_lines.append("# " + code + "_" + name + "_"+ str(count) + "\n")
            count = count + 1
        elif line != "\n":
            line = substitute(line,code)
            sentences = line.split('.')
            for sentence in sentences:
                sentence = sentence.lower()
                sentence = sentence.replace('\n','')
                sentence = sentence.replace('  ',' ')
                sentence = sentence.strip(' ')
                if len(sentence) > 0:
                    out_lines.append(sentence + '\n')
    return out_lines



def main():
    doc_names = ["bbc","jj","dr"]
    codes = ["fa","tj"]
    for code in codes:
        for name in doc_names:
            output = []
            with codecs.open(corpus_path + name + "." + code ,"r",'utf-8') as source:
                with codecs.open(align_path + name + "." + code,'w','utf-8') as outputter:
                    lines = source.readlines()
                    gacha_prep(lines,output,code,name)
                    #text has now been cleaned and put into a numbered format 
                    #lets make a composite and also individual text files for each of these entries
                    #this finds the #code in the output list
                    #then creates a numbered text file, iterating through until the
                    #next #code line, until end of list of strings
                    for line in output:
                        outputter.write(line)
                    #this one will write the individual text files
                    for line_num in range(0,len(output)):
                        if output[line_num].find("# " + code) != -1:
                            with codecs.open("/Users/rayyanmerchant/Dropbox (UFL)/ParsTransliteration/data/blogs/indiv/" +output[line_num][5:].strip('\n') + "." + code,'w') as individual:
                                count  = 1
                                while( ((line_num+count) < len(output)) and (output[line_num+count].find("# " + code) == -1)):
                                    individual.write(output[line_num+count])
                                    count = count + 1



main()          



