# 🔮 enviro
This Python script provides a simple solution for managing environmental variables in a software development project. It allows you to switch between different environment configurations by copying the contents of specific `.env` files based on the environment you specify. This makes it easy to manage credentials and configurations for various development stages, such as production, development, staging, and testing.

## Usage
You can run this script from the command line by providing the desired environment as an argument.

```bash
python3 enviro.py <environment>
```

Replace `<environment>` with the specific environment name you want to switch to, such as "production", "development" or any other configuration you have set up.

### Example
Suppose you have the following files inside your project directory:

```
myproject/
├── .env
├── .env.production
└── .env.development
```

To switch to the production environment, run the following command from within your project directory:

```bash
python3 switcher.py production
```

The script will copy the contents of `.env.production` into the main `.env` file. This will allow you to work with the configuration specific to the production environment.

## Building

### Building Locally
In order to build a standalone binary for **enviro** on your own machine, you can simply do the following:

```bash
pip install -r requirements.txt
pyinstaller enviro.py
```

The previous commands will output the binary for **enviro**, which you can locate inside the newly created `dist/enviro` folder.
>Don't forget that the `/_internal` folder needs to exist next to the `enviro` or `enviro.exe` file!

### Building from Docker
If you currently do not have access to a Linux machine but need to generate the binary for it, you can try this Docker alternative.

```bash
docker build -t enviro . && docker run enviro
```

The following command will output the Linux binaries.

## Executable Versions for Windows and Linux
In addition to the Python script, I've included executable versions of the script for both the Windows and Linux platforms. You now have the flexibility to switch between environments with just a simple double-click or terminal command, making the transition smoother than ever. Whether you're a Windows enthusiast or a Linux aficionado, I've got you covered.

Happy environment switching! 🚀💻🐧🖱