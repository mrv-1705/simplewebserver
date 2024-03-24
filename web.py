from http.server import HTTPServer, BaseHTTPRequestHandler
content="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        th{
            color: red;
        }
    </style>
</head>
<body>
    <h1>Top 5 Revenue Generating Software Companies</h1>
    <table border="2" cellspacing="10" cell padding="10" style="border: 5px solid blue; 
    font-weight: bold; 
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    ">
        <tr>
            <th>S.No</th>
            <th>Companies</th>
            <th>Revenue</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Microsoft</td>
            <td>65 Billion</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Oracle</td>
            <td>29.6 Billion</td>
        </tr>
        <tr>
            <td>3</td>
            <td>IBM</td>
            <td>29.1 Billion</td>
        </tr>
        <tr>
            <td>4</td>
            <td>SAP</td>
            <td>6.4 Billion</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Symentec</td>
            <td>5.6 Billion</td>
        </tr>
    </table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','test/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd=HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()