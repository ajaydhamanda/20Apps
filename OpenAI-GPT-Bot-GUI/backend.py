import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.3
        ).choice[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("who is king solomun")