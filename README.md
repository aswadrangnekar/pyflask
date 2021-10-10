# pyflask
----------

# Github integration
From github UI a webhook needs to be added to point to the URL in format below

http://<jenkins.ip>:<jenkins.port>/github-webhook/

# Run tests
$ python -m unittest discover . -vvvv "test_*.py"
# if python3
$ python3 -m unittest discover . -vvvv -p "test_*.py"
