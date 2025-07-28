# Remote Command Execution

<div align="center">

<img alt="GitHub Created At" src="https://img.shields.io/github/created-at/KieranPritchard/Remote-Command-Execution">

<img alt="GitHub License" src="https://img.shields.io/github/license/KieranPritchard/Remote-Command-Execution">

<img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/KieranPritchard/Remote-Command-Execution">

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/KieranPritchard/Remote-Command-Execution">

<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/KieranPritchard/Remote-Command-Execution">

<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/KieranPritchard/Remote-Command-Execution">

</div>

## Project Description

### Objective

To create a basic simulation of how remote command execution works, in order to understand the underlying mechanics and process.

### Technology and Tools Used

* **Language:** Python.
* **Tools:** Git, VS Code.

### Challenges Faced

I had trouble setting up the connection to the server script, because the ports I was using were already occupied by other applications on my computer. 
Once I resolved that by selecting a different port, the rest of the project went smoothly, as alot of the script was similar to things I had implemented in previous projects.

### Outcome

The project successfully simulates a basic remote command execution system. 
A server listens for incoming client connections, and once connected, the client can send commands which the server executes and returns the output. 
This helped solidify my understanding of socket programming, client-server architecture, and command handling. 
It also gave me hands-on experience with basic network debugging and error handling in Python.

## How to Use the Project

**1. Clone The Repository:**

* Use git to clone the project.

**2. Start the Server:**

* Open your terminal or command prompt.
* Navigate to the directory where you saved the files.
* Run the server script using the command:

```python server.py```

* You should see a message indicating that the server has started and is listening on 127.0.0.1:5001.

**3. Start the Client:**

* Open a new terminal or command prompt window.
* Navigate to the same directory where you saved the files.
* Run the client script using the command:
```
python client.py
```
* The client will attempt to connect to the server, and once connected, you will see a prompt: Please input a command: 

**4. Send Commands:

* In the client terminal, type any command you want to execute on the server (e.g., ls, dir, echo Hello World, whoami).
* Press Enter.
* The server will execute the command, and the output will be displayed in the client terminal.

**5. Disconnect:**

* To disconnect the client, you can typically press Ctrl+C in the client terminal. The server will detect the disconnection.
* To stop the server, press Ctrl+C in the server terminal.


## Licenses
License is found in the root of the repository.
