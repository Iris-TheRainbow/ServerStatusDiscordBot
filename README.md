# Server Status Discord bot

A discord bot intended to facilitate remote moitoring and management of a server without having direct access to it, either physical or SSH. 

## Features
- SSH like shell. Its very basic and many commands may not work, but it can do some basics like restarting services and working with files. It does have authentication, in the form of emailed one time codes sent via email
- Bot status. With a simple command, you can see the status of your discord bot
- Server status. You can get the current RAM and CPU usage, as well as your server uptime. You can also get the status of important services.
- Important serivces. You can configure a python file with important services for your server. If one of these services goes down, you will get a warning ping. Their status is also listed with the server's status.

## Manual
### SSH Authentication
You can request authentication with `$login` and an email will be sent to the email that is configured with a 64 character one time code that allows any text with `$` at the start to be run as a command
### SSH Commands
You can run any command that doesnt need any user input (like `mkdir`) with `$` at the start of the string (`$mkdir <directoryname>`
### Bot status
send a message that is just `bot status` in any channel.
### Server status
send a message that is just `status` in any channel

![image](https://github.com/user-attachments/assets/76892c51-8fc6-409b-863e-4ce29a06fb52)
