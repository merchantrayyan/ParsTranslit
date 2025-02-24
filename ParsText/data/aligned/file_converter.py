import csv
import json

def txt_to_csv_and_json(txt_file, csv_file, json_file):
    farsi_tajik_pairs = []
    
    # Read the parallel corpus data from the .txt file
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            farsi_sentence = lines[i].strip()
            tajik_sentence = lines[i+1].strip()
            farsi_tajik_pairs.append({'farsi': farsi_sentence, 'tajik': tajik_sentence})
    
    # Write to CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['farsi', 'tajik']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for pair in farsi_tajik_pairs:
            writer.writerow(pair)
    
    # Write to JSON file
    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(farsi_tajik_pairs, jsonfile, ensure_ascii=False, indent=4)

# Replace 'input.txt' with the name of your input file
txt_to_csv_and_json('txt/bbc.txt', 'csv/bbc.csv', 'json/bbc.json')
txt_to_csv_and_json('txt/jj.txt', 'csv/jj.csv', 'json/jj.json')
txt_to_csv_and_json('txt/dr.txt', 'csv/dr.csv', 'json/dr.json')
