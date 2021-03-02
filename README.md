### ec2-instance-manager

### Set Up

Install python3, pip3 and virtualenv:

```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install virtualenv
```

Create a virtual environment and activate it:

```
virtualenv -p python3 ec2
. ec2/bin/activate

#To stop working on ec2 venv use: deactivate
```

Within the ec2 venv, install the serverless framework:

```sudo npm install -g serverless```


### Package Solution

To create an artifact of entire stack including CloudFormation, run:

```serverless package --package ec2-instance-manager```

### Deployment

The first deployment, the stack needs to be created on cloudformation, so edit `serverless.yml` to deploy everything together by removing the line `individually: true` of the service package block and then deploy everything with:

```
serverless deploy -v
```

After first deploy, edit `serverless.yml` adding the line `individually: true` of the service package block and deploy functions separately:

```
serverless deploy function --function change
serverless deploy function --function start
serverless deploy function --function stop
```

### Known Issues with deployment

AWS Lambda requires global read permissions on the uploaded zip, otherwise it might return an error that says something like `Permission Denied to /path/to/src`, to resolve that change your local repository files and directories permissions.

1. First, check permission on deployment zip: 

```bash

$ zipinfo test.zip
Archive:  test.zip
Zip file size: 473 bytes, number of entries: 2
-r--------  3.0 unx        0 bx stor 17-Aug-10 09:37 exlib.py
-r--------  3.0 unx      234 tx defN 17-Aug-10 09:37 index.py
2 files, 234 bytes uncompressed, 163 bytes compressed:  30.3%

```

2. If there is no global read permission add those to all files and directories of your repository: 

```bash
$ chmod 644 $(find $(pwd) -type f)
$ chmod 755 $(find $(pwd) -type d)
```

3. Generate a new deployment zip. Permissions on the zip now should look like this:

```bash
$ zipinfo test.zip
Archive:  test.zip
Zip file size: 473 bytes, number of entries: 2
-r--r--r--  3.0 unx        0 bx stor 17-Aug-10 09:37 exlib.py
-r--r--r--  3.0 unx      234 tx defN 17-Aug-10 09:37 index.py
2 files, 234 bytes uncompressed, 163 bytes compressed:  30.3%
```