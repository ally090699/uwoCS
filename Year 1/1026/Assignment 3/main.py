from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    
    patients = {}
    try: ptFile=open(fileName,'r')
    except: print("An unexpected error occurred while reading the file.")

    if FileNotFoundError:
        print("The file '%s' could not be found." %fileName)

    import math  # opening module to use .trunc function in loop

    for line in ptFile.readlines():  # loop goes through each line of the file
        if line != "":
            line=line.strip()
            record=line.split(",")
            numFields=int(len(record))
            patientId=int(record[0])
            visitRecord=(record[1:])
            date=str(record[1])
            temp=float(record[2])
            hr=int(record[3])
            rr=int(record[4])
            sbp=int(record[5])
            dbp=int(record[6])
            spo2=int(record[7])
            if numFields==8:  # if there are 8 fields of data counted, the data will be checked for errors
                if (isinstance(patientId,int)==False) or (isinstance(date,str)==False) or (isinstance(temp,float)==False) or (isinstance(hr,int)==False) or (isinstance(rr,int)==False) or (isinstance(sbp,int)==False) or (isinstance(dbp,int)==False) or (isinstance(spo2,int)==False):
                    print("Invalid data type in line: [%s]" %line)
                    continue
                elif math.trunc(temp) not in range(30,44):
                    print("Invalid temperature value ([%f]) in line: [%s]" %(temp, line))
                    continue
                elif hr not in range(30,201):
                    print("Invalid heart rate value([%d]) in line: [%s]" %(hr, line))
                    continue
                elif rr not in range(5,61):
                    print("Invalid respiratory rate value([%d]) in line: [%s]" %(rr, line))
                    continue
                elif sbp not in range(50,251):
                    print("Invalid systolic blood pressure value([%d]) in line: [%s]" %(sbp, line))
                    continue
                elif dbp not in range(30,151):
                    print("Invalid diastolic blood pressure value([%d]) in line: [%s]" %(dbp, line))
                    continue
                elif spo2 not in range(80,101):
                    print("Invalid oxygen saturation value([%d]) in line: [%s]" %(spo2, line))
                    continue
                elif patientId not in patients:
                    patients[patientId]=[]
                patients[patientId].append(visitRecord)  # if there are no errors, the data is appended to the patient's log in the dictionary
        else:
            print("Invalid number of fields([%d]) in line: [%s]" %(numFields, line))
            continue
    ptFile.close()
    return patients


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    
    if patientId==0:  # conditional for loop that prints all patient data
        patientId=1
        for patientId in patients:
            print("Patient ID: %d" %int(patientId))
            for visit in patients[patientId]:
                ptVisit=visit
                print(" Visit Date: %s" %ptVisit[0])
                print("  Temperature: %.2f C" %float(ptVisit[1]))
                print("  Heart Rate: %d bpm" %int(ptVisit[2]))
                print("  Respiratory Rate: %d bpm" %int(ptVisit[3]))
                print("  Systolic Blood Pressure: %d mmHg" %int(ptVisit[4]))
                print("  Diastolic Blood Pressure: %d mmHg" %int(ptVisit[5]))
                print("  Oxygen Saturation: %d %%" %int(ptVisit[6]))
    else:  # conditional for loop that prints data for given patient id
        if patientId not in patients:
            print("Patient with ID %d not found." %patientId)
        else:
            print("Patient ID: %d" %int(patientId))
            for visit in patients[patientId]:
                ptVisit=visit
                print(" Visit Date: %s" %ptVisit[0])
                print("  Temperature: %.2f C" %float(ptVisit[1]))
                print("  Heart Rate: %d bpm" %int(ptVisit[2]))
                print("  Respiratory Rate: %d bpm" %int(ptVisit[3]))
                print("  Systolic Blood Pressure: %d mmHg" %int(ptVisit[4]))
                print("  Diastolic Blood Pressure: %d mmHg" %int(ptVisit[5]))
                print("  Oxygen Saturation: %d %%" %int(ptVisit[6]))
    return
                



def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    sumTemp=0
    cTemp=0
    sumHr=0
    cHr=0
    sumRr=0
    cRr=0
    sumSbp=0
    cSbp=0
    sumDbp=0
    cDbp=0
    sumOs=0
    cOs=0
    if isinstance(patients,dict)==False:  # first check 
        print("Error: 'patients' should be a dictionary.")
        return
    else:
        try:
            patientId=int(patientId)  # second check
        except:
            print("Error: 'patientid' should be an integer.")
            return
        if patientId==0:  # conditional for loop that prints data for all patients
            patientId+=1
            print("Vital Signs for All Patients:")
            for patientId in patients:
                for visit in patients[patientId]:
                    ptVisit=visit
                    sumTemp+=float(ptVisit[1])
                    cTemp+=1
                    sumHr+=int(ptVisit[2])
                    cHr+=1
                    sumRr+=int(ptVisit[3])
                    cRr+=1
                    sumSbp+=int(ptVisit[4])
                    cSbp+=1
                    sumDbp+=int(ptVisit[5])
                    cDbp+=1
                    sumOs+=int(ptVisit[6])
                    cOs+=1
            print("  Average temperature: %.2f C" %float((sumTemp/cTemp)))
            print("  Average heart rate: %.2f bpm" %float((sumHr/cHr)))
            print("  Average respiratory rate: %.2f bpm" %float((sumRr/cRr)))
            print("  Average systolic blood pressure: %.2f mmHg" %float((sumSbp/cSbp)))
            print("  Average diastolic blood pressure: %.2f mmHg" %float((sumDbp/cDbp)))
            print("  Average oxygen saturation: %.2f %%" %float((sumOs/cOs)))
        else:  # conditional for loop that prints data for given patient id
            if patientId not in patients:  # third check
                print("No data found for patient with ID %d." %int(patientId))
                return
            else:
                print("Vital Signs for Patient %d:" %patientId)
                for visit in patients[patientId]:
                    ptVisit=visit
                    sumTemp+=float(ptVisit[1])
                    cTemp+=1
                    sumHr+=int(ptVisit[2])
                    cHr+=1
                    sumRr+=int(ptVisit[3])
                    cRr+=1
                    sumSbp+=int(ptVisit[4])
                    cSbp+=1
                    sumDbp+=int(ptVisit[5])
                    cDbp+=1
                    sumOs+=int(ptVisit[6])
                    cOs+=1
            print("  Average temperature: %.2f C" %float((sumTemp/cTemp)))
            print("  Average heart rate: %.2f bpm" %float((sumHr/cHr)))
            print("  Average respiratory rate: %.2f bpm" %float((sumRr/cRr)))
            print("  Average systolic blood pressure: %.2f mmHg" %float((sumSbp/cSbp)))
            print("  Average diastolic blood pressure: %.2f mmHg" %float((sumDbp/cDbp)))
            print("  Average oxygen saturation: %.2f %%" %float((sumOs/cOs)))
    return



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    patientId=int(patientId)
    temp=float(temp)
    hr=int(hr)
    rr=int(rr)
    sbp=int(sbp)
    dbp=int(dbp)
    spo2=int(spo2)
    import math
    month=date.split("-")
    evenMonth=[4,6,9,11]
    oddMonth=[1,3,5,7,8,10,12]

    if int(month[1]) not in range(1,13) or int(month[1])==2 and int(month[2]) not in range(1,29) or int(month[1]) in evenMonth and int(month[2]) not in range(1,31) or int(month [1]) in oddMonth and int(month[2]) not in range(1,32) or len(month[0])!=4 or len(month[1])!=2 or len(month[2])!=2:  # series of error checks
        print("Invalid date. Please enter a valid date.")
    elif math.trunc(temp) not in range(30,44):
        print("Invalid temperature. Please enter a temperature between 30 and 43C.")
    elif hr not in range(30,201):
        print("Invalid heart rate. Please enter a heart rate between 30 and 200bpm.")
    elif rr not in range(5,61):
        print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 60bpm.")
    elif sbp not in range(50,251):
        print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 50 and 250mmHg.")
    elif dbp not in range(30,151):
        print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 30 and 150mmHg.")
    elif spo2 not in range(80,101):
        print("Invalid oxygen saturation. Please enter a oxygen saturation between 80 and 100%.")
    else:  # if no errors, opens file for appending to the end of the file
        ptFile=open(fileName,'a')
        ptFile.write("\n%d,%s,%.1f,%d,%d,%d,%d,%d" %(patientId,date,temp,hr,rr,sbp,dbp,spo2))
        ptFile.close()
        print("Visit saved successfully for Patient # %d" %patientId)
    return



def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []

    count=0 
    
    if (year!=None and month==None) or (year!=None and month==0):  # option 1
        if year not in range(0,2024):  #check
            return
        else:  # loops into each patient's visit appending year matches to the list
            for patientId in patients:
                for visit in patients[patientId]:
                    date=visit[0].split("-")
                    yrDate=int(date[0])
                    if yrDate==year:
                        count+=1
                        visit[1]=float(visit[1])
                        ptTuple=(patientId,visit)
                        visits.append(ptTuple)
            if count==0:  # if there are no matches, exits function
                return
    elif year!=None and month!=None:
        if year not in range(0,2024) or month not in range(0,13):  # check
            return
        else:  # loops into each patient's visit appending year and month matches to the list
            for patientId in patients:
                for visit in patients[patientId]:
                    date=visit[0].split("-")
                    yrDate=int(date[0])
                    mnDate=int(date[1])
                    visit[1]=float(visit[1])
                    isinstance(visit[1],float)
                    if yrDate==year and mnDate==month:
                        count+=1
                        visit[1]=float(visit[1])
                        ptTuple=(patientId,visit)
                        visits.append(ptTuple)
            if count==0:
                return
    elif (year==None or year==0) and (month==None or month==0):
        for patientId in patients:  # loops into each patient's visit appending all to the list
            for visit in patients[patientId]:
                visit[1]=float(visit[1])
                ptTuple=(patientId,visit)
                visits.append(ptTuple)
    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    for patientId in patients:   # loops into each patient's visits checking for abnormal vital signs
        for visit in patients[patientId]:
            hr=int(visit[2])
            sbp=int(visit[4])
            dbp=int(visit[5])
            os=int(visit[6])
            if hr>100 or hr<60 or sbp>140 or dbp>90 or os<90:
                followup_patients.append(patientId)
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    if patientId not in patients:
        print("No data found for patient with ID %s" %patientId)
    else:  # if no error, removes all data for given patient id
        newFile=open(filename,'w')
        patients.pop(patientId,None)
        for item in patients:
            for visit in patients[item]:
                newFile.write("%d,%s,%s,%s,%s,%s,%s,%s\n" %(item,visit[0],visit[1],visit[2],visit[3],visit[4],visit[5],visit[6]))
        newFile.close()
        print("Data for patient %s has been deleted." %patientId)
    return

###########################################################################
###########################################################################
#   The following code is being provided to you. Please don't modify it.  #
#   If this doesn't work for you, use Google Colab,                       #
#   where these libraries are already installed.                          #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('/Users/allisonso/Documents/UWO/Y4/CSCI1026/patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, '/Users/allisonso/Documents/UWO/Y4/CSCI1026/patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "/Users/allisonso/Documents/UWO/Y4/CSCI1026/patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()