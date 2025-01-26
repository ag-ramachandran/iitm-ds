import json
import urllib.parse

def handler(request):
    # Load marks data from file
    def load_marks():
        try:
            with open('q-vercel-python.json', 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading marks data: {e}")
            return {}

    # Parse query parameters
    query_params = urllib.parse.parse_qs(request.query_string)
    names = query_params.get('name', [])

    # Load marks data from file
    marks_data = load_marks()

    # Find the marks for the names
    marks = [marks_data.get(name, 0) for name in names]

    # Return the response
    return {
        "statusCode": 200,
        "body": json.dumps({"marks": marks}),
        "headers": {
            "Content-Type": "application/json"
        }
    }
