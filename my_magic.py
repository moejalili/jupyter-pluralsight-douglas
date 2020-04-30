import re

# @register_cell_magic       remove this the decoratoe because there is no need for this scenario 
def count_magic(line, cell):
    content = re.sub('[^A-Za-z0-9]', ' ', cell)     # remove all of the non-alphanumeric characters
    content = re.sub('\s+', ' ', content)           # remove multiple whitespace characters
    return len(content.lower().split(' '))          # splits on whitespace to get the number of words



#  Next, I'll write a function named load_ipython_extension. Jupyter Notebook will use this function in order to load the magic command. The argument to this function implements the register_magic_function method, which takes the name of a function to register as a magic and a string as to what kind of magic, cell in this case. 

def load_ipython_extension(ipython):                      
    ipython.register_magic_function(count_magic, 'cell')