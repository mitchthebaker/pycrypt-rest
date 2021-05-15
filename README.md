Requirements before cloning:

- Make sure to have Python3 and PIP3 installed

Setting up the project:

- We must use a virtual environment for the Python app. We will do this using 'virtualenv' package
- Install 'virtualenv' with the command: sudo -H pip3 install virtualenv
- After cloning the repository, run the command: virtualenv pycrypt-rest/
- Then, cd into pycrypt-rest/
- Then, run the command: source bin/activate
- Then, install Flask library: bin/pip3 install flask
- Then, install pyDes: pip install pyDes (may also have to run bin/pip3 install pyDes for line_profiler)
- Lastly, install PyCrypto: pip install pycrypto (may also have to run bin/pip3 install pycrypto for line_profiler)

How to get a more complete breakdown of the time taken for each route:
- Run the command: pip install line_profiler
- Add @profile above the function or block of code to test
- Test the code with the command: kernprof -l -v rest.py
- From a browser/Postman, test an api route of choice. (example: http://localhost:3000/des?plaintext=hello&key=-8B%20key-)
- After the route finishes, ctrl + c in console and the output from line_profiler library will be displayed

Running the project:

- Run the command: bin/python3 rest.py
- The server will be hosted locally on port 3000

When adding new commits, make sure NOT to commit bin, lib, or pyvenv.cfg. These files are environment-dependent.