#!/usr/bin/env python
from seqbio.calculation.SeqCal import *
from seqbio.pattern.SeqPattern import *
from seqbio.seqMan.dnaconvert import *
# from icecream import ic 

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    # subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", action='store_true', default=False,
                             help="Count number of each base in reverse complement DNA")

    cgcserch_command = subparsers.add_parser('cpgScan', help='Search for CpG sequence')
    cgcserch_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")

    Transcription_command = subparsers.add_parser('transcription', help='Transcription of DNA to RNA')
    Transcription_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    Transcription_command.add_argument("-r", "--revcomp", action='store_true', default=False,
                             help="Transcription of reverse complement DNA to RNA")


    Translation_command = subparsers.add_parser('translation', help='Translation of DNA to Protein')
    Translation_command.add_argument("-s", "--seq", type=str, default=None, 
                             help="Provide sequence")
    Translation_command.add_argument("-r", "--revcomp", action='store_true', default=False,
                             help="Translation of reverse complement DNA to Protein")


    Search_EcoRI_command = subparsers.add_parser('enzTargetsScan', help='Search for EcoRI restriction site')      
    Search_EcoRI_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    Search_EcoRI_command.add_argument("-r", "--revcomp", action='store_true', default=False,
                             help="Search for EcoRI restriction site in reverse complement DNA")
    Search_EcoRI_command.add_argument("-e", "--enzyme", type=str, default='EcoRI',
                             help="Provide enzyme name (default: EcoRI)")
    # parser.print_help()
    return parser


def test():
    # Input
    parser = argparserLocal()
    args = parser.parse_args(["cpgScan","-s","ATCGCTTTTTTCGCGCG"])
    print("Input",args.seq,"\ncpgScan =", cpgSearch(args.seq) )    
    
# Input
def main():
    parser = argparserLocal()
    args = parser.parse_args()
    print(args)

    if not hasattr(args, 'seq') or args.seq is None:
        print("------\nError: You did not provide a command or -s/--seq\n------\n")
        parser.print_help()
        return
    
    #if args.seq == None:
        #print("------\nError: You do not provide -s or --seq\n------\n")
    #else:
    seq = args.seq.upper()
    # print(seq)
    print('check1')
    # # Input
    # # seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'

    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        print("Input",args.seq,"\nGC content =", gcContent(seq) )

    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        print("Input",args.seq,"\ncountBases =", countBasesDict(seq) )
        if args.revcomp:
            print("Input",args.seq,"\ncountBases-revcomp =", countBasesDict(reverseComplementSeq(seq)) )
        
    
    elif args.command == 'cpgScan':
        if args.seq == None:
            exit(parser.parse_args(['cpgScan','-h']))
        print("Input",args.seq,"\ncpgScan =", cpgSearch(seq) )    

    elif args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription','-h']))
        print("Input",args.seq,"\nTranscription =", dna2rna(seq) )
        if args.revcomp:
            print("Input",args.seq,"\nTranscription-revcomp =", dna2rna(reverseComplementSeq(seq)) )

   
    elif args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation','-h']))
        print("Input",args.seq,"\nTranslation =", dna2protein(seq) )
        if args.revcomp:
            print("Input",args.seq,"\nTranslation-revcomp =", dna2protein(reverseComplementSeq(seq)) )



    elif args.command == 'enzTargetsScan':
        if args.seq == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        if args.revcomp:
            print("Input",args.seq,"\nSearch " + args.enzyme + "-revcomp =", enzTargetsScan(reverseComplementSeq(seq), args.enzyme) )
        else:
            print("Input",args.seq,"\nSearch " + args.enzyme + " =", enzTargetsScan(seq, args.enzyme) )

    


def test1():
    # Input
    seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    seq = seq.upper()
    print("Transcription: ", dna2rna(seq))
    print("Transcription-revcomp: ", dna2rna(reverseComplementSeq(seq)))
    print("Translation: ", dna2protein(seq))
    print("Translation-revcomp: ", dna2protein(reverseComplementSeq(seq)))
    print("GC Content:", gcContent(seq))
    print("Count Bases: ", countBasesDict(seq))
    print("Count Bases-revcomp: ", countBasesDict(reverseComplementSeq(seq)))
    print("Search EcoRI: ", enzTargetsScan(seq, 'EcoRI'))
    print("Search EcoRI-revcomp: ", enzTargetsScan(reverseComplementSeq(seq), 'EcoRI'))

if __name__ == "__main__":
    main()
    #test1()
