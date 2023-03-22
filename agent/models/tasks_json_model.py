from langchain import LLMChain, OpenAI, PromptTemplate
import json


class TasksJsonModel:
    # temporary: serialize tasks to file for debugging
    def __init__(self, tasks_path="./tasks.json"):
        self.tasks_path = tasks_path

    def get_tasks_for_person(self, name):
        with open(self.tasks_path, "r") as f:
            tasks_json = f.read()
            tasks = self.get_tasks_for_name(tasks_json, name)
        return tasks

    def get_tasks_for_name(self, tasks_json, name):
        template = """
        Given the following JSON object with tasks assigned to different people:

        {tasks_json}

        Please extract the tasks for the person named "{name}" and return them as a list.
        """

        prompt = PromptTemplate(
            input_variables=["tasks_json", "name"],
            template=template,
        )

        llm = OpenAI(temperature=0.9)
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(tasks_json, name)
        tasks = json.loads(response)
        return tasks
