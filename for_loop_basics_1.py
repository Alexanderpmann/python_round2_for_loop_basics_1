# 1. Basic - Print all integers from 0 to 150
for i in range (0,151):
    print (i); 

# 2. Multiples of Five - print all the multiples of 5 from 5 to 1,000
for i in range (5, 1001):
    if i % 5 == 0:
        print (i);

# 3. Counting, The Dojo Way - Print integers 1 to 100 - fi divisible by 5, print "Coding" instead, if divisible by 10, print 'Coding Dojo' 
for i in range (0,101):
    if i % 5 == 0:
        print ('Coding')
    if i % 10 == 0:
        print ('Coding Dojo')
        print (i);

# 4. Whoa. That Suck's Huge 0 add off integers from 0 to 500,000 and print the final sum 
sum = 0
for i in range (0,500001):
    sum += i
print(sum);

# 5. Countdown by Fours - print positive numbers starting at 2018, counting down by 4s
count = 2018
while count > 0:
    print (count)
    count = count - 4;

# 6. Flexible Counter - Set 3 variables - lowNum, highNum, and mult. starting at lowNum and going through highNum, print only integers that are multiple of mult. 
# ex. lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print (i);