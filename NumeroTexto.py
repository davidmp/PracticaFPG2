num = '1234'
number = int(num) # Convert the string to an integer
one_ten=['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
ten_nineteen=['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
twenty_ninety=[' ', ' ','veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
temp_str = ""
if number == 0: # If the string given equals to 0
    temp_str = 'cero ' # Assign the word zero to the var temp_str
# Do the calculation to find each digit of the str given
first_digit = number // 1000
second_digit = (number % 1000) // 100
third_digit = (number % 100) // 10
fourth_digit = (number % 10)
print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)
if first_digit > 0: 
    if first_digit == 1:
        temp_str = temp_str + 'mil '
    else:
        temp_str = temp_str + one_ten[first_digit] + ' mil '
# one_ten[first_digit] gets you the number you need from one_ten and you add thousand (since we're trying to convert to words ofc)
# You do the same for the rest...
if second_digit > 0:
    if second_digit == 1:
        temp_str = temp_str + ' ciento '
    else:
        temp_str = temp_str + one_ten[second_digit] + ' cientos '
if third_digit > 1:
    temp_str = temp_str + twenty_ninety[third_digit] + " "
if third_digit == 1:
    temp_str = temp_str + ten_nineteen[fourth_digit] + " "
else:
    if fourth_digit:
        temp_str = temp_str + 'y ' + one_ten[fourth_digit] + " "
if temp_str[-1] == " ": # If the last index is a space
    temp_str = temp_str[0:-1] # Slice it 
print(temp_str)