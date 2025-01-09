import os
import subprocess
import shlex


def execute_command(command):
    """
    Runs a shell command and supports pipes and I/O redirection.
    """
    # Use shlex to split the command into parts for proper handling
    parts = shlex.split(command)

    # Check for pipes (|) in the command
    if "|" in command:
        # Split the command into individual parts and set up piping
        commands = [shlex.split(cmd.strip()) for cmd in command.split("|")]
        prev_process = None

        for cmd in commands:
            if prev_process is None:
                prev_process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            else:
                prev_process = subprocess.Popen(cmd, stdin=prev_process.stdout, stdout=subprocess.PIPE)

        # Get the final output and any errors
        output, error = prev_process.communicate()
        return output.decode() if output else None, error

    # Check for I/O redirection ('>' or '<') in the command
    if ">" in parts or "<" in parts:
        if ">" in parts:
            # Redirect output to a file
            idx = parts.index(">")
            output_file = parts[idx + 1]
            cmd = parts[:idx]
            with open(output_file, "w") as outfile:
                result = subprocess.run(cmd, stdout=outfile, stderr=subprocess.PIPE, text=True)
            return None, result.stderr
        elif "<" in parts:
            # Redirect input from a file
            idx = parts.index("<")
            input_file = parts[idx + 1]
            cmd = parts[:idx]
            with open(input_file, "r") as infile:
                result = subprocess.run(cmd, stdin=infile, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return result.stdout, result.stderr

    # Run the command normally if there's no redirection or piping
    result = subprocess.run(parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr


def shell():
    """
    A simple shell program that runs user commands.
    """
    print("Welcome to 7.shell! Type 'exit' or 'quit' to leave.")
    while True:
        try:
            # Get the user command
            command = input("7.shell> ").strip()
            if command.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            # Execute the command and get the result
            output, error = execute_command(command)

            # Print the output or error (if any)
            if output:
                print(output, end="")
            if error:
                print(error, end="")
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nUse 'exit' or 'quit' to leave the shell.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    shell()
