import re
text = open('D:\DWH\***', 'r').read()
text2 = text.replace("<", "\n<")
workflowName = r'<WORKFLOW_NAME>.*'
runStatusCode = r'<RUN_STATUS_CODE>.*' 
runStatusCodeEnd = r'<RUN_STATUS_CODE/>'
file = open("D:\DWH\workbench.txt", 'w')
file.write(text2)
list = []
errorList = []
isFailed = False
readFile = open('D:\DWH\workbench.txt', 'r').readlines()
for line in readFile:
    flag = True
    workflowName = re.search(workflowName, line)
    runStatusCode = re.search(runStatusCode,line)
    runStatusCodeEnd = re.search(runStatusCodeEnd,line)
    if workflowName: #if we found sth
        line = workflowName.group()
        properLine = line[15:]
        list.append(properLine)
    if runStatusCodeEnd:
        list.remove(lista[-1])
    elif runStatusCode:
        status = runStatusCode.group()
        correctStatus = status[17:]
        list.append(correctStatus)
 
 
　
counter = 0
for item in list:
    flag = False
    if item == "Suceeded" or item =="Running":
        errorList.append(list[counter-1])
    if item == "Failed":
        if counter == 1:
            #errorList.append(lista[counter-1])
            counter = counter + 1
            isFailed = True
            break
        else:
            errorCounter = 0
            if list[counter-1] not in errorList:
                isFailed = True
            else:
                isFailed = False
  
    counter = counter + 1            
         
         
                   
if isFailed == True:
    print("Found Errors")
else:
    print("No Errors, go on")
