"""
Program to update input file value.yaml 
with values from vault (sample vault data)

"""
import re, yaml, logging

class VaultMock:
    def __init__(self):
        self.secrets = {
            "org::secret/api/integrations::api-token": "actual_token",
            "org::secret/api/integrations::private-key": "actual_private_key",
            "org::secret/api/integrations::license-string-1": "license_string_1",
            "org::secret/api/integrations::license-string-2": "license_string_2",
            "org::secret/api/integrations::license-string-3": "license_string_3",
            "org::secret/api/integrations::license-string-4": "license_string_4",
            "org::secret/api/integrations::username": "actual_username",
            "org::secret/api/integrations::password": "actual_password"
        }

    def get_secret(self, path_to_key):
        return self.secrets.get(path_to_key)

"""
YamlFileProcessor process the input values.yaml file
by getting the secret , replace and update the yaml file. 
"""
class YamlFileProcessor:
    def __init__(self, vault: VaultMock):
        self.vault = vault

    def replace_from_vault(self, match):
        key = match.group(1)
        value = self.vault.get_secret(key)
        return value

    def process_yaml_file(self, file_name: str):
        with open(file_name, 'r') as stream:
            try:
                input_string = stream.read()
                pattern = '<@VAULT::(.*?)>'
                updated_string = re.sub(pattern, self.replace_from_vault, input_string)
                updated_yaml = yaml.safe_load(updated_string)
                return updated_yaml
            except yaml.YAMLError as exception:
                logging.error(exception, exc_info=True)


def main():
    vault = VaultMock()
    input_file = "src/values.yaml"
    file_processor = YamlFileProcessor(vault)
    updated_yaml = file_processor.process_yaml_file(input_file)
    print(updated_yaml)

if __name__ == '__main__':
    main()
