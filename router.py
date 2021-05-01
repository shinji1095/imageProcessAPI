from controller import *

app.add_api_route("/", index)
app.add_api_route("/process", process, methods=["POST"])