import logging
logging.basicConfig(level=logging.INFO, filename="app.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

def format_text(text):
    return text.strip().capitalize()

def log_interaction(user_input, response):
    with open("interaction_log.txt", "a") as log_file:
        log_file.write(f"User: {user_input}\nLoki: {response}\n\n")

def validate_query(query):
    return isinstance(query, str) and len(query) > 0

def load_configuration(config_file):
    import json
    with open(config_file, "r") as file:
        return json.load(file)