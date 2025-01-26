from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

class Handler(BaseHTTPRequestHandler):

    def load_marks(self):
        """Load marks from the marks.json file."""
        try:
            with open('q-vercel-python.json', 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading marks data: {e}")
            return {}

    def do_GET(self):
        # Parse query parameters
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        # Get names from query parameters
        names = query_params.get('name', [])
        
        # Load marks data from file
        marks_data = self.load_marks()

        # Find the marks for the names
        marks = [marks_data.get(name, 0) for name in names]

        # Return the response
        response = {
            "marks": marks
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())