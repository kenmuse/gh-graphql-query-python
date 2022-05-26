# GraphQL Query in Python
This repository provides demonstrates how to make a basic GitHub GraphQL query using Python. The application will query the current API rate limit and return the results.

## Setup & Configuration
If you're using [GitHub Codespaces](https://github.com/features/codespaces) or [Visual Studio development containers](https://code.visualstudio.com/docs/remote/containers), then there's nothing special required. The container will automatically restore the needed packages.

If you're not using a development container, you will need to install Python 3. After that, use `pip` to install the project's dependencies:

```bash
pip3 install --upgrade pip
pip3 install --user -r ./requirements.txt
```

To run the application, you will need to create a GitHub [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) in your [Developer Settings](https://github.com/settings/tokens). This token will not require any privileges to be selected. If you modify the query, you will need to define appropriate privileges.

To run the sample, use the following command line. You will need to provide the token you created in the previous step.

```bash
python app.py {your-token}
```