#To train the model, we will split our data 80/10/10
#This means that each individual source of data must be split this way, then added together
#Rather than adding all together, then splitting
#so we'll access 3 aligned sources rather than one big one 


from subprocess import call

path = "/ParsText/data/unaligned/raw_data/"

call(["python","gale-church.py",(path + "bbc.txt"),("data/bbc.fa"),("data/bbc.tj"), "gacha"])
call(["python","gale-church.py",(path + "dr.txt"),("data/dr.fa"),("data/dr.tj"), "gacha"])
call(["python","gale-church.py",(path + "jj.txt"),("data/jj.fa"),("data/jj.tj"), "gacha"])
