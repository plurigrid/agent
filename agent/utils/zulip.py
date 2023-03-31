import zulip
import uuid
from slugify import slugify
import os


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
            raise ValueError(
                f"{id_type.upper()} ID must be specified to generate a {id_type} slug"
            )

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


import configparser


class ZulipClient:
    def __init__(self, msg_handler):
        config_path = os.path.expanduser("~/zuliprc")
        if not os.path.exists(config_path):
            raise ValueError(f"Configuration file not found at: {config_path}")

        config = configparser.ConfigParser()
        config.read(config_path)

        bot_key = config.get("api", "key", fallback=None)
        bot_email = config.get("api", "email", fallback=None)
        server_url = config.get("api", "site", fallback=None)

        print(bot_key)
        print(bot_email)
        print(server_url)

        if bot_email is None:
            raise ValueError("BOT_EMAIL config variable not set.")
        if server_url is None:
            raise ValueError("SERVER_URL config variable not set.")
        if bot_key is None:
            raise ValueError("ZULIP_API_KEY config ariable not set.")

        self.client = zulip.Client(api_key=bot_key, email=bot_email, site=server_url)
        self.msg_handler = msg_handler

    def run(self):
        print("waiting for messages..")
        self.client.call_on_each_message(
            lambda msg: self.respond_to_message(msg, self.msg_handler)
        )

    def send_message(self, message_type, stream, topic, content):
        request = {
            "type": message_type,
            "to": f"{stream}",
            "topic": f"{topic}",
            "content": f"{content}",
        }
        return self.client.send_message(request)

    def respond_to_message(self, msg, msg_handler):
        print(msg)
        stream = msg["stream_id"]
        topic = msg["subject"]
        output = msg_handler(msg["content"])
        self.send_message("stream", stream, topic, output)

    def send_stream_message(self, stream, topic, content):
        return self.send_message("stream", stream, topic, content)

    def send_private_message(self, user_id, content):
        return self.send_message("private", [user_id], None, content)

    def send_reply(self, message, content):
        response = {"type": "private", "to": message["sender_id"], "content": content}
        return self.client.send_message(response)
