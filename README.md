# websocket_counter
A simple hit counter using python, flask, redis, and websockets

**Clone the git repo.**

Install Homebrew
http://mxcl.github.com/homebrew/

You'll need libevent for gevent for Flask-SocketIO: `brew install libevent`

You'll need pip: https://pip.pypa.io/en/latest/installing.html or `easy_install pip` or `sudo apt-get install python-pip`

I recommend using virtual environments, but you don't have to: http://docs.python-guide.org/en/latest/dev/virtualenvs/

In one terminal, make sure redis is running, or run it in the background: `redis-server`

In another terminal, run `python app.py`

When you're done, Cmd+C or Ctrl+C to stop app.py. Do the same for redis-server.