def security_audit(astronauts):
 age_denied=[]
 clearance_denied=[]
 role_denied=[]
 allow_access=[]

 for astronaut in astronauts:
    
    id=astronaut[0]
    age=astronaut[1]
    role=astronaut[2]
    clearance=astronaut[3]
    
    if(age <18):
     
    #  print("access denied(under age)")
     age_denied=[id]
     
     if(clearance ==False):
       clearance_denied=[id]
      #  print("access denied:"age_denied)
       
       if(role =="commander" or role=="engineer" or role =="scentist"):
         print("Allow access")
         allow_access=[id]
         
       else:
       
            print("unknown role") 
            role_denied=[id]                                                

    print("age denied:",age_denied)
    # print("clearance denied:",clearance_denied)
    # print("role denied:",role_denied)
    # print("Allow access:",allow_access)
                  
            
    
astronauts=[
   ["A101",17,"commander",False],
  #  ["A102",16,"commander",False],
  #  ["A103",20,"commander",False],
  #  ["A104",35,"teacher",False],
  #  ["A105",40,"commander",True]
]

security_audit(astronauts)
