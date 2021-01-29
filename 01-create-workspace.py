from azureml.core import Workspace

ws = Workspace.create(name='learning-amlws-sandbox', # provide a name for your workspace
                      subscription_id='f97c158b-db60-40e4-b55b-653e3d5881e3', # provide your subscription ID
                      resource_group='leaning-rg', # provide a resource group name
                      create_resource_group=True,
                      location='eastus2') # For example: 'westeurope' or 'eastus2' or 'westus2' or 'southeastasia'.

# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')