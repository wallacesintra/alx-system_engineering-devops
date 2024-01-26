PID - Process ID
----------------
It is unique to identify a process on a system.

pidof process_name - return PID of the process.
pgrep process_name - return PID of all processes that match the name process_name.
ps -o ppid= -p PID - return the parent Process ID of the process with the given PID.

Linux process
-------------
Process - instance of a running computer program that you can find in an application/command.

ps - display info about the processes running on the system.
top - provides a real-time, dynamic view of the processes running on the system.
htop - similar to top, but more user-friendly interface.

[Types of processes]
foreground - depend on the user for input
            also referred to as interactive processes
background - run independently of the user
            referred to as non-interactive or automatic processes


[Process State]
    -running : it is running or it’s ready to run.
    -sleep : it is waiting for a resource to be available
    -stopped : when it receives a stop signal
    -zombie : when a process is dead but the entry for the process is still present in the table.



Linux Signal
------------
Signal - form of communication between process.