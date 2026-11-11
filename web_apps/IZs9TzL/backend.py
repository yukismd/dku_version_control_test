import dataiku

#Invalid syntax line

@app.route('/get_datasets')
def get_datasets():
    client = dataiku.api_client()
    project = client.get_project(dataiku.default_project_key())
    return json.dumps(project.list_datasets())