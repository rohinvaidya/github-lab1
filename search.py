import json
import json_converter

def search_json(json_data, search_string):
    results = []

    print("You have entered: " + search_string)

    for i in range(0, len(json_data)):
        # Create an object that stores a Single Object from the JSON file
        temp = json_data[i]
        # Iterate through the single object to search for the search_string
        for key in temp:
            # Check if the object key matches with the search_string
            if(key.casefold().startswith(search_string.casefold())):
                results.append(temp)
                break
            elif(key.casefold().endswith(search_string.casefold())):
                results.append(temp)
                break
            elif(key.casefold() == search_string.casefold()):
                results.append(temp)
                break
            # Check if the object value matches with the search_string
            if(temp[key].casefold().startswith(search_string.casefold())):
                results.append(temp)
                break
            elif(temp[key].casefold().endswith(search_string.casefold())):
                results.append(temp)
                break
            elif(temp[key].casefold() == search_string.casefold()):
                results.append(temp)
                break

    if(results == []):
        print("No match found!")
    else:
        print("Result has been found and saved to results.json")
        json_converter.convert_to_json(results)

    return results