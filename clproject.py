import os
import subprocess
import google.generativeai as genai
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import queue
import sys
import argparse
import json
import time
from pathlib import Path

# Configure your API key
genai.configure(api_key="AIzaSyCAjkkf4L37uhSZ4jCmTzNcTZ0mQx8uEEI")

class CommandLineAssistant:
    def __init__(self, root=None):
        if root:
            self.root = root
            self.gui_mode = True
        else:
            self.gui_mode = False
            
        self.command_log = []
        self.current_directory = os.getcwd()
        self.command_history = []
        self.history_index = -1
        self.builtin_commands = {
            'help': self.show_help,
            'history': self.show_history,
            'clear': self.clear_output,
            'cd': self.change_directory,
            'pwd': self.print_working_directory,
            'exit': self.exit_app,
            'ls': self.list_directory,
            'dir': self.list_directory,
            'mkdir': self.make_directory,
            'rmdir': self.remove_directory,
            'touch': self.create_file,
            'rm': self.remove_file,
            'cat': self.display_file,
            'echo': self.echo_text,
            'env': self.show_environment,
            'which': self.which_command,
            'alias': self.manage_aliases,
            'export': self.export_variable
        }
        self.aliases = {}
        self.environment_vars = {}
        
        if self.gui_mode:
            self.setup_ui()
            self.update_directory_display()
        
    def setup_ui(self):
        # Configure main window with modern flat design
        self.root.title("◉ Command Line Pro - AI-Enhanced Terminal")
        self.root.configure(bg="#1e1e1e")
        self.root.geometry("1400x900")
        self.root.minsize(1000, 600)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Create main container with padding
        main_container = tk.Frame(self.root, bg="#1e1e1e")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create horizontal layout: main content on left, AI panel on right
        self.content_frame = tk.Frame(main_container, bg="#1e1e1e")
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # AI Panel on the right (initially hidden)
        self.ai_panel = tk.Frame(main_container, bg="#0d1117", width=400)
        self.ai_panel_visible = False
        
        # Header section with clean typography
        header_frame = tk.Frame(self.content_frame, bg="#1e1e1e")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Modern title with subtle icon
        title_label = tk.Label(
            header_frame, 
            text="◉ Command Line Pro", 
            bg="#1e1e1e", 
            fg="#ffffff", 
            font=("Segoe UI", 24, "normal")
        )
        title_label.pack(side=tk.LEFT)
        
        # Status indicators
        status_frame = tk.Frame(header_frame, bg="#1e1e1e")
        status_frame.pack(side=tk.RIGHT)
        
        # Current directory with modern styling
        self.dir_label = tk.Label(
            status_frame, 
            text="", 
            bg="#2d2d2d", 
            fg="#a0a0a0", 
            font=("Consolas", 10),
            padx=12,
            pady=4
        )
        self.dir_label.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Main content area with clean layout
        content_frame = tk.Frame(self.content_frame, bg="#1e1e1e")
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Terminal output section
        output_frame = tk.Frame(content_frame, bg="#1e1e1e")
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Output text with terminal-like appearance
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            bg="#0d1117",
            fg="#f0f6fc",
            insertbackground="#58a6ff",
            font=("JetBrains Mono", 11),
            wrap=tk.WORD,
            state=tk.DISABLED,
            selectbackground="#264f78",
            selectforeground="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            padx=15,
            pady=15
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure syntax highlighting tags
        self.output_text.tag_configure("command", foreground="#58a6ff", font=("JetBrains Mono", 11, "bold"))
        self.output_text.tag_configure("error", foreground="#f85149")
        self.output_text.tag_configure("success", foreground="#3fb950")
        self.output_text.tag_configure("warning", foreground="#d29922")
        self.output_text.tag_configure("directory", foreground="#79c0ff")
        self.output_text.tag_configure("file", foreground="#f0f6fc")
        self.output_text.tag_configure("prompt", foreground="#7c3aed")
        
        # Command input section with modern design
        input_frame = tk.Frame(content_frame, bg="#1e1e1e")
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Input container with border
        input_container = tk.Frame(input_frame, bg="#0d1117", relief=tk.FLAT, bd=1)
        input_container.pack(fill=tk.X)
        
        # Prompt indicator
        prompt_label = tk.Label(
            input_container, 
            text="❯", 
            bg="#0d1117", 
            fg="#58a6ff", 
            font=("JetBrains Mono", 14, "bold")
        )
        prompt_label.pack(side=tk.LEFT, padx=(15, 8), pady=12)
        
        # Command entry with modern styling
        self.command_entry = tk.Entry(
            input_container,
            bg="#0d1117",
            fg="#f0f6fc",
            insertbackground="#58a6ff",
            font=("JetBrains Mono", 12),
            relief=tk.FLAT,
            borderwidth=0,
            highlightthickness=0
        )
        self.command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=12, padx=(0, 15))
        self.command_entry.bind("<Return>", self.run_command)
        self.command_entry.bind("<Up>", self.history_up)
        self.command_entry.bind("<Down>", self.history_down)
        self.command_entry.bind("<Tab>", self.tab_completion)
        self.command_entry.focus_set()
        
        # Action buttons with clean design
        button_frame = tk.Frame(content_frame, bg="#1e1e1e")
        button_frame.pack(fill=tk.X)
        
        # Execute button
        execute_btn = tk.Button(
            button_frame,
            text="Execute",
            command=self.run_command,
            bg="#238636",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            borderwidth=0
        )
        execute_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        clear_btn = tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_output,
            bg="#21262d",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            borderwidth=0
        )
        clear_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # AI Assistant button
        ai_btn = tk.Button(
            button_frame,
            text="🤖 AI Assistant",
            command=self.toggle_ai_panel,
            bg="#7c3aed",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            borderwidth=0
        )
        ai_btn.pack(side=tk.RIGHT)
        
        # Setup AI Panel (right side)
        self.setup_ai_panel()
        
        # Welcome message with professional tone
        self.insert_output("◉ Command Line Pro - AI-Enhanced Terminal\n", "success")
        self.insert_output("━" * 50 + "\n", "directory")
        self.insert_output("Ready for commands. Type 'help' for available commands.\n\n", "file")

    def setup_ai_panel(self):
        """Setup the AI assistant panel on the right side"""
        # AI Panel Header
        ai_header = tk.Frame(self.ai_panel, bg="#0d1117")
        ai_header.pack(fill=tk.X, padx=15, pady=(15, 10))
        
        # AI Panel Title
        ai_title = tk.Label(
            ai_header,
            text="🤖 AI Assistant",
            bg="#0d1117",
            fg="#f0f6fc",
            font=("Segoe UI", 14, "bold")
        )
        ai_title.pack(side=tk.LEFT)
        
        # Close button
        close_btn = tk.Button(
            ai_header,
            text="✕",
            command=self.toggle_ai_panel,
            bg="#0d1117",
            fg="#8b949e",
            font=("Segoe UI", 12),
            relief=tk.FLAT,
            borderwidth=0,
            cursor="hand2",
            width=2
        )
        close_btn.pack(side=tk.RIGHT)
        
        # AI Chat output area
        self.ai_output = scrolledtext.ScrolledText(
            self.ai_panel,
            bg="#0d1117",
            fg="#f0f6fc",
            insertbackground="#7c3aed",
            font=("Segoe UI", 10),
            wrap=tk.WORD,
            state=tk.DISABLED,
            selectbackground="#264f78",
            selectforeground="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            padx=15,
            pady=10
        )
        self.ai_output.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))
        
        # AI input section at bottom
        ai_input_frame = tk.Frame(self.ai_panel, bg="#0d1117")
        ai_input_frame.pack(fill=tk.X, padx=15, pady=(0, 15))
        
        # Input container with border
        ai_input_container = tk.Frame(ai_input_frame, bg="#21262d", relief=tk.FLAT, bd=1)
        ai_input_container.pack(fill=tk.X)
        
        # AI input entry
        self.ai_entry = tk.Entry(
            ai_input_container,
            bg="#21262d",
            fg="#f0f6fc",
            insertbackground="#7c3aed",
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            borderwidth=0,
            highlightthickness=0
        )
        self.ai_entry.pack(fill=tk.X, padx=12, pady=10)
        self.ai_entry.bind("<Return>", self.ask_ai)
        
        # Placeholder text
        self.ai_entry.insert(0, "Ask anything about your commands...")
        self.ai_entry.bind("<FocusIn>", self.clear_ai_placeholder)
        self.ai_entry.bind("<FocusOut>", self.restore_ai_placeholder)
        self.ai_entry.config(fg="#8b949e")
        
        # Send button
        send_btn = tk.Button(
            ai_input_frame,
            text="Send",
            command=self.ask_ai,
            bg="#238636",
            fg="white",
            font=("Segoe UI", 9, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=6,
            cursor="hand2",
            borderwidth=0
        )
        send_btn.pack(pady=(5, 0))
        
        # Configure AI response tags
        self.ai_output.tag_configure("user", foreground="#58a6ff", font=("Segoe UI", 10, "bold"))
        self.ai_output.tag_configure("ai", foreground="#f0f6fc", font=("Segoe UI", 10))
        self.ai_output.tag_configure("ai_header", foreground="#3fb950", font=("Segoe UI", 10, "bold"))
        
        # Add welcome message to AI panel
        self.ai_output.config(state=tk.NORMAL)
        self.ai_output.insert(tk.END, "🤖 AI Assistant Ready\n", "ai_header")
        self.ai_output.insert(tk.END, "Ask me anything about commands, troubleshooting, or system help!\n\n", "ai")
        self.ai_output.config(state=tk.DISABLED)

    def clear_ai_placeholder(self, event):
        """Clear placeholder text when AI input is focused"""
        if self.ai_entry.get() == "Ask anything about your commands...":
            self.ai_entry.delete(0, tk.END)
            self.ai_entry.config(fg="#f0f6fc")

    def restore_ai_placeholder(self, event):
        """Restore placeholder text when AI input loses focus and is empty"""
        if not self.ai_entry.get():
            self.ai_entry.insert(0, "Ask anything about your commands...")
            self.ai_entry.config(fg="#8b949e")

    def toggle_ai_panel(self):
        """Toggle AI assistant panel visibility on the right side"""
        if self.ai_panel_visible:
            # Hide AI panel
            self.ai_panel.pack_forget()
            self.ai_panel_visible = False
            # Expand main content to full width
            self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        else:
            # Show AI panel on the right
            self.ai_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=(20, 0))
            self.ai_panel_visible = True
            # Focus on AI input
            self.ai_entry.focus_set()
            if self.ai_entry.get() == "Ask anything about your commands...":
                self.ai_entry.select_range(0, tk.END)

    def update_directory_display(self):
        """Update the current directory display"""
        if self.gui_mode:
            dir_text = f"📁 {os.path.basename(self.current_directory) or self.current_directory}"
            self.dir_label.config(text=dir_text)

    def insert_output(self, text, tag="file"):
        """Insert text into output area with styling"""
        if self.gui_mode:
            self.output_text.config(state=tk.NORMAL)
            self.output_text.insert(tk.END, text, tag)
            self.output_text.config(state=tk.DISABLED)
            self.output_text.see(tk.END)
        else:
            print(text, end='')

    def execute_command(self, command):
        """Execute shell command with enhanced functionality"""
        command = command.strip()
        if not command:
            return "", ""

        # Handle built-in commands
        cmd_parts = command.split()
        base_cmd = cmd_parts[0]
        
        # Check for aliases
        if base_cmd in self.aliases:
            command = command.replace(base_cmd, self.aliases[base_cmd], 1)
            cmd_parts = command.split()
            base_cmd = cmd_parts[0]
        
        if base_cmd in self.builtin_commands:
            try:
                return self.builtin_commands[base_cmd](cmd_parts[1:] if len(cmd_parts) > 1 else [])
            except Exception as e:
                return "", f"Error in {base_cmd}: {str(e)}"

        # Handle environment variable expansion
        for var, value in self.environment_vars.items():
            command = command.replace(f"${var}", value)
            command = command.replace(f"${{{var}}}", value)

        try:
            # Execute external command
            process = subprocess.Popen(
                command, 
                shell=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                cwd=self.current_directory,
                text=True,
                encoding='utf-8'
            )
            
            output, error = process.communicate(timeout=30)  # 30 second timeout
            
            # Log command execution
            self.command_log.append({
                "command": command, 
                "output": output.strip(), 
                "error": error.strip(),
                "return_code": process.returncode,
                "directory": self.current_directory,
                "timestamp": time.time()
            })
            
            return output.strip(), error.strip()
            
        except subprocess.TimeoutExpired:
            return "", "Command timed out after 30 seconds"
        except Exception as e:
            error_msg = f"Failed to execute command: {str(e)}"
            self.command_log.append({
                "command": command, 
                "output": "", 
                "error": error_msg,
                "return_code": -1,
                "directory": self.current_directory,
                "timestamp": time.time()
            })
            return "", error_msg

    # Built-in command implementations
    def show_help(self, args):
        """Display help information"""
        help_text = """
◉ Built-in Commands:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

File & Directory Operations:
  ls, dir [path]           - List directory contents
  cd <path>               - Change directory
  pwd                     - Print working directory
  mkdir <name>            - Create directory
  rmdir <name>            - Remove directory
  touch <file>            - Create empty file
  rm <file>               - Remove file
  cat <file>              - Display file contents

System & Environment:
  env                     - Show environment variables
  export <var>=<value>    - Set environment variable
  which <command>         - Show command location
  echo <text>             - Display text
  alias <name>=<command>  - Create command alias

Terminal Control:
  clear                   - Clear terminal output
  history                 - Show command history
  help                    - Show this help
  exit                    - Exit application

Navigation Tips:
  • Use ↑/↓ arrow keys for command history
  • Tab for auto-completion (coming soon)
  • Type partial commands and get suggestions

AI Assistant:
  • Click 🤖 AI Assistant to toggle AI panel
  • Ask questions about commands, errors, or systems
  • Get intelligent suggestions and troubleshooting

"""
        return help_text, ""

    def show_history(self, args):
        """Show command history"""
        if not self.command_history:
            return "No command history available.\n", ""
        
        history_text = "Command History:\n" + "─" * 30 + "\n"
        for i, cmd in enumerate(self.command_history[-20:], 1):  # Show last 20 commands
            history_text += f"{i:2d}. {cmd}\n"
        return history_text, ""

    def clear_output(self, args=None):
        """Clear the output display"""
        if self.gui_mode:
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.config(state=tk.DISABLED)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
        return "", ""

    def change_directory(self, args):
        """Change current directory"""
        if not args:
            # Go to home directory
            target = os.path.expanduser("~")
        else:
            target = args[0]
            
        try:
            # Expand user path and resolve relative paths
            target = os.path.expanduser(target)
            target = os.path.abspath(os.path.join(self.current_directory, target))
            
            if os.path.isdir(target):
                os.chdir(target)
                self.current_directory = os.getcwd()
                self.update_directory_display()
                return f"Changed directory to: {self.current_directory}\n", ""
            else:
                return "", f"Directory not found: {target}"
        except PermissionError:
            return "", f"Permission denied: {target}"
        except Exception as e:
            return "", f"Error changing directory: {str(e)}"

    def print_working_directory(self, args):
        """Print current working directory"""
        return f"{self.current_directory}\n", ""

    def list_directory(self, args):
        """List directory contents with enhanced formatting"""
        try:
            target_dir = args[0] if args else self.current_directory
            target_dir = os.path.expanduser(target_dir)
            target_dir = os.path.abspath(os.path.join(self.current_directory, target_dir))
            
            if not os.path.isdir(target_dir):
                return "", f"Not a directory: {target_dir}"
            
            items = []
            try:
                entries = sorted(os.listdir(target_dir))
                for entry in entries:
                    path = os.path.join(target_dir, entry)
                    if os.path.isdir(path):
                        items.append(f"📁 {entry}/")
                    else:
                        # Get file size
                        try:
                            size = os.path.getsize(path)
                            if size < 1024:
                                size_str = f"{size}B"
                            elif size < 1024*1024:
                                size_str = f"{size//1024}KB"
                            else:
                                size_str = f"{size//(1024*1024)}MB"
                            items.append(f"📄 {entry} ({size_str})")
                        except:
                            items.append(f"📄 {entry}")
                
                result = f"Contents of {target_dir}:\n"
                result += "─" * (len(result) - 1) + "\n"
                if items:
                    result += "\n".join(items) + "\n"
                else:
                    result += "(empty directory)\n"
                return result, ""
                
            except PermissionError:
                return "", f"Permission denied: {target_dir}"
        except Exception as e:
            return "", f"Error listing directory: {str(e)}"

    def make_directory(self, args):
        """Create a new directory"""
        if not args:
            return "", "Usage: mkdir <directory_name>"
        
        dir_name = args[0]
        try:
            dir_path = os.path.join(self.current_directory, dir_name)
            os.makedirs(dir_path, exist_ok=True)
            return f"Directory created: {dir_name}\n", ""
        except Exception as e:
            return "", f"Error creating directory: {str(e)}"

    def remove_directory(self, args):
        """Remove a directory"""
        if not args:
            return "", "Usage: rmdir <directory_name>"
        
        dir_name = args[0]
        try:
            dir_path = os.path.join(self.current_directory, dir_name)
            os.rmdir(dir_path)
            return f"Directory removed: {dir_name}\n", ""
        except FileNotFoundError:
            return "", f"Directory not found: {dir_name}"
        except OSError as e:
            if "not empty" in str(e).lower():
                return "", f"Directory not empty: {dir_name}"
            return "", f"Error removing directory: {str(e)}"

    def create_file(self, args):
        """Create an empty file"""
        if not args:
            return "", "Usage: touch <filename>"
        
        filename = args[0]
        try:
            file_path = os.path.join(self.current_directory, filename)
            Path(file_path).touch()
            return f"File created: {filename}\n", ""
        except Exception as e:
            return "", f"Error creating file: {str(e)}"

    def remove_file(self, args):
        """Remove a file"""
        if not args:
            return "", "Usage: rm <filename>"
        
        filename = args[0]
        try:
            file_path = os.path.join(self.current_directory, filename)
            os.remove(file_path)
            return f"File removed: {filename}\n", ""
        except FileNotFoundError:
            return "", f"File not found: {filename}"
        except Exception as e:
            return "", f"Error removing file: {str(e)}"

    def display_file(self, args):
        """Display file contents"""
        if not args:
            return "", "Usage: cat <filename>"
        
        filename = args[0]
        try:
            file_path = os.path.join(self.current_directory, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return f"Contents of {filename}:\n{'─' * 20}\n{content}\n", ""
        except FileNotFoundError:
            return "", f"File not found: {filename}"
        except UnicodeDecodeError:
            return "", f"Cannot display binary file: {filename}"
        except Exception as e:
            return "", f"Error reading file: {str(e)}"

    def echo_text(self, args):
        """Echo text to output"""
        text = " ".join(args) if args else ""
        return f"{text}\n", ""

    def show_environment(self, args):
        """Show environment variables"""
        env_text = "Environment Variables:\n" + "─" * 25 + "\n"
        
        # Show custom environment variables first
        if self.environment_vars:
            env_text += "Custom Variables:\n"
            for var, value in self.environment_vars.items():
                env_text += f"  {var}={value}\n"
            env_text += "\n"
        
        # Show system environment variables (limited)
        env_text += "System Variables (selected):\n"
        important_vars = ['PATH', 'HOME', 'USER', 'USERPROFILE', 'COMPUTERNAME', 'OS']
        for var in important_vars:
            value = os.environ.get(var, 'Not set')
            if len(value) > 50:
                value = value[:47] + "..."
            env_text += f"  {var}={value}\n"
        
        return env_text, ""

    def which_command(self, args):
        """Find location of a command"""
        if not args:
            return "", "Usage: which <command>"
        
        command = args[0]
        try:
            result = subprocess.run(['where' if os.name == 'nt' else 'which', command], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                return f"Location of {command}:\n{result.stdout}", ""
            else:
                return "", f"Command not found: {command}"
        except Exception as e:
            return "", f"Error finding command: {str(e)}"

    def manage_aliases(self, args):
        """Manage command aliases"""
        if not args:
            # Show all aliases
            if self.aliases:
                result = "Command Aliases:\n" + "─" * 16 + "\n"
                for alias, command in self.aliases.items():
                    result += f"  {alias} → {command}\n"
                return result, ""
            else:
                return "No aliases defined.\n", ""
        
        # Set alias
        alias_def = " ".join(args)
        if "=" in alias_def:
            alias, command = alias_def.split("=", 1)
            self.aliases[alias.strip()] = command.strip()
            return f"Alias created: {alias.strip()} → {command.strip()}\n", ""
        else:
            return "", "Usage: alias <name>=<command>"

    def export_variable(self, args):
        """Export environment variable"""
        if not args:
            return "", "Usage: export <var>=<value>"
        
        var_def = " ".join(args)
        if "=" in var_def:
            var, value = var_def.split("=", 1)
            self.environment_vars[var.strip()] = value.strip()
            return f"Variable exported: {var.strip()}={value.strip()}\n", ""
        else:
            return "", "Usage: export <var>=<value>"

    def exit_app(self, args):
        """Exit the application"""
        if self.gui_mode:
            self.root.quit()
        else:
            sys.exit(0)
        return "Goodbye!\n", ""

    def run_command(self, event=None):
        """Execute command from input field"""
        if not self.gui_mode:
            return
            
        command = self.command_entry.get().strip()
        if not command:
            return
        
        # Add to history
        if command not in self.command_history:
            self.command_history.append(command)
        self.history_index = len(self.command_history)
        
        # Clear input
        self.command_entry.delete(0, tk.END)
        
        # Display command
        self.insert_output(f"❯ {command}\n", "prompt")
        
        # Execute command
        try:
            output, error = self.execute_command(command)
            
            if output:
                self.insert_output(output, "file")
            if error:
                self.insert_output(f"Error: {error}\n", "error")
        except Exception as e:
            self.insert_output(f"Unexpected error: {str(e)}\n", "error")

    def history_up(self, event):
        """Navigate command history up"""
        if self.command_history and self.history_index > 0:
            self.history_index -= 1
            self.command_entry.delete(0, tk.END)
            self.command_entry.insert(0, self.command_history[self.history_index])

    def history_down(self, event):
        """Navigate command history down"""
        if self.command_history and self.history_index < len(self.command_history) - 1:
            self.history_index += 1
            self.command_entry.delete(0, tk.END)
            self.command_entry.insert(0, self.command_history[self.history_index])
        elif self.history_index == len(self.command_history) - 1:
            self.history_index = len(self.command_history)
            self.command_entry.delete(0, tk.END)

    def tab_completion(self, event):
        """Basic tab completion for files and directories"""
        current_input = self.command_entry.get()
        parts = current_input.split()
        
        if not parts:
            return "break"
        
        # Get the last part (what we're trying to complete)
        to_complete = parts[-1]
        
        try:
            # Get directory path
            if "/" in to_complete or "\\" in to_complete:
                dir_path = os.path.dirname(to_complete)
                filename_part = os.path.basename(to_complete)
                search_dir = os.path.join(self.current_directory, dir_path)
            else:
                dir_path = ""
                filename_part = to_complete
                search_dir = self.current_directory
            
            # Find matches
            matches = []
            if os.path.isdir(search_dir):
                for item in os.listdir(search_dir):
                    if item.startswith(filename_part):
                        if dir_path:
                            matches.append(os.path.join(dir_path, item))
                        else:
                            matches.append(item)
            
            if len(matches) == 1:
                # Single match - complete it
                new_input = " ".join(parts[:-1] + [matches[0]])
                if len(parts) > 1:
                    new_input = " ".join(parts[:-1]) + " " + matches[0]
                else:
                    new_input = matches[0]
                
                self.command_entry.delete(0, tk.END)
                self.command_entry.insert(0, new_input)
            elif len(matches) > 1:
                # Multiple matches - show them
                self.insert_output(f"\nPossible completions:\n", "directory")
                for match in matches[:10]:  # Show first 10 matches
                    self.insert_output(f"  {match}\n", "file")
                if len(matches) > 10:
                    self.insert_output(f"  ... and {len(matches) - 10} more\n", "directory")
        except:
            pass  # Ignore completion errors
        
        return "break"  # Prevent default tab behavior

    def ask_ai(self, event=None):
        """Query AI assistant"""
        if not self.gui_mode:
            return
            
        user_query = self.ai_entry.get().strip()
        
        # Skip if it's placeholder text or empty
        if not user_query or user_query == "Ask anything about your commands...":
            return
        
        # Clear input and restore placeholder
        self.ai_entry.delete(0, tk.END)
        self.ai_entry.insert(0, "Ask anything about your commands...")
        self.ai_entry.config(fg="#8b949e")
        
        # Display user query
        self.ai_output.config(state=tk.NORMAL)
        self.ai_output.insert(tk.END, f"👤 You: {user_query}\n\n", "user")
        self.ai_output.config(state=tk.DISABLED)
        self.ai_output.see(tk.END)
        
        # Run AI query in separate thread to avoid blocking UI
        def ai_thread():
            try:
                # Prepare context
                recent_commands = []
                for entry in self.command_log[-5:]:  # Last 5 commands
                    recent_commands.append(f"Command: {entry['command']}")
                    if entry['output']:
                        recent_commands.append(f"Output: {entry['output'][:200]}...")
                    if entry['error']:
                        recent_commands.append(f"Error: {entry['error']}")
                
                context = "\n".join(recent_commands)
                full_query = f"Recent terminal session:\n{context}\n\nUser question: {user_query}"
                
                # Query AI
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(full_query)
                
                # Display response
                clean_response = response.text.replace("*", "").replace("•", "").strip()
                
                def update_ui():
                    self.ai_output.config(state=tk.NORMAL)
                    self.ai_output.insert(tk.END, f"🤖 AI Assistant: ", "ai_header")
                    self.ai_output.insert(tk.END, f"{clean_response}\n\n", "ai")
                    self.ai_output.config(state=tk.DISABLED)
                    self.ai_output.see(tk.END)
                
                self.root.after(0, update_ui)
                
            except Exception as e:
                def show_error():
                    self.ai_output.config(state=tk.NORMAL)
                    self.ai_output.insert(tk.END, f"🤖 AI Assistant: ", "ai_header")
                    self.ai_output.insert(tk.END, f"Sorry, I encountered an error: {str(e)}\n\n", "ai")
                    self.ai_output.config(state=tk.DISABLED)
                    self.ai_output.see(tk.END)
                
                self.root.after(0, show_error)
        
        threading.Thread(target=ai_thread, daemon=True).start()

    def run_cli_mode(self):
        """Run in command-line interface mode"""
        print("◉ Command Line Pro - CLI Mode")
        print("━" * 40)
        print("Type 'help' for commands, 'exit' to quit")
        print()
        
        while True:
            try:
                # Show prompt
                prompt = f"❯ {os.path.basename(self.current_directory)} $ "
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                # Add to history
                if command not in self.command_history:
                    self.command_history.append(command)
                
                # Execute command
                output, error = self.execute_command(command)
                
                if output:
                    print(output)
                if error:
                    print(f"Error: {error}")
                    
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit.")
            except EOFError:
                break

def main():
    """Main function with argument parsing"""
    parser = argparse.ArgumentParser(description="Command Line Pro - AI-Enhanced Terminal")
    parser.add_argument("--cli", action="store_true", help="Run in CLI mode (no GUI)")
    parser.add_argument("--config", type=str, help="Configuration file path")
    
    args = parser.parse_args()
    
    if args.cli:
        # CLI mode
        assistant = CommandLineAssistant()
        assistant.run_cli_mode()
    else:
        # GUI mode
        root = tk.Tk()
        assistant = CommandLineAssistant(root)
        root.mainloop()

if __name__ == "__main__":
    main()
