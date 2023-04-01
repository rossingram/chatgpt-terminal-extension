import openai


class ChatGPT:
    def __init__(self, api_key):
        if api_key == "":
            print("The API key was not set properly use the /help menu to debug")
            return

        openai.api_key = api_key
        self.model_engine = "text-davinci-003"

    def respond_to_prompt(self, prompt):
        """
        Sends a prompt to ChatGPT and waits for a response
        :param prompt: The Prompt to run in ChatGPT
        :return: Returns the string of ChatGPT's response
        """
        response = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=100)
        text = response.choices[0].text.strip()
        return text
