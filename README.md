# 3th variant:
Perform a query to the given API. I create an additional function in the utils.py file, then import it into github_graph.py to use. This function gets the necessary information to use for the frontend. The information will be displayed at http://localhost:5000/api/v1/github/x4nth055
# http://localhost:5000/api/v1/github/x4nth055:
## Retrieve GitHub User Information
This endpoint retrieves information about a GitHub user with the specified username.
## Request
Method: GET
URL: http://localhost:5000/api/v1/github/x4nth055
## Response
Status: 200
Content-Type: application/json
## Description: 
The response body contains an array of JSON objects with details of the GitHub user. Each object includes the user's login, avatar URL, size, and a list of followers with their login, avatar URL, and size.

# http://localhost:5000/api/v1/github/information/x4nth055
## Get GitHub User Information
This endpoint retrieves information about a GitHub user.
## Request
Method: GET
URL: http://localhost:5000/api/v1/github/hello/x4nth055
## Response
Status: 200 OK
Content-Type: application/json
# http://127.0.0.1:5000/api/v1/github/hello/x4nth055
This endpoint makes an HTTP GET request to retrieve information about a user on GitHub. The request should include the username in the URL path, for example, http://127.0.0.1:5000/api/v1/github/hello/x4nth055.
## Request Body
This request does not require a request body.
## Response Body
Upon a successful request, the server responds with a status code of 200 and a JSON object containing information about the user. The response includes the following fields:
message (string): A message from the server
Age (string): The age of the user
Occupation (string): The occupation of the user
Profession (string): The profession of the user
The content type of the response is application/json.

# Documentation: 
You can see the documentation in my workspace here: https://www.postman.com/aerospace-astronomer-13375905/my-workspace/documentation/euv6rf8/new-collection

