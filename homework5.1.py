import string
import keyword

potential_variable_names = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value',
                            'Get_value', 'get_Value', '3m', 'm3', 'assert', 'assert_exception',
                            'some_super_puper__value']

for potential_variable_name in potential_variable_names:
    if len(potential_variable_name) ==0:
       print("Incorrect variable length!")
       continue

    if potential_variable_name in keyword.kwlist:
        print(f"Error! Found {potential_variable_name} in keyword list!")
    elif potential_variable_name.find("__") != -1:
        print(f"Error! Found double '_' in {potential_variable_name} variable name!")
    elif (not potential_variable_name[0].isnumeric()
          and potential_variable_name.find(" ") == -1):
        is_correct = True
        restricted_symbols = string.punctuation.replace("_", "")
        restricted_letters = string.ascii_uppercase

        for symbol in potential_variable_name:
            if symbol in restricted_letters or symbol in restricted_symbols:
                is_correct = False
                print(f"Error! Found {potential_variable_name} in variable name!")
                break
        else:
            print(f"Keyword {potential_variable_name} is correct!")
    else:
        print(f"Error! Found {potential_variable_name} in variable name!")
