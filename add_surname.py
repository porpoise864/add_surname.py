# Author: Sarah Oertly
# Date: 11/4/2019
# Description: Write a function named add_surname that takes as a parameter a list of first names. It should use a list
# comprehension to return a list that contains only those names that start with a "K", but with the surname "Kardashian"
# added to each one, with a space between the first and last names.
first_name = ["Kathy","Krystal","Kerrie","Kristine","Kiara"]
last_name = ["Kardashian"]
def add_surname(first_name):
    name1 = first_name[0:4] + last_name
    name2 = first_name[6:12] + last_name
    name3 = first_name[14:19] + last_name
    name4 = first_name[21:28] + last_name
    name5 = first_name[30:34] + last_name
