import json

import yaml


class ConfigParserError(Exception):
    """Denotes failing to parse configuration file."""
    def __init__(self, message, *args):
        self.message = message
        super(ConfigParserError, self).__init__(message, *args)

    def __str__(self):
        return 'While parsing config: {}'.format(self.message)


def unmarshall_config_reader(file_, d, config_type):
    config_type = config_type.lower()

    if config_type in ['yaml', 'yml']:
        try:
            f = yaml.load(file_)
            d.update(yaml.load(f))
        except Exception as e:
            raise ConfigParserError(e)

    elif config_type == 'json':
        try:
            f = json.load(file_)
            d.update(f)
        except Exception as e:
            raise ConfigParserError(e)

    elif config_type == 'toml':
        try:
            d.update(file_)
        except Exception as e:
            raise ConfigParserError(e)

    return d
