# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = 'supercalifragilisticexpialidocious'
string_list = list(string)
string_list.sort()
string = "".join(string_list)
print(string)