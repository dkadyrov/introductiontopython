#%%
def my_function(
        my_string: str, 
        number: int = 2, 
        dictionary: dict = {}
) -> dict:
    """
    This function takes a string, a number, and a dictionary as input parameters and returns the dictionary with the number assigned to the string key.
    """
    if not isinstance(number, int): 
        raise "Needs to be an integer"
    
    if not isinstance(my_string, str):
        raise "Needs to be a string type"
    
    if not isinstance(dictionary, dict):
        raise "Need to be dictionary type"    
    
    dictionary[my_string] = number
    
    return dictionary
# %%
# dictionary_1 = {
#     "daniel": 2
# }

# my_function("kadyrov", 10, dictionary=dictionary_1)

# #%%
# dictionary_2 = my_function("blank")
#%%