Requirements before cloning:

- Make sure to have Python3 and PIP3 installed

Setting up the project:

- We must use a virtual environment for the Python app. We will do this using 'virtualenv' package
- Install 'virtualenv' with the command: sudo -H pip3 install virtualenv
- After cloning the repository, run the command: virtualenv pycrypt-rest/
- Then, cd into pycrypt-rest/
- Then, run the command: source bin/activate
- Lastly, install Flask library: bin/pip3 install flask

Running the project:

- Run the command: bin/python3 rest.py
- The server will be hosted locally on port 3000

When adding new commits, MAKE SURE NOT TO COMMIT bin, lib, or pyvenv.cfg. These files are environment-dependent.
