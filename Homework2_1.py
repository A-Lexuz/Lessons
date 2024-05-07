print ('Hello')

#1st block
print ('1st block')
A = int (input('Insert number, please '))
if A >= 100:
    print ('So, too much')
else:
    print ('So, too low')

#2nd block
print ('2nd block')
a = 32
b = 62
if a > b:
    print ('1-OK')

if a > b or a > 10:
    print ('2-OK')

if a > b and b != 32:
    print ('3-OK')

if a < b and (a == 32 or b == 32):
    print ('4-OK')

#3th block
print ('3th block')
x = "123"
y = '1234'

if x > y:
    print ('1-OK')

if x < y:
    print ('2-OK')

if [1,1,2,3,4] > [1,1,1]:
    print ('3-OK')

#4th block
print ('4th block')

if a != x:
    print ('1-OK')