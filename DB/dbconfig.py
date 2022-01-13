user = 'abc'
dsn =  "localhost/orclpdb1"
pw = "PYTHON_PASSWORD"
if pw is None:
    pw = getpass.getpass("Enter password for %s: " % user)