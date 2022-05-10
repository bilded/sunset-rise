import csv
 
f = open("SunRise_Set.csv","r") #파일 읽기 
reader = csv.reader(f)


for i in reader: #row라는 변수에 읽은 cvs파일을 하나씩 추가하여라 
    total = []
    total.append(i[0])
    total.append(i[5])
    total.append(i[7])
    print(total)
    
    #day =[]
    #day.append(i[0])
    #print(day)
    
    #sunrise =[]
    #sunrise.append(i[5])
    #print(sunrise)
    
    #sunset =[]
    #sunset.append(i[7])
    #print(sunset)
    
    
print("--------------------------------------------------")

for j in reader:
    sunrise =[]
    sunrise.append(j[5])
    print(sunrise)
print("--------------------------------------------------")    
for k in reader:
    sunset =[]
    sunset.append(k[7])
    print(sunset)
    

    
#양력일은 0번째,  월출 데이터는 5번째, 월몰 데이터는 7번째에 위치해있다. 
