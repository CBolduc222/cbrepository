##### ASSIGNMENT STARTS HERE #####


#%%
# First Assignment
'''
1: Please create a program which inputs two years and outputs the years as well as the difference
between them!

Your output should look like:

Year 1: 2025
Year 2: 2028
Difference: 3
'''

year1 = (input ("What is the first year you want calculated? "))
year2 = (input ("What is the second year you want calculated? "))


print ("Year 1:", (year1))
print ("Year 2:", (year2))

if year1 >= year2:
    print ("Difference:", (int(year1) - int(year2)))
else:
    print ("Difference:", (int(year2) - int(year1)))


#%%
# Second Assignment

'''
2: Please create a program which collects an input as fahrenheit and outputs the 
temperature in celsius

Your output should look like:

Fahrenheit: 25
Celsius: -3.89
'''

fahrenheit = float(input ("Please enter the fahrenheit to be converted to celsius "))
celpt1 = (fahrenheit - 32)
celpt2 = celpt1 * 5/9

print ("Fahrenheit:", (fahrenheit))
print ("Celsius:", (celpt2))


#%%
# Third Assignment

'''

3: Please create a program which collects an input as US Dollars and converts the output to Euros 
given the exchange rate on 1/19/25 as 1 USD = 0.97 Euro

Your output should look like:
USD: 1
EU: 0.97

'''

dollar = float(input ("Enter the amount in US dollars you want to convert to Euro "))
euro = dollar * 0.97

print ("USD:", (dollar))
print ("EU:", (euro))


##### ASSIGNMENT ENDS HERE #####


# %%

# %%
