## guess-the-number

To enter the virtual environment of a project hosted on a GitHub repository, follow the steps below:

1. **Clone the repository:**

   First, you need to clone the GitHub repository to your local machine. Open the terminal and run the command:

   ```bash
   git clone git@github.com:lourdilene/guess-the-number.git
   ```

2. **Navigate to the project directory:**

   After cloning the repository, enter the project directory:

   ```bash
   cd guess-the-number
   ```

3. **Create a virtual environment:**

   To create a virtual environment, you can use `venv`, which is a built-in Python module. Run the command:

   ```bash
   python3 -m venv venv
   ```

   Here, `venv` is the name of the directory where the virtual environment will be created. You can choose another name if you prefer.

4. **Activate the virtual environment:**

   After creating the virtual environment, you need to activate it. The activation command depends on your operating system:

   - On Linux/MacOS:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

5. **Install the dependencies:**

   With the virtual environment activated, install the necessary dependencies for the project. These dependencies are usually listed in a `requirements.txt` file. Run the command:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure that the `requirements.txt` file exists in the root directory of the project and contains all the necessary dependencies.

Now, you should be inside the virtual environment, with all dependencies installed and ready to work on the project.

To deactivate the virtual environment when you are done working, simply run the command:

```bash
deactivate
```

5. **Run Tests:**

To run tests, use the following command:

```bash
pytest
```

6. *** UML Class Diagram ***

![UML Class Diagram](https://github.com/lourdilene/guess-the-number/blob/main/uml/guess_the_number_UML_class.jpeg)

This UML class diagram provides a visual representation of the class structure and relationships within the project.

