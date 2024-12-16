# JSON-LD Data Conversion Project

This project demonstrates the conversion of tabular data into JSON-LD format following a specified ontology. It includes sample data and a conversion script that maintains semantic relationships and proper JSON-LD structure.

## Project Structure

```
project/
├── context.json         # JSON-LD context definitions
├── projects.csv         # Sample input data
├── converter.py         # Conversion script
├── output.jsonld        # Generated JSON-LD output
└── README.md           # Project documentation
```

## Prerequisites

- Python 3.7+
- Basic understanding of JSON-LD and data ontologies

## Setup and Usage

1. Ensure all files are in the same directory
2. Run the converter script:
   ```bash
   python converter.py
   ```
3. The script will generate `output.jsonld` containing the converted data

## Data Structure

The sample implementation includes the following classes and properties:

### Project
- name (string)
- description (text)
- dateCreated (date)
- author (Person)
- department (string)
- location (Place)
- status (string)
- priority (string)
- assignedTo (Person)
- dueDate (date)
- tags (array of strings)
- relatedProjects (array of Project references)

### Person
- name (string)

### Place
- name (string)

## Ontology

The project uses a combination of Schema.org vocabulary and custom terms:
- schema: http://schema.org/
- ex: http://example.com/ontology# (custom terms)

## Extending the Project

To extend this implementation:
1. Add new properties to the context.json file
2. Update the CSV structure with new columns
3. Modify the converter.py script to handle new data types or relationships

## Notes

- The sample data is fictional and meant for demonstration purposes
- The ontology can be extended based on specific requirements
- The converter handles basic data types and relationships but can be enhanced for more complex scenarios
