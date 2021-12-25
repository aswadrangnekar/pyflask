# pyflask
----------

# Github integration
From github UI a webhook needs to be added to point to the URL in format below

http://<jenkins.ip>:<jenkins.port>/github-webhook/

# Run tests
> for older versions of python
$ python -m unittest discover . -vvvv "test_*.py"
> for python3
$ python3 -m unittest discover . -vvvv -p "test_*.py"

# tag the image as below
docker build . -t "aswadrangnekar/pyflaskapp:v0.1.$(git rev-parse --short HEAD)"

# push the image to dockerhub
docker push aswadrangnekar/pyflaskapp:v0.1.$(git rev-parse --short HEAD)

