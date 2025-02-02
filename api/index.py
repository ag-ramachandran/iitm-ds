import json
from urllib.parse import parse_qs, urlparse

def read_marks_data():
    try:
        with open('q-vercel-python.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading marks data: {e}")
        return {}
    
# Simulating a custom request handler class
class Handler:
    def __init__(self, req, res):
        self.req = req
        self.res = res

    def do_GET(self):
        # Parse query parameters from the URL
        query_params = parse_qs(urlparse(self.req.url).query)
        names = query_params.get('name', [])
        
        # Retrieve marks for each name in the query, maintain order
        marks = [read_marks_data().get(name, "Not Found") for name in names]
        
        # Prepare the response data
        response_data = {"marks": marks}
        
        # Set response status and return JSON
        self.res.status(200).json(response_data)

# Vercel serverless function handler
def handler(req, res):
    # Create an instance of the Handler class and process the request
    handler_instance = Handler(req, res)
    handler_instance.do_GET()  # Call the method to process the GET request
