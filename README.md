# PyScript-GUI-logger
The script is a simple GUI application that enables users to select a Python file and run it while also logging the execution and completion status of the file in a log file. The user is also able to choose the level of logging required from the logging module.

The following modules were imported for this script:

tkinter: This module was imported as tk to provide a graphical user interface (GUI) for the application.
filedialog: This was imported from the tkinter module to provide a file dialog window for the user to select files.
logging: This module was imported to enable logging of messages during script execution.
The script consists of a main function run_script() which is bound to a tk.Button widget. The function prompts the user to select a Python file to be executed and a file to save the log. It then uses the logging.basicConfig() method to specify the log file and logging level provided by the user. It then logs the message "Running script: <script_path>" to indicate the script being executed.

The try-except block of the function is used to execute the Python script selected by the user. If the script execution is successful, a message "Script completed successfully" is logged to the log file. If the script execution fails, an error message is logged with the exception that caused the error.

Finally, the function displays a message box with the message "Script completed" to the user indicating that the script has completed execution.

The GUI consists of two tk.Label widgets prompting the user to select a Python file and log level respectively. Two tk.Button widgets are also present; the first for the user to browse and select a Python file and the second to execute the selected script. A drop-down tk.OptionMenu widget is present to enable the user to select the level of logging required.

At the end of the script, the mainloop() method is called on the root object to start the GUI application.



Regenerate response

