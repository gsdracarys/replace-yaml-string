import pytest
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.vaultmock import *

def test_yaml_processor():
    vault_mock = VaultMock()
    yaml_processor = YamlFileProcessor(vault_mock)
    yaml_content = yaml_processor.process_yaml_file('tests/test.yaml')

    assert isinstance(yaml_content, dict), "The returned object is not a dictionary"

    # Test the value of one of the keys to know if the method
    # correctly fetched the secret from the vault or not
    assert yaml_content['app']['secrets']['apiToken'] == "actual_token"

pytest.main()
