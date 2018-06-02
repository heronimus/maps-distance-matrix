import simplejson
import urllib.request
import csv

def MapsDistance(orig_coord,dest_coord):
    url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(orig_coord),str(dest_coord))
    distance_val = "-1"
    duration_val = "-1"

    try:
        result= simplejson.load(urllib.request.urlopen(url))
        status= result['rows'][0]['elements'][0]['status']
    except:
        status="ERROR"

    if status=="OK":
        distance_val = result['rows'][0]['elements'][0]['distance']['value']
        duration_val = result['rows'][0]['elements'][0]['duration']['value']

    return status,distance_val,duration_val

if __name__ == '__main__':
    print("---------------------------------------------------")
    print("--> This Python Script Using Google Maps Distance Matrix API")
    print("    please be aware that Google limits free request to 2500/day.")
    print("---------------------------------------------------")

    #Open cordinate csv file
    with open('coordinate.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        listCoord = list(spamreader)

    #List for Header location name
    headerList=[]
    for row in listCoord:
        headerList.append(row[0])

    datarow = len(listCoord)
    print("Data Row : ",datarow)

    distanceDict = {}
    durationDict = {}
    index=0

    #For Loops to create distance and duration list
    for i in range(1,datarow):
        distanceList = []
        durationList = []
        #Append location name to first Row
        distanceList.append(listCoord[i][0])
        durationList.append(listCoord[i][0])

        for j in range(1, datarow):
            if j<i+1:
                distanceList.append("")
                durationList.append("")
            else:
                index=index+1
                #Replace . (point) with , (comma) for excel csv compability
                orig_coord="{},{}".format(listCoord[i][1].replace(",","."),listCoord[i][2].replace(",","."))
                dest_coord="{},{}".format(listCoord[j][1].replace(",","."),listCoord[j][2].replace(",","."))
                status,distance_val,duration_val=MapsDistance(orig_coord,dest_coord)
                # Append distance and duration data with 2 digits after comma
                if not distance_val=="-1":
                    distanceList.append(("%.2f" % (int(distance_val)/1000)).replace(".",","))
                    durationList.append(("%.2f" % (int(duration_val)/60)).replace(".",","))
                else:
                    distanceList.append("error")
                    durationList.append("error")

                #Log Print
                print("{}. {} - Ori : ({}) --> Dest : ({}) = {} ; {}"
                    .format(index, status,listCoord[i][0],listCoord[j][0],distance_val,duration_val))

        distanceDict[str(i)] = distanceList
        durationDict[str(i)] = durationList

        #Break at google maps quota 2500 request
        if index>=2500:
            print("Request has more than 2500 Google Maps request limits.")
            break


    #Write List to CSV file
    print("\n--> Saving Distance Matrix to distance_matrix.csv")
    with open('distance_matrix.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(headerList)
        for i in range(1,datarow):
            spamwriter.writerow(distanceDict[str(i)])
        spamwriter.writerow([])
        spamwriter.writerow(["**Distance in kilometer"])

    print("--> Saving Duration Matrix to duration_matrix.csv")
    with open('duration_matrix.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(headerList)
        for i in range(1,datarow):
            spamwriter.writerow(durationDict[str(i)])
        spamwriter.writerow([])
        spamwriter.writerow(["**Duration in minutes"])

    print("\nThankyou!")
