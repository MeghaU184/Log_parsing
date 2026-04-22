# Log Analyzer
# Author: Megha U
# Purpose: Parse validation log files and extract test results
# pattern used : #"[2024-03-01 09:00:18] FAIL  - Test: NVMe_Link_Speed - Expected Gen3x4, got Gen2x4"

import csv

res=[]
with open("logs/sample_log.txt",'r') as file:
    for line in file:
        parts= line.strip().split(" -")
        part=parts[0].split("]")

        status=part[1].strip()
        time=part[0].replace('"[',"").strip()
        test=parts[1].replace("Test:","").strip()
        msg=parts[2].replace('"',"").strip()

        entry={"time_stamp": time,"status": status,"test": test,"msg": msg }
        res.append(entry)

count={"PASS":0,"FAIL":0,"ERROR":0,"WARN":0}
for item in res:
    if item["status"]=="PASS":
        count["PASS"]+=1
    elif item["status"]=="FAIL":
        count["FAIL"]+=1
    elif item["status"]=="ERROR":
        count["ERROR"]+=1
    elif item["status"]=="WARN":
        count["WARN"]+=1
#we can use counter here 
print("="*40)
print("Log analysis report")
print("="*40)
print("PASS:", count["PASS"])
print("FAIL:", count["FAIL"])
print("ERROR:", count["ERROR"])
print("WARN:", count["WARN"])
print("TOTAL TEST:", len(res))
print(f"PASS RATE:, {count["PASS"]/len(res)*100}%")



#generating csv report
with open("report.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["time_stamp", "status", "test", "msg"])
    writer.writeheader()
    writer.writerows(res)

print("report.csv saved!")


