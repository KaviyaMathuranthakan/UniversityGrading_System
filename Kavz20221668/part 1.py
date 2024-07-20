progress = 0
trailer = 0
retriever = 0
excluded = 0


while True:
    try :
    #input
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
                       
        elif p==100 :
            if  d==20 or d==0:
                print("Progress(module trailer)")
                trailer+=1
            elif  d==0 or d==20:
                print("Progress(module trailer)")
                trailer+=1
                   
        elif p==80:
            print("Do not progress = module retreiver")
            retriever+=1
             
        elif p==60:
            print("Do not progress = module retriever")
            retriever+=1
              
        elif p==40:
            if d==0 and f==80:
                print("Exculde")
                excluded+=1

            else:
                print("Do not progress = module retriever")
                retriever+=1
                
                
        elif p==20:
            if d==20 and f==80:
                print("Exculde")
                excluded+=1
                
            elif d==0 and f==100:
                print("Exculde")
                excluded+=1

            else:
                print("Do not progress = module retriever")
                retriever+=1
                

        elif p==0:
            if d==40 and f==80:
                print("Exculde")
                excluded+=1
                
            elif d==20 and f==100:
                print("Exculde")
                excluded+=1
                
            elif d==0 and f==120:
                print("Exculde")
                excluded+=1

            else:
                print("Do not progress = module retriever")
                retriever+=1
            
                
    
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
            break
      
         
     #integer required message
    except ValueError:
        print("Integer required")

