import csv
import json
from datetime import datetime

def load_context():
    """Load the JSON-LD context from file"""
    with open('context.json', 'r') as f:
        return json.load(f)

def csv_to_jsonld(csv_file, context):
    """Convert CSV data to JSON-LD format"""
    projects = []
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Process tags and related projects from semicolon-separated strings
            tags = row['tags'].split(';') if row['tags'] else []
            related_projects = row['relatedProjects'].split(';') if row['relatedProjects'] else []
            
            project = {
                "@context": context['@context'],
                "@type": "schema:Project",
                "@id": f"http://example.com/projects/{row['id']}",
                "name": row['name'],
                "description": row['description'],
                "dateCreated": row['dateCreated'],
                "author": {
                    "@type": "schema:Person",
                    "name": row['author']
                },
                "department": row['department'],
                "location": {
                    "@type": "schema:Place",
                    "name": row['location']
                },
                "status": row['status'],
                "priority": row['priority'],
                "assignedTo": {
                    "@type": "schema:Person",
                    "name": row['assignedTo']
                },
                "dueDate": row['dueDate'],
                "tags": tags,
                "relatedProjects": [
                    {
                        "@type": "schema:Project",
                        "@id": f"http://example.com/projects/{proj_id}"
                    } for proj_id in related_projects
                ]
            }
            projects.append(project)
    
    return {
        "@context": context['@context'],
        "@graph": projects
    }

def main():
    # Load context
    context = load_context()
    
    # Convert CSV to JSON-LD
    jsonld_data = csv_to_jsonld('projects.csv', context)
    
    # Write output to file
    with open('output.jsonld', 'w', indent=2) as f:
        json.dump(jsonld_data, f, indent=2)

if __name__ == "__main__":
    main()
