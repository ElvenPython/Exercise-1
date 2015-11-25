# Copyright (c) 2015,Vienna University of Technology,
# Department of Geodesy and Geoinformation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Vienna University of Technology,
#      Department of Geodesy and Geoinformation nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
In this module you will define several functions.

Please document your functions according to
https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
'''

# Example so that you can see a passing test


def f():
    """Returns the string 'success'
    """
    return "success"

##############################
# Basic function definitions #
##############################

# Define a function named add that takes two numbers and returns the sum.
def add(a,b):
	"""Returns the sum of two given numbers.
	
	Adds variables a and b an returns the result:
	
	Parameters
	----------
	a : int	
		First number to be added to.
	b : int	
		Number added to a.
	
	Returns
	-------
	sum : int
		Result of addition
	"""
	
	sum = a + b
	return sum

# Define a function named to_tuple that takes three arguments and returns a
# tuple of these three arguments.
def to_tuple(arg1, arg2, arg3):
	"""Returns a tuple of arguments
	
	Takes 3 arguments and returns a tupel.
	
	Parameters
	----------
	arg1, arg2, arg3 : optional
		Arguments formed into a tupel.
		
	Returns
	-------
	tuple : tuple
		Tuple of all the arguments
	"""
	tuple = (arg1, arg2, arg3)
	return tuple

# Define a function named check5 that checks if a number is greater than 5 and
# returns True or False.
def check5(a):
	"""Checks if number is greater than a reference number.
	
	Takes a given number to check if it is greater than 5.
	
	Parameters
	----------
	a : int
		Number given to be checked.
		
	Returns
	-------
	True	
		If number is greater than 5.
	False	
		If number is smaller than 5.
	
	"""
	if (a>5):
		return True
	else:
		return False

# Define a function named check_n that checks if a number is greater than n. The
# number should be the first argument and n the second
def check_n(num, n):
	"""Checks two numbers.
	
	Takes a given number and checks if it is greater than n.
	
	Parameters
	----------
	num : int
		Given number to be checked.
	n : int
		Reference number.
	
	Returns
	-------
	True
		If num is greater than n.
	False
		If num is smaller than n.
	"""
	if (num > n):
		return True
	else:
		return False

#########
# LISTS #
#########

# Define a function named check_list that takes two arguments. The first
# argument is a list of numbers and the second argument is the number n to
# compare against. The function should return a list with equal length as the
# input list containing for each number in the original list either True or
# False if the number was greater than or equal to n.
def check_list(list, n):
	"""Checks list to number.
	
	Runs n over list and returns a list containing
	True or False if value is greater or equal to n.
	
	Parameters
	----------
	list : list
		list of numbers.
	n : int
		Reference number
		
	Returns
	-------
	result : list	
		Containing True or False values
	
	"""
	result = [x >= n for x in list]
	return result

# Define a function named check_list_nth that does the same as check_list but
# uses every nth element of the input list (including the first one). You will
# need a third input argument.
def check_list_nth(list, n, nth):
	"""Checks list to number.
	
	
	
	"""
	result = [x >= n for x in list[0::nth]]
	return result

# Define a function named add_new_list that takes two inputs. A list l and a
# second variable x to add to the list. Return a new list containing x as the
# last element without modifying the original list.
def add_new_list(l, x):
	"""Appending a new element to a list.
	
	Appends an element to a list without modifying original.
	
	Parameters
	----------
	l : list
		List of values.
	x : optional
		Element that is to be added.
		
	Returns
	-------
	l : list
		New list with added element.
	"""
	lnew = l.copy()
	lnew.append(x)
	return l	

# Define a function named remove_nth that takes a list and removes every nth
# element (including the first one). Use a keyword named nth to set the default
# value for nth to 2.
def remove_nth(list, nth=2):
	"""Remove elements.
	
	Removes every nth element from a lisst.
	
	Parameters
	----------
	list: list
		List of elements.
	nth : int
		Index for removing element from list.
		
	Returns
	-------
	l : list
		A list without every nth element.
	"""
	l = list.copy()
	del l[0::nth]
	return l

# Define a function named search_n that takes a list and a variable x and
# searches for x in the list. If the variable is found return the index of the
# variable in the list and the variable. Otherwise use None for both return
# values
def search_n(list, x):
	"""Searches for an element.
	
	Looks for a certain element in a list.
	
	Parameters
	----------
	list : list
		A list of elements.
	x : object
		Reference variable
		
	Returns
	-------
	x, index(x) : tuple
		If variable is in list.
	None
		If nothing is found.	
	"""
	if x in list:
		return (list.index(x), x)
	else:
		return (None, None)

################
# Dictionaries #
################

# Define a function named args_to_dict that takes three arguments and returns a
# dictionary with the position of the argument as the key (starting at 0) and
# the argument as the value.
def args_to_dict(arg1, arg2, arg3):
	"""Makes a dictionary.
	
	Takes three arguments and returns a dictionary.
	
	Parameters
	----------
	arg1, arg2, arg3 : object
		Arguments that come into the dictionary.
	
	Returns
	-------
	dict
		
	"""
	return {0: arg1, 1: arg2, 2: arg3}

# BONUS: Write a function named args_to_dict_general that does the same for any
# number of arguments
def args_to_dict_general(*args):
	"""Makes a dictionary out of arguments.
	
	Makes a dictionary out of any number of given arguments.
	
	Parameters
	----------
	args : object
		Various arguments
		
	Returns
	-------
	d : dict
		Dictionary consisting of args.
	"""
	counter = 0
	d = {}
	for x in args:
		d[counter] = x
		counter += 1
	return d
# Define a function named lists_to_dict that takes two lists of equal length
# named keys and values and builds a dictionary out of them.
def lists_to_dict(keys, values):
	"""Makes a dictionary.
	
	Takes two lists and makes a dictionary out of them.
	
	Parameters
	----------
	keys, values : list
		Lists of equal length
		
	Returns
	-------
	dict
	"""
	return dict(zip(keys, values))

# Define a function named search_list that takes two lists a and b. The
# function searches for all elements of b in list a. The return value should be
# a dictionary containing the index of the found element of b in list a and the
# value of the found element. If nothing was found then return an empty
# dictionary.
def search_list(a,b):
	"""Searches lists.
	
	Searches a list for values of another list.
	
	Parameters
	----------
	a, b : list
		List that is searched through and a reference list
	
	Returns
	-------
	d : dict
		Containing index of found element and value
	"""
	d = {}
	for x in a:
		if x in b:
			d[a.index(x)] = x
	return d

# Define a function named dict_to_string that takes a dictionary and a
# separator string. The function should only take elements out of the
# dictionary whose value is a string and then return a single string containing
# the strings stored in the dictionary seperated by the separator string.
# Return an empty string if there are no strings in the dictionary.
def dict_to_string(dict, string):
	"""Searches for strings.
	
	Searches through a dictionary to find the strings.
	
	Parameters
	----------
	dict : dict
		Dictionary that is to be searches through
	string : string
		Seperator string
		
	Returns
	-------
	st : dict
		Containing all strings.
	st : string
		Empty if no string found
	"""
	st = ''
	for key in dict:
		if(type(dict[key]) == str):
			st += dict[key]+string
	return st[0:len(st)-1]

# Define a function named classify_by_type which takes a list l and returns a
# dictionary d. The d must have the keys 'int' and 'str' which contain the
# elements out of l that have this type. Elements that do not fit one of these
# two types should be stored in a list under the key 'others'
def classify_by_type(l):
	"""Checks types of a list.
	
	Checks the type of elements in a list
	and stores them in three lists: int, string and other.
	
	Parameters
	----------
	l : list
		List that has values with different types
		
	Returns
	-------
	dict
		Dictionary containing the three type-lists
	"""
	list_int = []
	list_str = []
	list_other = []
	for x in l:
		if(type(x) == int):
			list_int.append(x)
		elif (type(x) == str):
			list_str.append(x)
		else:
			list_other.append(x)
	return {'int': list_int, 'str': list_str, 'others':list_other}
	