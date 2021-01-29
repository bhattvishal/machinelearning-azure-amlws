# A control script allows you to run your hello.py script in the cloud. 
# You use the control script to control how and where your machine learning code is run.

# tutorial/03-run-hello.py
from azureml.core import Workspace, Experiment, Environment, ScriptRunConfig

ws = Workspace.from_config()
experiment = Experiment(workspace=ws, name='day1-experiment-hello')

config = ScriptRunConfig(source_directory='./src', script='hello.py', compute_target='cpu-cluster-01')

run = experiment.submit(config)
aml_url = run.get_portal_url()
print(aml_url)