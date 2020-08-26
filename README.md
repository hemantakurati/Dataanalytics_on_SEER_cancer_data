Analyzing SEER cancer data

System Requiremens:
Programming Language - Python 3.x
Libraries - csv,re,glob

Background: I Acquired a Dataset from The National Cancer Institute’s SEER (Surveillance, Epidemiology and End Results) Program conducted in 28 percent of Us population on different cancer incidences which is funded by NCI and CDC. Using the Data set from SEER Program I tried to find out the cancer occurrences in all types in different age groups ranges for both men and women Respectively. 
Method: Firstly I Obtained the SEER dataset by signing and sending the user-agreement form at http://seer.cancer.gov/data/request.html . Then I obtained the login-password to access the SEER dataset which I downloaded from http://seer.cancer.gov/data/options.html the ASCII text version of the data and uncompressed it. Later I saved a file with ICD-O3 codes with the respective diseases. I performed data analytics on the data and saved an output results file in .csv format for future references.
Results: I saved a datafile with output data after analysis which consists of number of cases with different cancers for different age groups and genders. Based on the results obtained majority of the cases reported are among the men(age>75) and adenocarcinoma ranks among the highest.
