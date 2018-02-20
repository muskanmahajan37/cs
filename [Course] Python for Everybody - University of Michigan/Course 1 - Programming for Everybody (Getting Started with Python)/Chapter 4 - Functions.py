# Chapter Four Quiz



# 1. Which Python keyword indicates the start of a function definition?


#    def


# 2. In Python, how do you indicate the end of the block of code that makes up the function?


#    You de-indent a line of code to the same indent level as the def keyword


# 3. In Python what is the input() feature best described as?


#    A built-in function


# 4. What does the following code print out?

#    def thing():
#        print('Hello')
#
#    print('There')


#    There


# 5. In the following Python code, which of the following is an "argument" to a function?

#    x = 'banana'
#    y = max(x)
#    print(y)


#    x


# 6. What will the following Python code print out?

#    def func(x) :
#        print(x)
#
#    func(10)
#    func(20)


#    10, 20


# 7. Which line of the following Python program will never execute?

#    def stuff():
#        print('Hello')
#        return
#        print('World')
#
#    stuff()


#    print ('World')


# 8. What will the following Python program print out?

#    def greet(lang):
#        if lang == 'es':
#            return 'Hola'
#        elif lang == 'fr':
#            return 'Bonjour'
#        else:
#            return 'Hello'
#
#    print(greet('fr'),'Michael')


#    Bonjour Michael


# 9. What does the following Python code print out? (Note that this is a bit of a trick question
#    and the code has what many would consider to be a flaw/bug - so read carefully).

#    def addtwo(a, b):
#        added = a + b
#        return a
#
#    x = addtwo(2, 7)
#    print(x)


#    2


# 10. What is the most important benefit of writing your own functions?


#     Avoiding writing the same non-trivial code more than once in your program



# Chapter Four Assignments



# Assignment 4.6


def computepay(h, r):
    if h > 40:
        a = (h - 40) * (r * 0.5)
        result = h * r
        result = result + a
        return result

hrs = input("Enter Hours:")  # Enter 45
rate = input("Enter Rate:")  # Enter 10.5
hrs = float(hrs)
rate = float(rate)
p = computepay(hrs, rate)
print(p)