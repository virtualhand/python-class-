#ls1=["Mombasa", ["Kitale", ("Eldoret", "Fill"),("Nakuru")]]
#print(ls1[1][1][1])


#if "Fill" in ls1[1][1]:
 #   ls1[1][1] = ("Eldoret", "Machakos")
    
#print(ls1)

#name=input("what is your name")

#age =input("input your age: ")
#if avg > 18:
  #    print("you are of right age")
 #     print("now you may get a liscence")
#else:
 #     print("you are edge is not elidgble")
#      print ("your age is below reqirements")

#print("this will run either way")

#avg=60

#if avg >=70:
    #print("A")
#elif avg >=60 and avg<70:
 #   print("B")
#elif avg >=50 and avg <60:
 #   print("C")
#elif avg>=40 and avg <50:
 #   print("D")
#else:
  # print("E")
 # 

#num1=input("input your number:")
#num2=input("input your number:")
#num3=input("input your number:")
#if num1>num2 and num1>num3:
 #   print(num1)
#elif num2>num1 and num2>num3:
 #   print(num2)    
#elif num3>num1 and num3>num2:
 #   print(num3)
#else:
 #   print("no one won")


try:
  marks = float(input("enter marks:"))

  if marks < 40:
      print("E")
  else:
      if marks >= 40 and marks < 50:
          print("D")
      else:
          if marks >=50 and marks < 60:
              print("C")
          else:
              if marks >=60 and marks < 70:
                  print("B")
              else:
                  print("A")  
except Exception as chris:
    print(chris)
                 
            
                
          
