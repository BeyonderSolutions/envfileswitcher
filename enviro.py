import os
import sys

from dotenv import load_dotenv


def switch_environment(environment):
    env_file = f".env.{environment}"
    
    if not os.path.exists(env_file):
        print(f"File '{env_file}' does not exist.")
        sys.exit(1)

    with open(env_file, 'r') as source_file:
        env_contents = source_file.read()

    with open('.env', 'w') as target_file:
        target_file.write(env_contents)

    print(f'Switched to {environment} environment.')

def test():
    load_dotenv()
    var_1 = os.getenv("VAR1")
    var_2 = os.getenv("VAR2")
    print(var_1, var_2)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: switcher <environment>")
        sys.exit(1)
    switch_environment(args[0])