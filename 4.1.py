# A Dynamic Programming based Python program for edit
# distance problem
import editdistance

# Driver program
import math

if __name__ == '__main__':
    # this is for GP gen, If you want to do it for other gens you have to change the "GP_O" to your desire name

    data = [5, 5, 5, 5, 5, 5]

    # read data

    with open('Marburg_genome.txt', 'r') as myfile:
        data[0] = myfile.read().replace('\n', '')

    with open('TaiForest_genome.txt', 'r') as myfile:
        data[1] = myfile.read().replace('\n', '')

    with open('Zaire_genome.txt', 'r') as myfile:
        data[2] = myfile.read().replace('\n', '')

    with open('Sudan_genome.txt', 'r') as myfile:
        data[3] = myfile.read().replace('\n', '')

    with open('Bundibugyo_genome.txt', 'r') as myfile:
        data[4] = myfile.read().replace('\n', '')

    with open('Reston_genome.txt', 'r') as myfile:
        data[5] = myfile.read().replace('\n', '')

    for i in range(0,6):
        for j in range(i,6):
            str1 = data[i]
            str2 = data[j]
            # edit distance
            score = editdistance.eval(str1,str2)

            #calculate t here
            if len(str1) > len(str2):
                tmp = -3/4*math.log(1-(4/3)*(score/len(str1)))
                print (tmp / 0.0019)
            else:
                tmp = -3 / 4 * math.log(1 - (4 / 3) * (score / len(str2)))
                print(tmp / 0.0019)
