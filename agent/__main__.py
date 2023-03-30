import argparse
from agent.agents.digital_twin import DigitalTwin
from agent.agents.ontology_agent import OntologyAgent
from agent.config import config
from agent.agents.play_coplay_agent import PlayCoplayAgent


def run():
    parser = argparse.ArgumentParser(description="Agent")
    parser.add_argument(
        "--agent",
        choices=["play_coplay", "digital_twin", "ontology"],
        help="Specify which agent to run",
        required=True,
    )
    parser.add_argument(
        "--mode",
        choices=["zulip", "discord", "repl", "gradio", "fastapi"],
        help="Specify the mode to run in",
        required=True,
    )
    parser.add_argument(
        "--path",
        help="Specify the path to a knowledge base to index",
        required=False,
    )
    args = parser.parse_args()
    if args.agent == "play_coplay":
        agent = PlayCoplayAgent(config.Config(), mode=args.mode)
    elif args.agent == "ontology":
        if args.path is None:
            raise ValueError("Must specify a knowledge base path")
        c = config.Config()
        c.set("DATA_DIR", args.path)
        agent = OntologyAgent(c, mode=args.mode)
    elif args.agent == "digital_twin":
        agent = DigitalTwin(config.Config(), mode=args.mode)
    else:
        raise ValueError(f"Invalid agent: {args.agent}")
    agent.run()


if __name__ == "__main__":
    run()
