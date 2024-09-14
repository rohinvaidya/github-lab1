import read_csv
import json_converter
import search
import json

def main():
    csv_file_path = 'data.csv'
    json_file_path = 'data.json'
    results_file_path = 'results.json'
    
    # Step 1: Read CSV
    csv_data = read_csv.read_csv("files/google_review_ratings.csv")
    
    # Step 2: Convert to JSON
    json_data = json_converter.convert_to_json(csv_data)
    
    # Step 3: Save JSON to file
    json_converter.save_json_to_file(json_data, json_file_path)
    
    # Print JSON data
    # print("JSON Data:\n", json_data)

    # Step 4: Search in JSON
    search_string = input("Enter a string to search in the JSON data: ")
    search_results = search.search_json(json.loads(json_data), search_string)
    
    # Print search results
    final_results = json.dumps(search_results, indent=4)
    json_converter.save_json_to_file(final_results, results_file_path)
    if len(search_results) >= 20:
        print("Search Results are too large to print in console. Please check results.json for the entire result.")
    else:
        print("Search Results:\n", final_results)

if __name__ == "__main__":
    main()