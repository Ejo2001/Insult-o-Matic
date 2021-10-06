import requests

insult = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=text")
print(insult.text)