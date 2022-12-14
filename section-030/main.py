#FileNotFound

try:
    file =  open("section-030/exercises/a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    # print("There was an error!")
    
    #if error = create the file
    file = open("section-030/exercises/a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist!")
else:
    content = file.read()
    print(content)
finally:
    raise 
        