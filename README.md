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

```serverless deploy -v```

To deploy specific function:

```serverless deploy function --function myFunction```
