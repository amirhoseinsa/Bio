
import editdistance
# Driver program
if __name__ == '__main__':

    #this is for GP gen, If you want to do it for other gens you have to change the "GP_O" to your desire name
    data = [5, 5, 5, 5, 5]

    #read data
    with open('TaiForest\GP_O.txt', 'r') as myfile:
        data[0] = myfile.read().replace('\n', '')

    with open('Zaire\GP_O.txt', 'r') as myfile:
        data[1] = myfile.read().replace('\n', '')

    with open('Sudan\GP_O.txt', 'r') as myfile:
        data[2] = myfile.read().replace('\n', '')

    with open('Bundibugyo_genome\GP_O.txt', 'r') as myfile:
        data[3] = myfile.read().replace('\n', '')

    with open('Reston\GP_O.txt', 'r') as myfile:
        data[4] = myfile.read().replace('\n', '')




    for i in range(0,5):
        for j in range(i,5):
            str1 = data[i]
            str2 = data[j]
            #edit distance
            score = editdistance.eval(str1, str2)
            print("___")
            print(score)

