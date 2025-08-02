import os

from azure.identity.aio import DefaultAzureCredential
from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.agents import AzureAIAgentSettings

# AI Foundary Agent Client
class AIF_SemanticKernelAgent:    
    # constructor    
    def __init__(self):
        try:
            print("Connecting to agent...")                      
            # Clear the console
            os.system('cls' if os.name=='nt' else 'clear')
            # Load environment variables from .env file
            self.ai_project_endpoint = os.getenv("AI_PROJECT_ENDPOINT")
            self.model_deployment_name = os.getenv("MODEL_DEPLOYMENT_NAME")                

            # Get configuration settings
            self.ai_agent_settings = AzureAIAgentSettings(
                model_deployment_name=self.model_deployment_name,
                endpoint=self.ai_project_endpoint,
            )                    
        except Exception as ex:
            print(ex)
    
    # create an agent.
    async def create_agent(self, name, instructions, plugin_class):
        try:
            # Define an Azure AI agent that sends an expense claim email
            ai_agent_def = await self.project_client.agents.create_agent(
                model= self.ai_agent_settings.model_deployment_name,
                name= name,
                instructions=instructions
                )            
            # Create a semantic kernel agent
            agent = AzureAIAgent(
                client=self.project_client,
                definition=ai_agent_def,
                plugins=[plugin_class]
            )
            return agent
        except Exception as ex:
                print(ex)
    
    # Ask for a prompt
    async def load_data(self):
         raise NotImplementedError("This method should be overridden.")
    # create an agent or multiple agents.
    async def create_agents(self):
        raise NotImplementedError("This method should be overridden.")
    # execute a task requested to an agent.
    async def execute_task(self):
        raise NotImplementedError("This method should be overridden.")
    # Cleanup: Delete an agent or agents.
    async def delete_agents(self):
        raise NotImplementedError("This method should be overridden.")
    # execute an agent to complete a task.
    # process data function
    async def process_data(self):
        try:
            await self.create_agents()                        
            await self.execute_task()            
        except Exception as ex:
                print(ex) 
        finally:
            # Cleanup: Delete an agent or agents.
            await self.delete_agents()
    
    # function to run the agent
    async def execute_agent(self):
        try:                                   
            # Ask for a prompt
            await self.load_data()   
            # Connect to the Azure AI Foundry project
            async with (
                DefaultAzureCredential(
                    exclude_environment_credential=True,
                    exclude_managed_identity_credential=True) as creds,
                AzureAIAgent.create_client(
                    credential=creds,
                    endpoint= self.ai_agent_settings.endpoint
                ) as self.project_client,
            ):
                # execute a task by the agent.
                await self.process_data()        
        except Exception as ex:
                print(ex)     
