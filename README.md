Requirements before cloning:

- Make sure to have Python3 and PIP3 installed

Setting up the project:

- We must use a virtual environment for the Python app. We will do this using 'virtualenv' package
- Install 'virtualenv' with the command: sudo -H pip3 install virtualenv
- After cloning the repository, run the command: virtualenv pycrypt-rest/
- Then, cd into pycrypt-rest/
- Then, run the command: source bin/activate
- Then, install Flask library: bin/pip3 install flask
- Lastly, install pip install pyDes

Running the project:

- Run the command: bin/python3 rest.py
- The server will be hosted locally on port 3000

When adding new commits, make sure NOT to commit bin, lib, or pyvenv.cfg. These files are environment-dependent.
