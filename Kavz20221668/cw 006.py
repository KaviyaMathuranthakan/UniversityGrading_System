progress = 0
trailer = 0
retriever = 0
excluded = 0

#list
listt=[]

#dict
outputs={}

#defs for appending to list
def lst():
    listt.append(["progress:- ",p,",",d,",",f])

def lst1():
    listt.append(["trailer:- ",p,",",d,",",f])

def lst2():
    listt.append(["retriever:- ",p,",",d,",",f])

def lst3():
    listt.append(["excluded:- ",p,",",d,",",f])

#defs for dics

def dict_of_progress():
    outputs[st_id] = ["progress:- ",p,d,f]

def dict_of_trailer():
    outputs[st_id] = ["trailer:- ",p,d,f]

def dict_of_retriever():
    outputs[st_id] = ["retriever:- ",p,d,f]

def dict_of_excluded():
    outputs[st_id] = ["excluded:- ",p,d,f]

#looping
while True:
    try :
    #input
        st_id=input("enter the student id:- ")
        if st_id [0] != "w" or len(st_id ) !=8:
            print("invalid student id ")
            continue
        
        p = int(input("PLEASE ENTER YOUR CREDITS AT PASS : "))
    #out of range message   
        if p not in range(0,121,20):
            print("Out of range")
            continue
            
        d = int(input("PLEASE ENTER YOUR CREDITS AT DEFER : "))
    #out of range message
        if d not in range(0,121,20):
            print("Out of range")
            continue
        
        f = int(input("PLEASE ENTER YOUR CREDITS AT FAIL : "))
    #out of range message 
        if f not in range(0,121,20):
            print("Out of range")
            continue

    #total incorrect message
        if p+d+f!=120:
            print("Total incorrect")
            
    #outcomes        
        if p==120:
            print("progress")
            progress+=1
            
            lst()
            
            text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
            text_file.write("\n")
            text_file.write("progress:- ")
            text_file.write(str(p))
            text_file.write(",")
            text_file.write(str(d))
            text_file.write(",")
            text_file.write(str(f))
            text_file.close()
            
            dict_of_progress()
            
        elif p==100:
            if  d==20 or d==0:
                print("Progress(module trailer)")
                trailer+=1
                lst1()
                text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
                text_file.write("\n")
                text_file.write("trailer:- ")
                text_file.write(str(p))
                text_file.write(",")
                text_file.write(str(d))
                text_file.write(",")
                text_file.write(str(f))
                text_file.close()

                dict_of_trailer()
                
            elif  d==0 or d==20:
                print("Progress(module trailer)")
                trailer+=1
                lst1()
                text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
                text_file.write("\n")
                text_file.write("trailer:- ")
                text_file.write(str(p))
                text_file.write(",")
                text_file.write(str(d))
                text_file.write(",")
                text_file.write(str(f))
                text_file.close()
                
                dict_of_trailer()

        elif p==80:
            print("Do not progress = module retreiver")
            retriever+=1
            
            lst2()
            
            text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
            text_file.write("\n")
            text_file.write("retriever:- ")
            text_file.write(str(p))
            text_file.write(",")
            text_file.write(str(d))
            text_file.write(",")
            text_file.write(str(f))
            text_file.close()

            dict_of_retriever()
            
            
        elif p==60:
            print("Do not progress = module retriever")
            retriever+=1
            
            lst2()
            
            text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
            text_file.write("\n")
            text_file.write("retriever:- ")
            text_file.write(str(p))
            text_file.write(",")
            text_file.write(str(d))
            text_file.write(",")
            text_file.write(str(f))
            text_file.close()

            dict_of_retriever()
            
        elif p==40:
            if d==0 and f==80:
                print("Exculde")
                excluded+=1
                
                lst3()
                
                text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
                text_file.write("\n")
                text_file.write("Exculde:- ")
                text_file.write(str(p))
                text_file.write(",")
                text_file.write(str(d))
                text_file.write(",")
                text_file.write(str(f))
                text_file.close()

                dict_of_excluded()

            else:
                print("Do not progress = module retriever")
                retriever+=1
                
                lst2()
                
                text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
                text_file.write("\n")
                text_file.write("retriever:- ")
                text_file.write(str(p))
                text_file.write(",")
                text_file.write(str(d))
                text_file.write(",")
                text_file.write(str(f))
                text_file.close()

                dict_of_retriever()
                
        elif p==20:
            if d==20 and f==80:
                print("Exculde")
                excluded+=1
                
                lst3()
                
                text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
                text_file.write("\n")
                text_file.write("Exculde:- ")
                text_file.write(str(p))
                text_file.write(",")
                text_file.write(str(d))
                text_file.write(",")
                text_file.write(str(f))
                text_file.close()

                dict_of_excluded()
                
            elif d==0 and f==100:
                print("Exculde")
                excluded+=1
                
                lst3()
                
                text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
                text_file.write("\n")
                text_file.write("Exculde:- ")
                text_file.write(str(p))
                text_file.write(",")
                text_file.write(str(d))
                text_file.write(",")
                text_file.write(str(f))
                text_file.close()

                dict_of_excluded()
                
            else:
                print("Do not progress = module retriever")
                retriever+=1

                lst2()
                
                text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
                text_file.write("\n")
                text_file.write("retriever:- ")
                text_file.write(str(p))
                text_file.write(",")
                text_file.write(str(d))
                text_file.write(",")
                text_file.write(str(f))
                text_file.close()

                dict_of_retriever()
                
        elif p==0:
            if d==40 and f==80:
                print("Exculde")
                excluded+=1
                
                lst3()
                
                text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
                text_file.write("\n")
                text_file.write("Exculde:- ")
                text_file.write(str(p))
                text_file.write(",")
                text_file.write(str(d))
                text_file.write(",")
                text_file.write(str(f))
                text_file.close()

                dict_of_excluded()
                
            elif d==20 and f==100:
                print("Exculde")
                excluded+=1
                
                lst3()
                
                text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
                text_file.write("\n")
                text_file.write("Exculde:- ")
                text_file.write(str(p))
                text_file.write(",")
                text_file.write(str(d))
                text_file.write(",")
                text_file.write(str(f))
                text_file.close()

                dict_of_excluded()
                
            elif d==0 and f==120:
                print("Exculde")
                excluded+=1
                
                lst3()
                
                text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
                text_file.write("\n")
                text_file.write("Exculde:- ")
                text_file.write(str(p))
                text_file.write(",")
                text_file.write(str(d))
                text_file.write(",")
                text_file.write(str(f))
                text_file.close()

                dict_of_excluded()

            else:
                print("Do not progress = module retriever")
                retriever+=1
                
                lst2()
                
                text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","a")
                text_file.write("\n")
                text_file.write("retriever:- ")
                text_file.write(str(p))
                text_file.write(",")
                text_file.write(str(d))
                text_file.write(",")
                text_file.write(str(f))
                text_file.close()

                dict_of_retriever()

        #asking user choice
        print("Would you like to enter another set of data? ")
        user_choice= input("Enter 'y' for yes or 'q' to quit ")
        if user_choice == "y":
            continue
        if user_choice == "q":
            print("-"*80)
            print("Histogram")
            print("progress",progress,":","*"*progress)
            print("trailer",trailer,":","*"*trailer)
            print("retriever",retriever,":","*"*retriever)
            print("excluded",excluded,":","*"*excluded)
            print(progress+trailer+retriever+excluded,"Total outcomes")
            print("-"*80)
            print("part02")
            for i in listt:
                print(*i)
            print("-"*80)
            break
      
         
#integer required message
    except ValueError:
        print("Integer required")

#part02
#open text file 
text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","r")
data=text_file.read()
print("part03")
print(data)
text_file.close()

#part03
#close and rewrite text file
text_file = open("C:\\Users\\Computer Corner\\Desktop\\Kavz20221668\\Students Outcomes","w")
text_file.write("")

#part04
#loop dict
print("-"*80)
print("part04")
for key,value in outputs.items():
    print(f"{key} : {value[0]} - {value[1]}, {value[2]}, {value[3]}", end=",")
            
            
                  
 








