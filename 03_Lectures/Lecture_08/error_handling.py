#%%
def test_if_string(parameter): 
    if isinstance(parameter, str):
        return "This is a string"

    if isinstance(parameter, int):
        return "This is a int"
    

test_if_string("test")

test_if_string(1)

# %%
def convert_string_to_int(string):
    try:  
        return int(string)
    except Exception as e: 
        return f"Received this error: {e}"

convert_string_to_int("test")

# %%
