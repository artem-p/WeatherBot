import json

def get_secret(secret_key):
  secret_file = 'secrets.json'
  with open(secret_file) as f:
    SECRETS = json.load(f)

  return str(SECRETS[secret_key])
