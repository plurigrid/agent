import zulip
import uuid
from slugify import slugify
from PIL import Image

class ZulipUUID:
    def __init__(self, namespace=None, stream_id=None, topic_id=None, user_id=None):
        """
        Initializes a new instance of the ZulipUUID class.

        Args:
            namespace (str, optional): A namespace string to use when generating UUIDs.
            stream_id (int, optional): An integer stream ID to use when generating slugs.
            topic_id (str, optional): A string topic ID to use when generating slugs.
            user_id (int, optional): An integer user ID to use when generating slugs.
        """
        self.namespace = namespace
        self.stream_id = stream_id
        self.topic_id = topic_id
        self.user_id = user_id
        
    def _check_id(self, id_type):
        """
        Checks whether the specified ID type is set in the instance and raises a ValueError if it is not.
        """
        id_value = getattr(self, f"{id_type}_id")
        if id_value is None:
            raise ValueError(f"{id_type.upper()} ID must be specified to generate a {id_type} slug")
    
    def generate_stream_slug(self, name):
        """
        Generates a unique but readable slug for a stream using the given name.
        """
        self._check_id("stream")
        
        # Use the slugify function to create a URL-friendly version of the name
        slug = slugify(name)
    
        # Combine the slug and "stream" to form a unique but readable stream slug
        stream_slug = f"{slug}_stream"
    
        return stream_slug
    
    
    def generate_topic_slug(self, stream_id, name):
        """
        Generates a unique but readable slug for a topic in the given stream using the given name.
        """
        self._check_id("topic")
        
        # Use the slugify function to create a URL-friendly version of the name
        slug = slugify(name)
    
        # Combine the stream ID, slug, and "topic" to form a unique but readable topic slug
        topic_slug = f"{stream_id}_{slug}_topic"
    
        return topic_slug
    
    
    def generate_message_slug(self, topic_id, message_id):
        """
        Generates a unique but readable slug for a message in the given topic using the given message ID.
        """
        self._check_id("topic")
        
        # Generate a random UUID and convert it to a string
        uuid_str = str(uuid.uuid4())
    
        # Combine the topic ID, message ID, and UUID to form a unique but readable message slug
        message_slug = f"{topic_id}_{message_id}_{uuid_str}_message"
    
        return message_slug
    
    
    def generate_user_slug(self, user_id):
        """
        Generates a unique but readable slug for a user using the given user ID.
        """
        self._check_id("user")
        
        # Generate a random UUID and convert it to a string
        uuid_str = str(uuid.uuid4())
    
        # Combine the user ID and UUID to form a unique but readable user slug
        user_slug = f"{user_id}_{uuid_str}_user"
    
        return user_slug


class ZulipClient:
    def __init__(self, config):
        self.client = zulip.Client(config_file=config.ZULIP_CONFIG_PATH)
        self.config = config

    def send_message(self, stream, topic, content):
        request = {
            "type": "stream",
            "to": f"{stream}",
            "topic": f"{topic}",
            "content": f"{content}",
        }
        return self.client.send_message(request)

    def upload_image(self, stream, topic, image):
        image.save("tmp", "PNG")
        with open("./tmp", "rb") as fp:
            result = self.client.upload_file(fp)
            print(result)
            result = self.client.send_message(
                {
                    "type": "stream",
                    "to": f"{stream}",
                    "topic": f"{topic}",
                    "content": "Check out [your generated color]({}{})!".format(
                        self.config.ZULIP_BASE_URL, result["uri"]
                    ),
                }
            )
            print(result)

    def send_stream_message(self, stream, topic, content):
        return self.send_message("stream", stream, topic, content)

    def send_private_message(self, user_id, content):
        return self.send_message("private", [user_id], None, content)

    def send_help_message(self, message):
        help_text = """
        Here are some things you can ask me to do:
        - Add me to your DAO
        - Curate your lamp configuration
        """
        self.send_reply(message, help_text)

    def handle_message(self, message):
        content = message["content"]
        sender_email = message["sender_email"]

        if content == "!help":
            self.send_help_message(message)
        elif content == "Add me to your DAO":
            self.add_to_dao(sender_email)
        elif content == "Curate my lamp configuration":
            self.curate_lamp(sender_email)
        else:
            self.send_reply(message, "Sorry, I didn't understand that.")

    def send_reply(self, message, content):
        response = {"type": "private", "to": message["sender_id"], "content": content}
        return self.client.send_message(response)

    def add_to_dao(self, sender_email):
        # logic to add the sender's email to the DAO goes here
        response = (
            f"Thanks for your interest, {sender_email}! You've been added to the DAO."
        )
        self.send_private_message(sender_email, response)

    def curate_lamp(self, sender_email):
        # logic to curate the sender's lamp configuration goes here
        response = f"Thanks, {sender_email}! Your lamp configuration has been updated."
        self.send_private_message(sender_email, response)
