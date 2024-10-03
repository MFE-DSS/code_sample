import dataiku
import base64
import markdown
import requests

# Connect to Dataiku project
client = dataiku.api_client()
project = client.get_project("<PROJECT_KEY>")

# Get the project flow
flow = project.get_flow()

# Managed folder to store the ZIP
folder = dataiku.Folder("<SOME_MANAGED_FOLDER>")

# Generate flow documentation
flow_documentation = flow.generate_documentation()

# Download the flow documentation ZIP
folder.upload_stream(
    "flow_export.zip",
    flow.download_documentation_stream(flow_documentation.wait_for_result()['exportId'])
)

# Extract the flow image from the ZIP file (assuming the image name is known)
import zipfile
with folder.get_download_stream("flow_export.zip") as f:
    with zipfile.ZipFile(f) as z:
        flow_image_data = z.read("<FLOW_IMAGE_NAME>.png")

# Encode the image in Base64
encoded_image = base64.b64encode(flow_image_data).decode('utf-8')


# Identify the wiki article
article_id_or_name = "<ARTICLE_ID_OR_NAME>"
wiki_article = project.get_wiki().get_article(article_id_or_name)
article_data = wiki_article.get_data().article_data

# Convert markdown to HTML
html_article_content = markdown.markdown(article_data)


# Create the HTML content for the email
email_content = f"""
<html>
<body>
    <h1>Flow Image</h1>
    <img src="data:image/png;base64, {encoded_image}" alt="Flow Image">

    <h1>Wiki Content</h1>
    <div>{html_article_content}</div>
</body>
</html>
"""
# Example of sending email : use DSS's scenarios object like Reporter or scenario send email step.
