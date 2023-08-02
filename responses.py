import api


def handle_responcse(message) -> str:
    p_message = message.lower()

    if p_message == "d!joke":
        return str(api.dadJoke())
    elif p_message == "d!help":
        return "`d!help for help \nd!joke for joke`"
