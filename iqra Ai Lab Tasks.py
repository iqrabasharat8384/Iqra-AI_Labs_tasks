task:1

a=[]
c=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
new=a+c
new.sort()
print("Sorted list is:",new)

task:2
arr = [111, 13, 25, 9, 34, 1]
n = len(arr)
arr.sort()
print("smallest element is "+str(arr[0]))
print("largest element is "+str(arr[1]))

task:3

if __name__ == '__main__':

    birthdays = {
        'iqra': '03/14/1879',
        'yasir': '01/17/1706',
        'Arsalan': '12/10/1815',
        'Ahmad': '06/14/1946',
        'Romana': '01/6/1955'}

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))
