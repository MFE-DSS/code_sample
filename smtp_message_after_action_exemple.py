# Implementing custom alerting through the various dataiku code features
import smtplib
from email.message import EmailMessage
# In this example we considere using it after a project deployment. 
def post_action_message(project_key, bundle_id, client, sender_email, recipient_email):
    """
    Publishes a bundle for a project and sends an email notification.

    :param project_key: Unique key for the project in the data platform.
    :param bundle_id: Identifier of the bundle to be published.
    :param client: Instance of the API client for interacting with the data platform.
    :param sender_email: Email address of the sender.
    :param recipient_email: Email address of the recipient.

    """
    try:
        # get the project
        project = client.get_project(project_key)
        
        # Publish the bundle into the deployer node
        project.publish_bundle(bundle_id)
        
        # Config email content
        msg = EmailMessage()
        msg.set_content(f"The bundle {bundle_id} has been successfully published for the project {project_key}.")
        
        # head, send and recipient
        msg['Subject'] = 'Successful Bundle Publication'
        msg['From'] = sender_email
        msg['To'] = recipient_email
        
        # use smtp protocol
        with smtplib.SMTP('localhost') as smtp:
            smtp.send_message(msg)

    except Exception as e:
        logging.error(f"Failed to publish bundle {bundle_id} for project {project_key}: {e}")
