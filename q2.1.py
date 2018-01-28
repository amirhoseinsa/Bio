from Bio import pairwise2
from Bio.pairwise2 import format_alignment, _make_score_matrix_generic


from math import ceil


def allign(seq1 , seq2 , name , gap):
    f1 = ""
    #allign here
    for a in pairwise2.align.globalms(seq1, seq2, 1, -1, -1, -1, penalize_end_gaps=(False, False)):
         f1 = format_alignment(*a)
         break


    #our parameter
    res1 = 0
    cnt = 0
    cnt_for_seq1 = 0
    start = False
    lengthToBreak = 0


    #determine end of seq1 in allignment
    for i in range(0, len(f1)):
        if (f1[i] != '-'):
            cnt = cnt + 1
        if (cnt == len(seq1)):
            lengthToBreak = i
            break

    cnt = 0
    # determine end of seq2 in allignment
    for i in range(2 * lengthToBreak , len(f1)):
        if(f1[i] != '-'):
            cnt = cnt + 1
        if (cnt == len(seq2)):
            res1 = i - 2*lengthToBreak
            break

    newSeq1 = f1[:lengthToBreak]

    newSe2 = ""

    #create our new seqs
    for i in range(2*lengthToBreak, len(f1)):
        if f1[i].isalpha():
            newSe2 = newSe2 + f1[i]
        if f1[i] == '-' :
            newSe2 = newSe2 + f1[i]


    result = ""

    #generate output here
    start = False
    for i in range (1,res1):
        if (start == False):
            if ((newSe2[i].isalpha())):
                start = True
        if (start == True):
            if (newSeq1[i] != '-'):
               result = result + newSeq1[i]

    print(f1)
    print(result)
	
    #save output to file
    text_file = open(name + "_O.txt", "w")
    text_file.write("%s" % result)
    text_file.close()
    print(res1)
    return res1






""" ----STARTS THE  EXECUTION---- """
if __name__ == "__main__":
    #open our data and save them in data , data2
    with open('Reston_genome.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')

    with open('NP.txt', 'r') as myfile:
        data2 = myfile.read().replace('\n', '')

    ind = int(ceil( len(data2)* 1.5))
    sequence1 = data
    sequence2 = data2

    # our parameter
    match_award = 1
    mismatch_penalty = -1
    gap_penalty = -1

    #call allign func
    first = allign(sequence1, sequence2 , "NP" , True)

    """____"""
    with open('Reston_genome.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')

    with open('VP35.txt', 'r') as myfile:
        data2 = myfile.read().replace('\n', '')

    sequence1 = data
    sequence2 = data2

    match_award = 1
    mismatch_penalty = -1
    gap_penalty = -1

    allign(sequence1, sequence2, "VP35" , False)

    """____"""
    with open('Reston_genome.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')

    with open('VP40.txt', 'r') as myfile:
        data2 = myfile.read().replace('\n', '')

    sequence1 = data
    sequence2 = data2

    match_award = 1
    mismatch_penalty = -1
    gap_penalty = -1

    allign(sequence1, sequence2, "VP40" , False)




    """____"""
    with open('Reston_genome.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')

    with open('GP.txt', 'r') as myfile:
        data2 = myfile.read().replace('\n', '')

    sequence1 = data
    sequence2 = data2

    match_award = 1
    mismatch_penalty = -1
    gap_penalty = -1

    allign(sequence1, sequence2, "GP" , False)
    """____"""
    with open('Reston_genome.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')

    with open('VP30.txt', 'r') as myfile:
        data2 = myfile.read().replace('\n', '')

    sequence1 = data
    sequence2 = data2

    match_award = 1
    mismatch_penalty = -1
    gap_penalty = -1

    allign(sequence1, sequence2, "VP30" , False)
    """____"""
    with open('Reston_genome.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')

    with open('VP24.txt', 'r') as myfile:
        data2 = myfile.read().replace('\n', '')

    sequence1 = data
    sequence2 = data2

    match_award = 1
    mismatch_penalty = -1
    gap_penalty = -1

    allign(sequence1, sequence2, "VP24" , False)



    """____"""
    with open('Sudan_genome.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')

    with open('L.txt', 'r') as myfile:
        data2 = myfile.read().replace('\n', '')

    sequence1 = data[ceil(len(data)-len(data2)):]
    sequence2 = data2

    match_award = 1
    mismatch_penalty = -1
    gap_penalty = -1

    allign(sequence1, sequence2, "L" , False)

