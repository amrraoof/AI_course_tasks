import math
def laws():
    Shape_Type = int(input("please enter [1 for triangle,2 for square,3 for rectangle,4 for rhombus,5 for parallelogram,6 for circle]: "))
    
    if Shape_Type == 1:
 
        First_Rib= float(input("Please enter 1st rib length: "))
        Second_Rib= float(input("Please enter 2nd rib length: "))
        Angel_Betwen = float(input("Please enter angle betwen: "))
        Third_Rib = float(input("Please enter 3ed rib length: "))
        
        Tri_Area =0.5*(First_Rib)*(Second_Rib)*(math.sin((Angel_Betwen)*(math.pi/180)))
        Tri_Circumference = (First_Rib)+(Second_Rib)+(Third_Rib)
        print("The triangle area is: %s and triangle circumference is: %s" %(Tri_Area,Tri_Circumference) )
        
    elif Shape_Type == 2 :
        
        Rib_length = float(input("Please enter rib length: "))
        Square_area = (Rib_length)**2
        Square_Circumference = 4*(Rib_length)
        print("square area is: %s and Square circumference is: %s " %(Square_area,Square_Circumference))
        
    elif Shape_Type == 3 :
        
        First_r_Rib = float(input("Please enter 1st rib length: "))
        Second_r_Rib= float(input("Please enter 2nd rib length: "))
        Rectangle_Area = (First_r_Rib)*(Second_r_Rib)
        Rectangle_Circumference = 2*((First_r_Rib)+(Second_r_Rib))
        print("rectangle area is: %s and rectangle circumference is: %s " %(Rectangle_Area,Rectangle_Circumference))

    elif Shape_Type == 4:
        
        Base_Length = float(input("Please enter base length: "))
        Height_Length = float(input("Please enter height length: "))
        Rhombus_Area = (Base_Length)*(Height_Length)
        Rhombus_Circumference = 4*(Base_Length)
        print("Rhombus area is: %s and Rhombus circumference is: %s " %(Rhombus_Area,Rhombus_Circumference))
    
    elif Shape_Type == 5:
        
        First_Rib= float(input("Please enter 1st rib length: "))
        Second_Rib= float(input("Please enter the length of the rib next to 1st rib: "))
        Height_length= float(input("Please enter the length of the corresponding height of the 1st rib: "))
        
        Parallalogram_Area = (First_Rib)*(Height_length) 
        Parallalogram_Circumference = 2*((First_Rib)+(Height_length))
        print("Parallalogram area is: %s and Parallalogram circumference is: %s " %(Parallalogram_Area,Parallalogram_Circumference))
      
    elif Shape_Type == 6:
        
        Radius_length = float(input("Please enter radius length: "))
        
        Circlur_Area  = (math.pi*(Radius_length**2))
        Circlur_Circumference = 2*(math.pi)*(Radius_length)
        print("Circlur area is: %s and Circlur circumference is: %s " %(Circlur_Area,Circlur_Circumference))