# %%
def add_two():
    num_1 = 4
    num_2 = 5
    sum = num_1 + num_2
    print(sum)
    

add_two()
    

# %%

def areaofCircle(radius):
    pi = 3.14
    return pi *(radius * radius)
print(areaofCircle(5))

# %%
def AreaCircle(radius):
    area = 3.14 * int(radius*radius)
    return area

AreaCircle(5)



# %%
def temp_convert(celcius):
    Ftemp =  celcius * (9/5)
    return Ftemp

temp_convert(35)

# %%
def greetinga(name):
    message = name  + ''+ 'welcome to our platform'
    return message


print(greetinga('james'))
    

# %%
def season_check(month):
    if month in ['March', 'April', 'May']:
        return spring
    elif month in ['June', 'July', 'August']:
        return summer
    elif month in ['September', 'October', 'November']:
        return autumn
    else: return ('winter')
        

print(season_check('january'))

# %%

def print_list(lists):
    for i in lists:
        print(i, end='')
Months = ['jan','feb','march','april']
print (print_list(Months))


# %%


def area_Rectangle(lengt, width):
    return lengt * width
    
    
print ('area of the given triangle is' + str'area_Rectangle(5, 10)'))

# %%
def sum0f_ods(n):
    total =0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i
    return total

sum0f_ods(10)  

# %%
#WRITE A FUNCTION THAT TAKES A NUMBER AS AN ARGUMENT AND CHECKS IF IT IS EVEN OR ODD

# %%
#WRITE A FUNCTION CALLED CALCULATE_SLOPE WHICH RETURNS THE SLOPE OF A LINEAR EQUATION
#y = mx + b. THE FUNCTION TAKES IN TWO ARGUMENTS, THE RISE AND THE RUN.
#THE SLOPE IS THE RATIO OF THE RISE TO THE RUN. 
def calculate_slope(rise, run):
    if run == 0:
        return "Slope is undefined (run cannot be zero)"
    else:
        slope = rise / run
        return slope

print(calculate_slope(3, 4))  # Example usage: rise = 3, run = 4



# %%
#AX^2 + BX + C = 0
def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return "No real roots"
    
print(quadratic_formula(1, -3, 2))  # Example usage: a = 1, b = -3, c = 2 




# %%
GENERATE SIMMILAR FUNCTIONS TO THE ABOVE ONE    
def calculate_area_of_circle(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area

print(calculate_area_of_circle(5))  # Example usage: radius = 5 

def calculate_perimeter_of_circle(radius):
    pi = 3.14
    perimeter = 2 * pi * radius
    return perimeter


print(calculate_perimeter_of_circle(5))  # Example usage: radius = 5

# %%



# %%
#WRITE A FUNCTION CALLED CALCULATE_AREA WHICH RETURNS THE AREA OF A RECTANGLE.
#THE FUNCTION TAKES IN TWO ARGUMENTS, THE LENGTH AND THE WIDTH.
def calculate_area(length, width):
    area = length * width
    return area


# %%
def find_maximum(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# %%
define A FUNCTION THAT ADD ALL ODD NUMBERS IN A RANGE
def sum_of_odds_in_range(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            total += num
    return total


# %%
DEFINE A FUNCTION THAT TAKES A LIST OF NUMBERS AS AN ARGUMENT AND RETURNS  ALL EVEN NUMBERS IN THE LIST.
def find_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# %%
*args is used to pass a variable number of arguments to a function.
def sum_all (*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all(1, 2, 3, 4, 5))  # Example usage: sum of numbers from 1 to 5
    

# %%
#WRITE A FUNCTION THAT TAKES A STRING AS AN ARGUMENT AND RETURNS THE NUMBER OF VOWELS IN THE STRING.
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# %%
use first param and args to print items iteratively
# there is no limit to *args 

def print_items(first_item, *args):
    print("First item:", first_item)
    for item in args:
        print("Additional item:", item)

# %%
def dictionary_example(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
dictionary_example(name="Alice", age=30, city="New York")  # Example usage: passing keyword arguments


# %%


