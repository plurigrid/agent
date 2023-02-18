from langchain import LLMChain, OpenAI, PromptTemplate


class AestheticModel:
    # This is an LLM which translates an aesthetic into brightness and color values.
    def aesthetic_to_msg(self, aesthetic):
        template = """
        Take an aesthetic and translate it into an HSV value. Format the response as JSON where there is a different key for each variable:
        hue, saturation, and value. Each value must be an integer. 
        What is a good brightness and color that represents {aesthetic}?
        """
        prompt = PromptTemplate(
            input_variables=["aesthetic"],
            template=template,
        )

        llm = OpenAI(temperature=0.9)
        chain = LLMChain(llm=llm, prompt=prompt)
        return chain.run(aesthetic)
