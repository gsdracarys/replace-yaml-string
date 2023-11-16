# Vault Mock Program

## Problem

Write a program where given a yaml file with strings formatted like: `<@VAULT::org::secret/path/to/string::key>`, it will replace it with its actual value.

`values.yaml`

```yaml
app:
  config:
    https: true
    grpc: false
  port: 9990

  secrets:
    apiToken: <@VAULT::org::secret/api/integrations::api-token>
    privateKey: <@VAULT::org::secret/api/integrations::private-key>
    licenseFile: |
      <@VAULT::org::secret/api/integrations::license-string-1>
      ===
      <@VAULT::org::secret/api/integrations::license-string-2>
      ===
      <@VAULT::org::secret/api/integrations::license-string-3>
      ===
      <@VAULT::org::secret/api/integrations::license-string-4>
    userAuth: "<@VAULT::org::secret/api/integrations::username>:<@VAULT::org::secret/api/integrations::password>"
```

 since we do not have a vault instance available, create a function to simulate fetching the secret from vault, example

## Solution

- Create vaultmock.yaml with two classes `VaultMock` and `YamlFileProcessor`
- `VaultMock` will have `init` function (Store the mock vault secrets) and `get_secrets` functions (retrieve the function)
- `YamlFileProcessor` will process the yaml file with function `replace_from_vault`(get secrets from vault by mtaching the keys) and `process_yaml_file` (reads the input yaml file and returns updated yaml string)

## How to run and test the program

- `make run` which call target from `Makefile` , setup the virtuan environment , install dependencies and run the progream
- `make test` target will test it with pytest lib.
