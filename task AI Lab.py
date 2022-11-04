try:
       n=int(input("Enter a number..."))
       reversed =0
       while(n!=0):
              r=int(n%10)
              reversed=reversed*10+r
              n=int(n/10)
              print(reversed)

except valueError:
       print("Given input is not a number!!!!!!!")

list =[234,123,333,777]
print("The orignal list is >>>>",list)
odd_sum =0
even_sum=0
for sub in list:
       for ele in str(sub):
              if int(ele)%2 ==0:
                     even_sum += int (ele)
              else:
                     odd_sum += int (ele)

print("odd  digit sum >>>>" + str(odd_sum))
print("Even  digit sum >>>>" + str(even_sum))


nterms =int(input("How many terms??"))
n1=0
n2=1
count = 0

if nterms <=0:
       print("Enter the Positive integers....")
elif nterms== 1:
       print("Fibobacci sequence upto" ,nterms,":")
       print(n1)

else:
       print("fibonacci sequence : ")
       while count < nterms:
              print(n1)
              nth=n1+n2
              n1=n2
              n2=nth
              count+=1

print("Enter the marks obtained in 5 subjects")
marks_one=int(input())
marks_two=int(input())
marks_three=int(input())
marks_four=int(input())
marks_five=int(input())
average=marks_one + marks_two + marks_three + marks_four+marks_five/5
if average>=81 and average>=90:
       print("Got Grade A")
elif average>=81 and average>=90:
       print("Got Grade B")
elif average>=71 and average>=80:
       print("Got Grade c")
elif average>=61 and average>=70:
       print("Got Grade d")
elif average>=51 and average>=60:
       print("Got Grade E")
elif average <50:
       print("you are fail!!!!")
else:
       print("invalid")


um = int(input("Enter a number >>>>> "))
fac =1
if num< 0:
       print("sorry, factorial does not exist for negative numbers")
elif num==0:
       print("the factorial of 0 is 1")
else:
       for i in range (1, num+1):
              fac=fac*i
              print("The Factorial of", num, "is",fac)
                            
