import yaml


class Config:

    with open('Config/config.yaml', 'r') as stream:
        config = yaml.safe_load(stream)
    browser = config['data']['browser']
    url = config['data']['url']
    email = config['account']['email']
    password = config['account']['password']
