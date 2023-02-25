from agents.base_agent import BaseAgent


class ValueAgent(BaseAgent):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.values = {}

    def handle_message(self, message):
        if message["content"] == "GM":
            # Send a DM to the user to start value elicitation
            self.client.send_message(
                {
                    "type": "private",
                    "to": message["sender_email"],
                    "content": "Hello! I'm the value elicitation agent. Can you tell me a bit about your personal values?",
                }
            )
        else:
            # Parse the message and update the user's values
            # Assumes messages will be of the format "key: value"
            key, value = message["content"].split(":")
            self.values[key.strip()] = value.strip()

            # Send a confirmation message to the user
            self.client.send_message(
                {
                    "type": "private",
                    "to": message["sender_email"],
                    "content": f"Thanks for sharing! I've updated your {key.strip()} value to {value.strip()}.",
                }
            )

    def summarize_values(self):
        # Generate a summary of all users' values
        # Assumes self.values is a dictionary with keys = user IDs and values = dictionaries of key-value pairs
        summary = {}
        for user_values in self.values.values():
            for key, value in user_values.items():
                if key not in summary:
                    summary[key] = {value: 1}
                else:
                    if value not in summary[key]:
                        summary[key][value] = 1
                    else:
                        summary[key][value] += 1

        return summary

    def group_users(self):
        # Group users together based on shared values
        # Assumes self.values is a dictionary with keys = user IDs and values = dictionaries of key-value pairs
        groups = []
        for user_id1, user_values1 in self.values.items():
            group_found = False
            for group in groups:
                for user_id2 in group:
                    user_values2 = self.values[user_id2]
                    if all(
                        key in user_values2 and user_values2[key] == user_values1[key]
                        for key in user_values1
                    ):
                        group.append(user_id1)
                        group_found = True
                        break
                if group_found:
                    break
            if not group_found:
                groups.append([user_id1])
        return groups
