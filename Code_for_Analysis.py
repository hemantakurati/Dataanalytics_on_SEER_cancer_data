import glob
import csv
import re


def main():
    d = {}
    Infile = open("icdo3.txt", "r")
    for line in Infile:
        r = re.search("(\d+/\d+)\s+(.+)", line)
        if r:
            code = r.group(1)
            code = code.replace("/", "")
            disease = r.group(2)
            disease = disease.rstrip()
            disease = disease.lower()
            d[code] = disease
    Infile.close()

    filelist = glob.glob("C:/Users/avula/Desktop/Priyanka/Assignment-10/SEER_1975_2016_TEXTDATA/incidence/yr*/*.TXT")
    # print(filelist)
    # filelist=glob.glob("C:/Users/avula/Desktop/Priyanka/Assignment-10/test.txt")
    di = {}  # dictionary with ICD-O codes as keys and # of occurrences as values
    for file in filelist:  # process each file
        # print(file)
        infile = open(file, "r")
        for line in infile:
            disease = line[52:57]  # ICD-Oncology-3 code (Histology+Behavior) )
            gender = line[23]
            birthstring = line[27:31]
            if (birthstring == "    "):
                birth = 0
            else:
                birth = int(birthstring)
            age = 2019 - birth
            # print(disease)
            # print(gender)
            # print(age)
            # index is the location in the list which needs to be updated
            if gender == "1":  # men
                if age < 25:
                    index = 0
                    # print("men25")
                elif age >= 25 and age < 50:
                    index = 2
                    # print("men25-50")
                elif age >= 50 and age < 75:
                    index = 4
                    # print("men50-75")
                elif age > 75:
                    index = 6
                    # print("men75+")
            if gender == "2":  # women
                if age < 25:
                    index = 1
                    # print("women25")
                elif age >= 25 and age < 50:
                    index = 3
                    # print("women25-50")
                elif age >= 50 and age < 75:
                    index = 5
                    # print("women50-75")
                elif age > 75:
                    index = 7
                    # print("women75+")
            if disease in di:
                di[disease][index] += 1
            else:
                di[disease] = [0] * 8  # list of eight zeros
                di[disease][index] += 1
            # a = int(line[52:57]) # ICD-Oncology-3 code (Histology+Behavior) appears at 53-57 characters (then why 52-57?)
            # di[a] = di.get(a,0)+1 # increment the count in the dictionary
        infile.close()
    # print(di)
    #print(d)

    w = csv.writer(open("output1.csv", "w"))
    for key, val in di.items():
        # print(val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7])
        name = str((d.get(key)))
        name = name.replace(",", "")
        w.writerow([name, val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7]])


main()