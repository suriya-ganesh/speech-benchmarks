import yaml


def get_config():
    # Load the YAML file
    with open('config/config.yaml', 'r') as file:
        data = yaml.safe_load(file)

    # Print the dictionary
    print(data)


def benchmarks():
    get_config()


if __name__ == "__main__":
    benchmarks()
