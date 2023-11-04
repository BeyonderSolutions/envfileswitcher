# 🧙‍♂️EnviroSwitcher
This Python script provides a simple solution for managing environmental variables in a software development project. It allows you to switch between different environment configurations by copying the contents of specific .env files based on the environment you specify. This makes it easy to manage credentials and configurations for various development stages, such as production, development, staging, and testing.

## Usage
You can run this script from the command line by providing the desired environment as an argument.

```
python switcher.py <environment>
```

Replace \<environment> with the specific environment you want to switch to, such as "production," "development," or any other configuration you have set up.

## Example
Suppose you have the following files inside your project directory:

```
myproject/
├── .env
├── .env.production
└── .env.development
```

To switch to the production environment, run the following command from within your project directory:

```
python switcher.py production
```

The script will copy the contents of `.env.production` into the main .env file. This will allow you to work with the configuration specific to the production environment.

## Executable Versions for Windows and Linux
In addition to the Python script, I've included executable versions of the script for both Windows and Linux platforms. You now have the flexibility to switch between environments with just a simple double-click or terminal command, making the transition smoother than ever. Whether you're a Windows enthusiast or a Linux aficionado, I've got you covered. Happy environment switching! 🚀💻🐧🖱