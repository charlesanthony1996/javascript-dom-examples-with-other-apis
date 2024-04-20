import os

# SECRET_KEY is stored as an environmental variable in your local machine

# to view all environmental variables (command line)
# command -> export -r

# to set an environment variable (command line)
# command -> export COLORTERM="charles"

# to change the same environment variable (command line)
# command -> source ~/.bashrc


secret_key = os.environ['COLORTERM']

print(secret_key)