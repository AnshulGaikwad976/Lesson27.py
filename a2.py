dividend= int(input("Enter dividend :"))
divisor = int(input("Enter divisor: "))

if divisor == 0:
   print("Cannt divide by zero")

else:
   quotient = 0
   remaining =dividend

   while remaining >= divisor:
         temp = divisor 
         count = 1

         while (temp<<1)<=remaining:
               temp=temp << 1
               count= count << 1
         remaining = remaining-temp
         quotient=quotient + count
   print("quotient: ",quotient)
   print("remainder: ",remaining)           
