import csv
import sys
import argparse
import os.path

parser = argparse.ArgumentParser(description='Parse the temperatures, concatenate into one file')



parser.add_argument('-in',
                    dest='fasta',
                    required = True,
                    help='Input a SecStruct output file',
                    metavar = 'FILE',
                    #type=lambda x: is_valid_file(parser,x)
                    )

parser.add_argument('-out',
                    dest='out',
                    required = True,
                    help='output specific Transcript',
                    metavar = 'FILE',
                    #type=lambda x: is_valid_file(parser,x)
                    )

parser.add_argument('-transcript',
                    dest='transcript',
                    required = True,
                    help='Name of the desired transcript',
                    metavar = 'FILE',
                    #type=lambda x: is_valid_file(parser,x)
                    )

args = parser.parse_args()

with open("%s" %(args.fasta), "rU") as in_raw, open('%s' %(args.out),'r') as int_raw:
    infile = csv.reader(in_raw, delimiter = '\t')
    outInt = csv.reader(int_raw, delimiter = '\t')

    

    inDict = {}

    for row in infile:
        if str(args.transcript) in row[0]:
            inDict[row[1]] = row[2]
            

    outDict = {}

    
    for row in outInt:
        count = 0
        for element in row:
            if count == 0:
                index = element
                outDict[index] = []
                count +=1
            else:
                outDict[index].append(element)
                count +=1


    if len(outDict) == 0:
        for key, value in inDict.items():
            
            outDict[key] = [value]

    else:
        for key, value in inDict.items():
##            print value
            if key in outDict:
##                print key,outDict[key], value
##                print key
                outDict[key].append(value)
##                print len(outDict[key])


    outList = []

    with open('%s' %(args.out),'w') as out_raw:
        outfile = csv.writer(out_raw, delimiter = '\t')
        for key, value in outDict.items():
            row = []
            row.append(key)

            for element in value:
                row.append(element)

##            print row
            outfile.writerow(row)
##            print len(row)
##            print type(row)
        
        
                
            
                


            
    
