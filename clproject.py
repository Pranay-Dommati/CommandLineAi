# import os
# import subprocess
# import google.generativeai as genai
# import tkinter as tk
# from tkinter import simpledialog, messagebox

# # Configure your API key
# genai.configure(api_key="AIzaSyCAjkkf4L37uhSZ4jCmTzNcTZ0mQx8uEEI")

# # Initialize a log to store command history and outputs
# command_log = []

# def execute_command(command):
#     """Executes a shell command and captures its output and error."""
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     output, error = process.communicate()

#     output = output.decode("utf-8").strip()
#     error = error.decode("utf-8").strip()

#     command_log.append({"command": command, "output": output, "error": error})
#     return output, error

# def run_command():
#     """Handles command execution from the entry field."""
#     command = command_entry.get()
#     output, error = execute_command(command)
#     output_text.delete(1.0, tk.END)  # Clear previous output
#     output_text.insert(tk.END, f"Output: {output}\nError: {error}\n")  # Display output

# def ask_gemini():
#     """Queries the Gemini AI based on the command log."""
#     history = "\n".join([f"Command: {entry['command']}\nOutput: {entry['output']}\nError: {entry['error']}" for entry in command_log])
#     user_query = simpledialog.askstring("Ask AI", "What would you like to ask the AI?")
    
#     if user_query:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         chat_session = model.start_chat(
#             history=[
#                 {
#                     "role": "user",
#                     "parts": [history + "\n" + user_query],
#                 }
#             ]
#         )
#         response = chat_session.send_message(user_query)
#         messagebox.showinfo("Gemini Response", response.text)

# # Create the main window
# root = tk.Tk()
# root.title("Command Line Assistant with AI")

# # Command entry
# command_entry = tk.Entry(root, width=50)
# command_entry.pack(pady=10)

# # Execute command button
# execute_button = tk.Button(root, text="Execute Command", command=run_command)
# execute_button.pack(pady=5)

# # Text area for output
# output_text = tk.Text(root, height=15, width=60)
# output_text.pack(pady=10)

# # Ask AI button
# ask_button = tk.Button(root, text="Ask AI", command=ask_gemini)
# ask_button.pack(pady=5)

# # Run the application
# root.mainloop()















# import os
# import subprocess
# import google.generativeai as genai
# import tkinter as tk
# from tkinter import simpledialog, messagebox

# # Configure your API key directly in the code
# genai.configure(api_key="AIzaSyCAjkkf4L37uhSZ4jCmTzNcTZ0mQx8uEEI")

# # Initialize a log to store command history and outputs
# command_log = []

# def execute_command(command):
#     """Executes a shell command and captures its output and error."""
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     output, error = process.communicate()

#     output = output.decode("utf-8").strip()
#     error = error.decode("utf-8").strip()

#     command_log.append({"command": command, "output": output, "error": error})
#     return output, error

# def run_command():
#     """Handles command execution from the entry field."""
#     command = command_entry.get()
#     output, error = execute_command(command)
#     output_text.delete(1.0, tk.END)  # Clear previous output
#     output_text.insert(tk.END, f"Output: {output}\nError: {error}\n")  # Display output

# def ask_gemini():
#     """Queries the Gemini AI based on the command log."""
#     history = "\n".join([f"Command: {entry['command']}\nOutput: {entry['output']}\nError: {entry['error']}" for entry in command_log])
#     user_query = simpledialog.askstring("Ask AI", "What would you like to ask the AI?")
    
#     if user_query:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         chat_session = model.start_chat(
#             history=[{
#                 "role": "user",
#                 "parts": [history + "\n" + user_query],
#             }]
#         )
#         response = chat_session.send_message(user_query)
#         messagebox.showinfo("Gemini Response", response.text)

# # Create the main window
# root = tk.Tk()
# root.title("Command Line Assistant with AI")

# # Command entry
# command_entry = tk.Entry(root, width=50)
# command_entry.pack(pady=10)

# # Execute command button
# execute_button = tk.Button(root, text="Execute Command", command=run_command)
# execute_button.pack(pady=5)

# # Text area for output
# output_text = tk.Text(root, height=15, width=60)
# output_text.pack(pady=10)

# # Ask AI button
# ask_button = tk.Button(root, text="Ask AI", command=ask_gemini)
# ask_button.pack(pady=5)

# # Run the application
# root.mainloop()

















# import os
# import subprocess
# import google.generativeai as genai
# import tkinter as tk
# from tkinter import simpledialog, messagebox

# # Configure your API key directly in the code
# genai.configure(api_key="AIzaSyCAjkkf4L37uhSZ4jCmTzNcTZ0mQx8uEEI")

# # Initialize a log to store command history and outputs
# command_log = []
# current_directory = os.getcwd()  # Track the current working directory

# def execute_command(command):
#     """Executes a shell command and captures its output and error."""
#     global current_directory  # Use the global variable for current directory

#     # Handle cd command to change working directory
#     if command.startswith("cd "):
#         path = command[3:].strip()
#         try:
#             # Change directory
#             os.chdir(path)
#             current_directory = os.getcwd()  # Update the tracked current directory
#             output = f"Changed directory to {current_directory}"
#             error = ""
#             command_log.append({"command": command, "output": output, "error": error})
#             return output, error
#         except FileNotFoundError:
#             error = f"cd: {path}: No such file or directory"
#             command_log.append({"command": command, "output": "", "error": error})
#             return "", error

#     # Execute other commands in the current directory
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_directory)
#     output, error = process.communicate()

#     output = output.decode("utf-8").strip()
#     error = error.decode("utf-8").strip()

#     # Log command execution
#     command_log.append({"command": command, "output": output, "error": error})

#     return output, error

# def run_command():
#     """Handles command execution from the entry field."""
#     command = command_entry.get()
#     if command.strip():
#         output, error = execute_command(command)  # Execute the command
#         output_text.delete(1.0, tk.END)  # Clear previous output
#         output_text.insert(tk.END, f"> {command}\n")
#         if output:
#             output_text.insert(tk.END, f"Output: {output}\n")
#         if error:
#             output_text.insert(tk.END, f"Error: {error}\n")
#         command_entry.delete(0, tk.END)  # Clear entry field

# def ask_gemini():
#     """Queries the Gemini AI based on the command log."""
#     history = "\n".join([f"Command: {entry['command']}\nOutput: {entry['output']}\nError: {entry['error']}" for entry in command_log])
#     user_query = simpledialog.askstring("Ask AI", "What would you like to ask the AI?")
    
#     if user_query:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         chat_session = model.start_chat(
#             history=[{"role": "user", "parts": [history + "\n" + user_query]}]
#         )
#         response = chat_session.send_message(user_query)
#         messagebox.showinfo("Gemini Response", response.text)

# # Create the main window
# root = tk.Tk()
# root.title("Command Line Assistant with AI")

# # Command entry
# command_entry = tk.Entry(root, width=70)
# command_entry.pack(pady=10)

# # Execute command button
# execute_button = tk.Button(root, text="Execute Command", command=run_command)
# execute_button.pack(pady=5)

# # Text area for output
# output_text = tk.Text(root, height=20, width=80)
# output_text.pack(pady=10)

# # Ask AI button
# ask_button = tk.Button(root, text="Ask AI", command=ask_gemini)
# ask_button.pack(pady=5)

# # Run the application
# root.mainloop()

















# import os
# import subprocess
# import google.generativeai as genai
# import tkinter as tk
# from tkinter import simpledialog, messagebox, scrolledtext

# # Configure your API key directly in the code
# genai.configure(api_key="AIzaSyCAjkkf4L37uhSZ4jCmTzNcTZ0mQx8uEEI")

# # Initialize a log to store command history and outputs
# command_log = []
# current_directory = os.getcwd()  # Track the current working directory

# def execute_command(command):
#     """Executes a shell command and captures its output and error."""
#     global current_directory  # Use the global variable for current directory

#     # Handle cd command to change working directory
#     if command.startswith("cd "):
#         path = command[3:].strip()
#         try:
#             # Change directory
#             os.chdir(path)
#             current_directory = os.getcwd()  # Update the tracked current directory
#             output = f"Changed directory to {current_directory}"
#             error = ""
#             command_log.append({"command": command, "output": output, "error": error})
#             return output, error
#         except FileNotFoundError:
#             error = f"cd: {path}: No such file or directory"
#             command_log.append({"command": command, "output": "", "error": error})
#             return "", error

#     # Execute other commands in the current directory
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_directory)
#     output, error = process.communicate()

#     output = output.decode("utf-8").strip()
#     error = error.decode("utf-8").strip()

#     # Log command execution
#     command_log.append({"command": command, "output": output, "error": error})

#     return output, error

# def run_command():
#     """Handles command execution from the entry field."""
#     command = command_entry.get()
#     if command.strip():
#         output, error = execute_command(command)  # Execute the command
#         output_text.insert(tk.END, f"> {command}\n")  # Show the command entered
#         if output:
#             output_text.insert(tk.END, f"{output}\n")
#         if error:
#             output_text.insert(tk.END, f"Error: {error}\n")
#         command_entry.delete(0, tk.END)  # Clear entry field

# def ask_gemini():
#     """Queries the Gemini AI based on the command log."""
#     history = "\n".join([f"Command: {entry['command']}\nOutput: {entry['output']}\nError: {entry['error']}" for entry in command_log])
#     user_query = simpledialog.askstring("Ask AI", "What would you like to ask the AI?")
    
#     if user_query:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         chat_session = model.start_chat(
#             history=[{"role": "user", "parts": [history + "\n" + user_query]}]
#         )
#         response = chat_session.send_message(user_query)
#         messagebox.showinfo("Gemini Response", response.text)

# # Create the main window
# root = tk.Tk()
# root.title("Command Line Assistant with AI")
# root.configure(bg="black")

# # Command entry
# command_entry = tk.Entry(root, width=70, bg="black", fg="green", insertbackground="green", font=("Courier New", 12))
# command_entry.pack(pady=10)

# # Execute command button
# execute_button = tk.Button(root, text="Execute Command", command=run_command, bg="black", fg="green", font=("Courier New", 10))
# execute_button.pack(pady=5)

# # Text area for output
# output_text = scrolledtext.ScrolledText(root, height=20, width=80, bg="black", fg="green", font=("Courier New", 12), wrap=tk.WORD)
# output_text.pack(pady=10)
# output_text.config(state=tk.DISABLED)  # Initially disable editing

# # Ask AI button
# ask_button = tk.Button(root, text="Ask AI", command=ask_gemini, bg="black", fg="green", font=("Courier New", 10))
# ask_button.pack(pady=5)

# # Run the application
# root.mainloop()






























# import os
# import subprocess
# import google.generativeai as genai
# import tkinter as tk
# from tkinter import simpledialog, messagebox

# # Configure your API key directly in the code
# genai.configure(api_key="AIzaSyCAjkkf4L37uhSZ4jCmTzNcTZ0mQx8uEEI")

# # Initialize a log to store command history and outputs
# command_log = []
# current_directory = os.getcwd()  # Track the current working directory

# def execute_command(command):
#     """Executes a shell command and captures its output and error."""
#     global current_directory  # Use the global variable for current directory

#     # Handle cd command to change working directory
#     if command.startswith("cd "):
#         path = command[3:].strip()
#         try:
#             # Change directory
#             os.chdir(path)
#             current_directory = os.getcwd()  # Update the tracked current directory
#             output = f"Changed directory to {current_directory}"
#             error = ""
#             command_log.append({"command": command, "output": output, "error": error})
#             return output, error
#         except FileNotFoundError:
#             error = f"cd: {path}: No such file or directory"
#             command_log.append({"command": command, "output": "", "error": error})
#             return "", error

#     # Execute other commands in the current directory
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_directory)
#     output, error = process.communicate()

#     output = output.decode("utf-8").strip()
#     error = error.decode("utf-8").strip()

#     # Log command execution
#     command_log.append({"command": command, "output": output, "error": error})

#     return output, error

# def run_command(event=None):
#     """Handles command execution from the entry field."""
#     command = input_text.get("1.0", tk.END).strip()
#     if command:
#         output, error = execute_command(command)  # Execute the command
#         output_text.insert(tk.END, f"> {command}\n")  # Show the command entered
#         if output:
#             output_text.insert(tk.END, f"{output}\n")
#         if error:
#             output_text.insert(tk.END, f"Error: {error}\n")
#         input_text.delete("1.0", tk.END)  # Clear input field
#         output_text.see(tk.END)  # Scroll to the end of the output      



# def ask_gemini():
#     """Queries the Gemini AI based on the command log."""
#     history = "\n".join([f"Command: {entry['command']}\nOutput: {entry['output']}\nError: {entry['error']}" for entry in command_log])
#     user_query = chat_entry.get()
    
#     if user_query:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         chat_session = model.start_chat(
#             history=[{"role": "user", "parts": [history + "\n" + user_query]}]
#         )
#         response = chat_session.send_message(user_query)
        
#         # Process response text to remove special characters
#         clean_response = response.text.replace("*", "").replace("•", "").strip()
        
#         # Display response
#         chat_output_text.config(state=tk.NORMAL)  # Enable editing for output
#         chat_output_text.insert(tk.END, f"You: {user_query}\n")
#         chat_output_text.insert(tk.END, f"Gemini: {clean_response}\n")
#         chat_output_text.config(state=tk.DISABLED)  # Disable editing again
#         chat_entry.delete(0, tk.END)  # Clear chat input

# # Create the main window
# root = tk.Tk()
# root.title("Command Line Assistant with AI")

# # Style the window to look like a command prompt
# root.configure(bg="black")

# # Output text area
# output_text = tk.Text(root, height=20, width=80, bg="black", fg="white", insertbackground="green")
# output_text.pack(pady=10)

# # Input text area
# input_text = tk.Text(root, height=1, width=80, bg="black", fg="white", insertbackground="green")
# input_text.pack(pady=10)
# input_text.bind("<Return>", run_command)  # Execute command on Enter key

# # Chat area for AI interactions
# chat_frame = tk.Frame(root, bg="black")
# chat_frame.pack(pady=10)

# chat_entry = tk.Entry(chat_frame, width=60)
# chat_entry.pack(side=tk.LEFT, padx=5)

# # Ask AI button
# ask_button = tk.Button(chat_frame, text="Ask AI", command=ask_gemini, bg='white', fg='black')
# ask_button.pack(side=tk.RIGHT)

# chat_output_text = tk.Text(root, height=10, width=80, bg="black", fg="white", insertbackground="green", state=tk.DISABLED)
# chat_output_text.pack(pady=10)

# # Run the application
# root.mainloop()
























# import os
# import subprocess
# import google.generativeai as genai
# import tkinter as tk
# from tkinter import simpledialog, messagebox

# # Configure your API key directly in the code
# genai.configure(api_key="AIzaSyCAjkkf4L37uhSZ4jCmTzNcTZ0mQx8uEEI")

# # Initialize a log to store command history and outputs
# command_log = []
# current_directory = os.getcwd()  # Track the current working directory

# def execute_command(command):
#     """Executes a shell command and captures its output and error."""
#     global current_directory  # Use the global variable for current directory

#     # Handle clear command to clear output text
#     if command.strip() == "clear":
#         output_text.delete("1.0", tk.END)  # Clear the output text area
#         command_log.append({"command": command, "output": "", "error": ""})
#         return "", ""  # No output or error for the clear command

#     # Handle cd command to change working directory
#     if command.startswith("cd "):
#         path = command[3:].strip()
#         try:
#             # Change directory
#             os.chdir(path)
#             current_directory = os.getcwd()  # Update the tracked current directory
#             output = f"Changed directory to {current_directory}"
#             error = ""
#             command_log.append({"command": command, "output": output, "error": error})
#             return output, error
#         except FileNotFoundError:
#             error = f"cd: {path}: No such file or directory"
#             command_log.append({"command": command, "output": "", "error": error})
#             return "", error

#     # Execute other commands in the current directory
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_directory)
#     output, error = process.communicate()

#     output = output.decode("utf-8").strip()
#     error = error.decode("utf-8").strip()

#     # Log command execution
#     command_log.append({"command": command, "output": output, "error": error})

#     return output, error

# def run_command(event=None):
#     """Handles command execution from the entry field."""
#     command = input_text.get("1.0", tk.END).strip()
#     if command:
#         output, error = execute_command(command)  # Execute the command
#         if command != "clear":
#             output_text.insert(tk.END, f"> {command}\n")  # Show the command entered
#         if output:
#             output_text.insert(tk.END, f"{output}\n")
#         if error:
#             output_text.insert(tk.END, f"Error: {error}\n")
#         input_text.delete("1.0", tk.END)  # Clear input field
#         output_text.see(tk.END)  # Scroll to the end of the output

# def ask_gemini():
#     """Queries the Gemini AI based on the command log."""
#     history = "\n".join([f"Command: {entry['command']}\nOutput: {entry['output']}\nError: {entry['error']}" for entry in command_log])
#     user_query = chat_entry.get()
    
#     if user_query:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         chat_session = model.start_chat(
#             history=[{"role": "user", "parts": [history + "\n" + user_query]}]
#         )
#         response = chat_session.send_message(user_query)
        
#         # Process response text to remove special characters
#         clean_response = response.text.replace("*", "").replace("•", "").strip()
        
#         # Display response
#         chat_output_text.config(state=tk.NORMAL)  # Enable editing for output
#         chat_output_text.insert(tk.END, f"You: {user_query}\n")
#         chat_output_text.insert(tk.END, f"Gemini: {clean_response}\n")
#         chat_output_text.config(state=tk.DISABLED)  # Disable editing again
#         chat_entry.delete(0, tk.END)  # Clear chat input

# # Create the main window
# root = tk.Tk()
# root.title("Command Line Assistant with AI")

# # Style the window to look like a command prompt
# root.configure(bg="black")

# # Output text area
# output_text = tk.Text(root, height=20, width=80, bg="black", fg="white", insertbackground="green")
# output_text.pack(pady=10)

# # Input text area
# input_text = tk.Text(root, height=1, width=80, bg="black", fg="white", insertbackground="green")
# input_text.pack(pady=10)
# input_text.bind("<Return>", run_command)  # Execute command on Enter key

# # Chat area for AI interactions
# chat_frame = tk.Frame(root, bg="black")
# chat_frame.pack(pady=10)

# chat_entry = tk.Entry(chat_frame, width=60)
# chat_entry.pack(side=tk.LEFT, padx=5)

# # Ask AI button
# ask_button = tk.Button(chat_frame, text="Ask AI", command=ask_gemini, bg='white', fg='black')
# ask_button.pack(side=tk.RIGHT)

# chat_output_text = tk.Text(root, height=10, width=80, bg="black", fg="white", insertbackground="green", state=tk.DISABLED)
# chat_output_text.pack(pady=10)

# # Run the application
# root.mainloop()

















# import os
# import subprocess
# import google.generativeai as genai
# import tkinter as tk

# # Configure your API key directly in the code
# genai.configure(api_key="AIzaSyCAjkkf4L37uhSZ4jCmTzNcTZ0mQx8uEEI")

# # Initialize a log to store command history and outputs
# command_log = []
# current_directory = os.getcwd()  # Track the current working directory

# def execute_command(command):
#     """Executes a shell command and captures its output and error."""
#     global current_directory  # Use the global variable for current directory

#     # Handle clear command to clear output text
#     if command.strip() == "clear":
#         output_text.config(state=tk.NORMAL)  # Enable editing for clearing
#         output_text.delete("1.0", tk.END)  # Clear the output text area
#         output_text.config(state=tk.DISABLED)  # Disable editing again
#         command_log.append({"command": command, "output": "", "error": ""})
#         return "", ""  # No output or error for the clear command

#     # Handle cd command to change working directory
#     if command.startswith("cd "):
#         path = command[3:].strip()
#         try:
#             os.chdir(path)
#             current_directory = os.getcwd()  # Update the tracked current directory
#             output = f"Changed directory to {current_directory}"
#             error = ""
#             command_log.append({"command": command, "output": output, "error": error})
#             return output, error
#         except FileNotFoundError:
#             error = f"cd: {path}: No such file or directory"
#             command_log.append({"command": command, "output": "", "error": error})
#             return "", error

#     # Execute other commands in the current directory
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_directory)
#     output, error = process.communicate()

#     output = output.decode("utf-8").strip()
#     error = error.decode("utf-8").strip()

#     # Log command execution
#     command_log.append({"command": command, "output": output, "error": error})

#     return output, error

# def run_command(event=None):
#     """Handles command execution from the entry field."""
#     command = input_text.get("1.0", tk.END).strip()
#     if command:
#         output, error = execute_command(command)  # Execute the command
#         if command != "clear":
#             output_text.config(state=tk.NORMAL)  # Enable editing to insert output
#             output_text.insert(tk.END, f"> {command}\n")  # Show the command entered
#             if output:
#                 output_text.insert(tk.END, f"{output}\n")
#             if error:
#                 output_text.insert(tk.END, f"Error: {error}\n")
#             output_text.config(state=tk.DISABLED)  # Disable editing again
#         input_text.delete("1.0", tk.END)  # Clear input field
#         output_text.see(tk.END)  # Scroll to the end of the output

# def ask_gemini(event=None):
#     """Queries the Gemini AI based on the command log."""
#     history = "\n".join([f"Command: {entry['command']}\nOutput: {entry['output']}\nError: {entry['error']}" for entry in command_log])
#     user_query = chat_entry.get()
    
#     if user_query:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         chat_session = model.start_chat(
#             history=[{"role": "user", "parts": [history + "\n" + user_query]}]
#         )
#         response = chat_session.send_message(user_query)
        
#         # Process response text to remove special characters
#         clean_response = response.text.replace("*", "").replace("•", "").strip()
        
#         # Display response
#         chat_output_text.config(state=tk.NORMAL)  # Enable editing for output
#         chat_output_text.insert(tk.END, f"You: {user_query}\n")
#         chat_output_text.insert(tk.END, f"Gemini: {clean_response}\n")
#         chat_output_text.config(state=tk.DISABLED)  # Disable editing again
#         chat_entry.delete(0, tk.END)  # Clear chat input

# # Create the main window
# root = tk.Tk()
# root.title("Command Line Assistant with AI")

# # Style the window to look like a command prompt
# root.configure(bg="black")

# # Output text area
# output_text = tk.Text(root, height=20, width=80, bg="black", fg="white", insertbackground="green", state=tk.DISABLED)
# output_text.pack(pady=10)

# # Input text area
# input_text = tk.Text(root, height=1, width=80, bg="black", fg="white", insertbackground="green")
# input_text.pack(pady=10)
# input_text.bind("<Return>", run_command)  # Execute command on Enter key

# # Chat area for AI interactions
# chat_frame = tk.Frame(root, bg="black")
# chat_frame.pack(pady=10)

# chat_entry = tk.Entry(chat_frame, width=60)
# chat_entry.pack(side=tk.LEFT, padx=5)
# chat_entry.bind("<Return>", ask_gemini)  # Execute AI command on Enter key

# # Ask AI button
# ask_button = tk.Button(chat_frame, text="Ask AI", command=ask_gemini, bg='white', fg='black')
# ask_button.pack(side=tk.RIGHT)

# chat_output_text = tk.Text(root, height=10, width=80, bg="black", fg="white", insertbackground="green", state=tk.DISABLED)
# chat_output_text.pack(pady=10)

# # Run the application
# root.mainloop()




















# import os
# import subprocess
# import google.generativeai as genai
# import tkinter as tk
# from tkinter import PhotoImage  # Import PhotoImage to load images

# # Configure your API key directly in the code
# genai.configure(api_key="AIzaSyCAjkkf4L37uhSZ4jCmTzNcTZ0mQx8uEEI")

# # Initialize a log to store command history and outputs
# command_log = []
# current_directory = os.getcwd()  # Track the current working directory

# def execute_command(command):
#     """Executes a shell command and captures its output and error."""
#     global current_directory  # Use the global variable for current directory

#     # Handle clear command to clear output text
#     if command.strip() == "clear":
#         output_text.config(state=tk.NORMAL)  # Enable editing for clearing
#         output_text.delete("1.0", tk.END)  # Clear the output text area
#         output_text.config(state=tk.DISABLED)  # Disable editing again
#         command_log.append({"command": command, "output": "", "error": ""})
#         return "", ""  # No output or error for the clear command

#     # Handle cd command to change working directory
#     if command.startswith("cd "):
#         path = command[3:].strip()
#         try:
#             os.chdir(path)
#             current_directory = os.getcwd()  # Update the tracked current directory
#             output = f"Changed directory to {current_directory}"
#             error = ""
#             command_log.append({"command": command, "output": output, "error": error})
#             return output, error
#         except FileNotFoundError:
#             error = f"cd: {path}: No such file or directory"
#             command_log.append({"command": command, "output": "", "error": error})
#             return "", error

#     # Execute other commands in the current directory
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_directory)
#     output, error = process.communicate()

#     output = output.decode("utf-8").strip()
#     error = error.decode("utf-8").strip()

#     # Log command execution
#     command_log.append({"command": command, "output": output, "error": error})

#     return output, error

# def run_command(event=None):
#     """Handles command execution from the entry field."""
#     command = input_text.get("1.0", tk.END).strip()
#     if command:
#         output, error = execute_command(command)  # Execute the command
#         if command != "clear":
#             output_text.config(state=tk.NORMAL)  # Enable editing to insert output
#             output_text.insert(tk.END, f"> {command}\n")  # Show the command entered
#             if output:
#                 output_text.insert(tk.END, f"{output}\n")
#             if error:
#                 output_text.insert(tk.END, f"Error: {error}\n")
#             output_text.config(state=tk.DISABLED)  # Disable editing again
#         input_text.delete("1.0", tk.END)  # Clear input field
#         output_text.see(tk.END)  # Scroll to the end of the output

# def ask_gemini(event=None):
#     """Queries the Gemini AI based on the command log."""
#     history = "\n".join([f"Command: {entry['command']}\nOutput: {entry['output']}\nError: {entry['error']}" for entry in command_log])
#     user_query = chat_entry.get()
    
#     if user_query:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         chat_session = model.start_chat(
#             history=[{"role": "user", "parts": [history + "\n" + user_query]}]
#         )
#         response = chat_session.send_message(user_query)
        
#         # Process response text to remove special characters
#         clean_response = response.text.replace("*", "").replace("•", "").strip()
        
#         # Display response
#         chat_output_text.config(state=tk.NORMAL)  # Enable editing for output
#         chat_output_text.insert(tk.END, f"You: {user_query}\n")
#         chat_output_text.insert(tk.END, f"Gemini: {clean_response}\n")
#         chat_output_text.config(state=tk.DISABLED)  # Disable editing again
#         chat_entry.delete(0, tk.END)  # Clear chat input

# # Create the main window
# root = tk.Tk()
# root.title("Command Line Assistant with AI")

# # Style the window to look like a command prompt
# root.configure(bg="black")

# # Output text area
# output_text = tk.Text(root, height=20, width=80, bg="black", fg="white", insertbackground="green", state=tk.DISABLED)
# output_text.pack(pady=10)

# # Input text area
# input_text = tk.Text(root, height=1, width=80, bg="black", fg="white", insertbackground="green")
# input_text.pack(pady=10)
# input_text.bind("<Return>", run_command)  # Execute command on Enter key

# # Chat area for AI interactions
# chat_frame = tk.Frame(root, bg="black")
# chat_frame.pack(pady=10)

# chat_entry = tk.Entry(chat_frame, width=60)
# chat_entry.pack(side=tk.LEFT, padx=5)
# chat_entry.bind("<Return>", ask_gemini)  # Execute AI command on Enter key

# # Ask AI button
# ask_button = tk.Button(chat_frame, text="Ask AI", command=ask_gemini, bg='white', fg='black')
# ask_button.pack(side=tk.RIGHT)

# # Chat output text area
# chat_output_text = tk.Text(root, height=10, width=80, bg="black", fg="white", insertbackground="green", state=tk.DISABLED)
# chat_output_text.pack(pady=10)

# # Create a frame for logo and label on the right
# right_frame = tk.Frame(root, bg="black")
# right_frame.pack(side=tk.RIGHT, padx=10)

# # Load the flower pot logo image
# flower_pot_image = PhotoImage(file="logo.png")  # Ensure this image is in the same directory

# # Create a label for the logo
# logo_label = tk.Label(right_frame, image=flower_pot_image, bg="black")
# logo_label.pack(pady=5)

# # Create a label for the personalized command prompt text
# text_label = tk.Label(right_frame, text="Pranay's Personalized Command Prompt", bg="black", fg="white", font=("Helvetica", 12))
# text_label.pack(pady=5)

# # Run the application
# root.mainloop()














# import os
# import subprocess
# import google.generativeai as genai
# import tkinter as tk
# from PIL import Image, ImageTk  # Import Image and ImageTk for image handling

# # Configure your API key directly in the code
# genai.configure(api_key="AIzaSyCAjkkf4L37uhSZ4jCmTzNcTZ0mQx8uEEI")

# # Initialize a log to store command history and outputs
# command_log = []
# current_directory = os.getcwd()  # Track the current working directory

# def execute_command(command):
#     """Executes a shell command and captures its output and error."""
#     global current_directory  # Use the global variable for current directory

#     # Handle clear command to clear output text
#     if command.strip() == "clear":
#         output_text.config(state=tk.NORMAL)  # Enable editing for clearing
#         output_text.delete("1.0", tk.END)  # Clear the output text area
#         output_text.config(state=tk.DISABLED)  # Disable editing again
#         command_log.append({"command": command, "output": "", "error": ""})
#         return "", ""  # No output or error for the clear command

#     # Handle cd command to change working directory
#     if command.startswith("cd "):
#         path = command[3:].strip()
#         try:
#             os.chdir(path)
#             current_directory = os.getcwd()  # Update the tracked current directory
#             output = f"Changed directory to {current_directory}"
#             error = ""
#             command_log.append({"command": command, "output": output, "error": error})
#             return output, error
#         except FileNotFoundError:
#             error = f"cd: {path}: No such file or directory"
#             command_log.append({"command": command, "output": "", "error": error})
#             return "", error

#     # Execute other commands in the current directory
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_directory)
#     output, error = process.communicate()

#     output = output.decode("utf-8").strip()
#     error = error.decode("utf-8").strip()

#     # Log command execution
#     command_log.append({"command": command, "output": output, "error": error})

#     return output, error

# def run_command(event=None):
#     """Handles command execution from the entry field."""
#     command = input_text.get("1.0", tk.END).strip()
#     if command:
#         output, error = execute_command(command)  # Execute the command
#         if command != "clear":
#             output_text.config(state=tk.NORMAL)  # Enable editing to insert output
#             output_text.insert(tk.END, f"> {command}\n")  # Show the command entered
#             if output:
#                 output_text.insert(tk.END, f"{output}\n")
#             if error:
#                 output_text.insert(tk.END, f"Error: {error}\n")
#             output_text.config(state=tk.DISABLED)  # Disable editing again
#         input_text.delete("1.0", tk.END)  # Clear input field
#         output_text.see(tk.END)  # Scroll to the end of the output

# def ask_gemini(event=None):
#     """Queries the Gemini AI based on the command log."""
#     history = "\n".join([f"Command: {entry['command']}\nOutput: {entry['output']}\nError: {entry['error']}" for entry in command_log])
#     user_query = chat_entry.get()
    
#     if user_query:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         chat_session = model.start_chat(
#             history=[{"role": "user", "parts": [history + "\n" + user_query]}]
#         )
#         response = chat_session.send_message(user_query)
        
#         # Process response text to remove special characters
#         clean_response = response.text.replace("*", "").replace("•", "").strip()
        
#         # Display response
#         chat_output_text.config(state=tk.NORMAL)  # Enable editing for output
#         chat_output_text.insert(tk.END, f"You: {user_query}\n")
#         chat_output_text.insert(tk.END, f"Pranay's Ai: {clean_response}\n\n")
#         chat_output_text.config(state=tk.DISABLED)  # Disable editing again
#         chat_entry.delete(0, tk.END)  # Clear chat input

# # Create the main window
# root = tk.Tk()
# root.title("Command Line Assistant with AI")

# # Style the window to look like a command prompt
# root.configure(bg="black")

# # Create a frame for logo and label
# logo_frame = tk.Frame(root, bg="black")
# logo_frame.pack(side=tk.RIGHT, padx=10)

# # Load the image and create a label
# logo_image = Image.open("logo.png")  # Make sure to provide the correct path to your image
# logo_image = logo_image.resize((450, 200), Image.LANCZOS)  # Resize if necessary
# logo_photo = ImageTk.PhotoImage(logo_image)
# logo_label = tk.Label(logo_frame, image=logo_photo, bg="black")
# logo_label.pack()


# # Output text area
# output_text = tk.Text(root, height=20, width=80, bg="black", fg="white", insertbackground="green", state=tk.DISABLED)
# output_text.pack(pady=10)

# # Input text area
# input_text = tk.Text(root, height=1, width=80, bg="black", fg="white", insertbackground="green")
# input_text.pack(pady=10)
# input_text.bind("<Return>", run_command)  # Execute command on Enter key

# # Chat area for AI interactions
# chat_frame = tk.Frame(root, bg="black")
# chat_frame.pack(pady=10)

# chat_entry = tk.Entry(chat_frame, width=60)
# chat_entry.pack(side=tk.LEFT, padx=5)
# chat_entry.bind("<Return>", ask_gemini)  # Execute AI command on Enter key

# # Ask AI button
# ask_button = tk.Button(chat_frame, text="Ask AI", command=ask_gemini, bg='white', fg='black')
# ask_button.pack(side=tk.RIGHT)

# chat_output_text = tk.Text(root, height=10, width=80, bg="black", fg="white", insertbackground="green", state=tk.DISABLED)
# chat_output_text.pack(pady=10)

# # Run the application
# root.mainloop()



















# import os
# import subprocess
# import google.generativeai as genai
# import tkinter as tk
# from PIL import Image, ImageTk  # Import Image and ImageTk for image handling

# # Configure your API key directly in the code
# genai.configure(api_key="AIzaSyCAjkkf4L37uhSZ4jCmTzNcTZ0mQx8uEEI")

# # Initialize a log to store command history and outputs
# command_log = []
# current_directory = os.getcwd()  # Track the current working directory

# def execute_command(command):
#     """Executes a shell command and captures its output and error."""
#     global current_directory  # Use the global variable for current directory

#     # Handle clear command to clear output text
#     if command.strip() == "clear":
#         output_text.config(state=tk.NORMAL)  # Enable editing for clearing
#         output_text.delete("1.0", tk.END)  # Clear the output text area
#         output_text.config(state=tk.DISABLED)  # Disable editing again
#         command_log.append({"command": command, "output": "", "error": ""})
#         return "", ""  # No output or error for the clear command

#     # Handle cd command to change working directory
#     if command.startswith("cd "):
#         path = command[3:].strip()
#         try:
#             os.chdir(path)
#             current_directory = os.getcwd()  # Update the tracked current directory
#             output = f"Changed directory to {current_directory}"
#             error = ""
#             command_log.append({"command": command, "output": output, "error": error})
#             return output, error
#         except FileNotFoundError:
#             error = f"cd: {path}: No such file or directory"
#             command_log.append({"command": command, "output": "", "error": error})
#             return "", error

#     # Execute other commands in the current directory
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_directory)
#     output, error = process.communicate()

#     output = output.decode("utf-8").strip()
#     error = error.decode("utf-8").strip()

#     # Log command execution
#     command_log.append({"command": command, "output": output, "error": error})

#     return output, error

# def run_command(event=None):
#     """Handles command execution from the entry field."""
#     command = input_text.get("1.0", tk.END).strip()
#     if command:
#         output, error = execute_command(command)  # Execute the command
#         if command != "clear":
#             output_text.config(state=tk.NORMAL)  # Enable editing to insert output
#             output_text.insert(tk.END, f"> {command}\n")  # Show the command entered
#             if output:
#                 output_text.insert(tk.END, f"{output}\n")
#             if error:
#                 output_text.insert(tk.END, f"Error: {error}\n")
#             output_text.config(state=tk.DISABLED)  # Disable editing again
#         input_text.delete("1.0", tk.END)  # Clear input field
#         output_text.see(tk.END)  # Scroll to the end of the output

# def ask_gemini(event=None):
#     """Queries the Gemini AI based on the command log."""
#     history = "\n".join([f"Command: {entry['command']}\nOutput: {entry['output']}\nError: {entry['error']}" for entry in command_log])
#     user_query = chat_entry.get()
    
#     if user_query:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         chat_session = model.start_chat(
#             history=[{"role": "user", "parts": [history + "\n" + user_query]}]
#         )
#         response = chat_session.send_message(user_query)
        
#         # Process response text to remove special characters
#         clean_response = response.text.replace("*", "").replace("•", "").strip()
        
#         # Display response
#         chat_output_text.config(state=tk.NORMAL)  # Enable editing for output
#         chat_output_text.insert(tk.END, f"You: {user_query}\n", "bold")  # Use the bold tag
#         chat_output_text.insert(tk.END, f"Pranay's AI: {clean_response}\n\n", "bold")  # Use the bold tag
#         chat_output_text.config(state=tk.DISABLED)  # Disable editing again
#         chat_entry.delete(0, tk.END)  # Clear chat input

# # Create the main window
# root = tk.Tk()
# root.title("Command Line Assistant with AI")

# # Style the window to look like a command prompt
# root.configure(bg="black")

# # Create a frame for logo and label
# logo_frame = tk.Frame(root, bg="black")
# logo_frame.pack(side=tk.RIGHT, padx=10)

# # Load the image and create a label
# logo_image = Image.open("logo.png")  # Make sure to provide the correct path to your image
# logo_image = logo_image.resize((450, 200), Image.LANCZOS)  # Resize if necessary
# logo_photo = ImageTk.PhotoImage(logo_image)
# logo_label = tk.Label(logo_frame, image=logo_photo, bg="black")
# logo_label.pack()

# # Output text area
# output_text = tk.Text(root, height=20, width=80, bg="black", fg="white", insertbackground="green", state=tk.DISABLED)
# output_text.pack(pady=10)

# # Input text area
# input_text = tk.Text(root, height=1, width=80, bg="black", fg="white", insertbackground="green")
# input_text.pack(pady=10)
# input_text.bind("<Return>", run_command)  # Execute command on Enter key

# # Chat area for AI interactions
# chat_frame = tk.Frame(root, bg="black")
# chat_frame.pack(pady=10)

# chat_entry = tk.Entry(chat_frame, width=60)
# chat_entry.pack(side=tk.LEFT, padx=5)
# chat_entry.bind("<Return>", ask_gemini)  # Execute AI command on Enter key

# # Ask AI button
# ask_button = tk.Button(chat_frame, text="Ask AI", command=ask_gemini, bg='white', fg='black')
# ask_button.pack(side=tk.RIGHT)

# chat_output_text = tk.Text(root, height=10, width=80, bg="black", fg="white", insertbackground="green", state=tk.DISABLED)
# chat_output_text.pack(pady=10)

# # Define a tag for bold text
# chat_output_text.tag_configure("bold", font=("Helvetica", 10, "bold"))  # Set bold font

# # Run the application
# root.mainloop()















import os
import subprocess
import google.generativeai as genai
import tkinter as tk
from PIL import Image, ImageTk  # Import Image and ImageTk for image handling

# Configure your API key directly in the code
genai.configure(api_key="AIzaSyCAjkkf4L37uhSZ4jCmTzNcTZ0mQx8uEEI")

# Initialize a log to store command history and outputs
command_log = []
current_directory = os.getcwd()  # Track the current working directory

def execute_command(command):
    """Executes a shell command and captures its output and error."""
    global current_directory  # Use the global variable for current directory

    # Handle clear command to clear output text
    if command.strip() == "clear":
        output_text.config(state=tk.NORMAL)  # Enable editing for clearing
        output_text.delete("1.0", tk.END)  # Clear the output text area
        output_text.config(state=tk.DISABLED)  # Disable editing again
        command_log.append({"command": command, "output": "", "error": ""})
        return "", ""  # No output or error for the clear command

    # Handle cd command to change working directory
    if command.startswith("cd "):
        path = command[3:].strip()
        try:
            os.chdir(path)
            current_directory = os.getcwd()  # Update the tracked current directory
            output = f"Changed directory to {current_directory}"
            error = ""
            command_log.append({"command": command, "output": output, "error": error})
            return output, error
        except FileNotFoundError:
            error = f"cd: {path}: No such file or directory"
            command_log.append({"command": command, "output": "", "error": error})
            return "", error

    # Execute other commands in the current directory
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_directory)
    output, error = process.communicate()

    output = output.decode("utf-8").strip()
    error = error.decode("utf-8").strip()

    # Log command execution
    command_log.append({"command": command, "output": output, "error": error})

    return output, error

def run_command(event=None):
    """Handles command execution from the entry field."""
    command = input_text.get("1.0", tk.END).strip()
    if command:
        output, error = execute_command(command)  # Execute the command
        if command != "clear":
            output_text.config(state=tk.NORMAL)  # Enable editing to insert output
            output_text.insert(tk.END, f"> {command}\n", "bold")  # Show the command entered
            if output:
                output_text.insert(tk.END, f"{output}\n", "bold")  # Make the output bold
            if error:
                output_text.insert(tk.END, f"Error: {error}\n", "bold")  # Make the error bold
            output_text.config(state=tk.DISABLED)  # Disable editing again
        input_text.delete("1.0", tk.END)  # Clear input field
        output_text.see(tk.END)  # Scroll to the end of the output

def ask_gemini(event=None):
    """Queries the Gemini AI based on the command log."""
    history = "\n".join([f"Command: {entry['command']}\nOutput: {entry['output']}\nError: {entry['error']}" for entry in command_log])
    user_query = chat_entry.get()
    
    if user_query:
        model = genai.GenerativeModel("gemini-1.5-flash")
        chat_session = model.start_chat(
            history=[{"role": "user", "parts": [history + "\n" + user_query]}]
        )
        response = chat_session.send_message(user_query)
        
        # Process response text to remove special characters
        clean_response = response.text.replace("*", "").replace("•", "").strip()
        
        # Display response
        chat_output_text.config(state=tk.NORMAL)  # Enable editing for output
        chat_output_text.insert(tk.END, f"You: {user_query}\n", "bold")  # Use the bold tag
        chat_output_text.insert(tk.END, f"\nPranay's AI: {clean_response}\n\n", "bold")  # Use the bold tag
        chat_output_text.config(state=tk.DISABLED)  # Disable editing again
        chat_entry.delete(0, tk.END)  # Clear chat input

# Create the main window
root = tk.Tk()
root.title("Command Line Assistant with AI")

# Style the window to look like a command prompt
root.configure(bg="black")

# Create a frame for logo and label
logo_frame = tk.Frame(root, bg="black")
logo_frame.pack(side=tk.RIGHT, padx=10)

# Load the image and create a label
logo_image = Image.open("logo.png")  # Make sure to provide the correct path to your image
logo_image = logo_image.resize((450, 200), Image.LANCZOS)  # Resize if necessary
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(logo_frame, image=logo_photo, bg="black")
logo_label.pack()

# Output text area
output_text = tk.Text(root, height=20, width=80, bg="black", fg="white", insertbackground="green", state=tk.DISABLED)
output_text.pack(pady=10)

# Input text area
input_text = tk.Text(root, height=1, width=80, bg="black", fg="white", insertbackground="green")
input_text.pack(pady=10)
input_text.bind("<Return>", run_command)  # Execute command on Enter key

# Chat area for AI interactions
chat_frame = tk.Frame(root, bg="black")
chat_frame.pack(pady=10)

chat_entry = tk.Entry(chat_frame, width=60)
chat_entry.pack(side=tk.LEFT, padx=5)
chat_entry.bind("<Return>", ask_gemini)  # Execute AI command on Enter key

# Ask AI button
ask_button = tk.Button(chat_frame, text="Ask AI", command=ask_gemini, bg='white', fg='black')
ask_button.pack(side=tk.RIGHT)

chat_output_text = tk.Text(root, height=10, width=80, bg="black", fg="white", insertbackground="green", state=tk.DISABLED)
chat_output_text.pack(pady=10)

# Define a tag for bold text
chat_output_text.tag_configure("bold", font=("Helvetica", 10, "bold"))  # Set bold font
output_text.tag_configure("bold", font=("Helvetica", 10, "bold"))  # Set bold font for output text

# Run the application
root.mainloop()
