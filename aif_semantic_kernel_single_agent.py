import os
from pathlib import Path

from semantic_kernel.agents import AzureAIAgentThread
from semantic_kernel.functions import kernel_function
from typing import Annotated

from aif_semantic_kernel_agent import AIF_SemanticKernelAgent

# Class definition to execute semantic kernal using an agent.
class AIF_SemanticKernelSingle(AIF_SemanticKernelAgent):
    # constructor of the class
    def __init__(self):
        try:
            super().__init__()
            self.expenses_agent_name = os.getenv("EXPENSE_AGENT_NAME")
        except Exception as ex:
            print(ex)
        
    # Load the expnses data file
    async def load_data(self):
        try:
            # Load the expnses data file
            script_dir = Path(__file__).parent
            file_path = script_dir / 'data.txt'
            with file_path.open('r') as file:
                self.expenses_data = file.read() + "\n"                  
            # Ask for a prompt
            self.user_prompt = input(f"Here is the expenses data in your file:\n{self.expenses_data}\nWhat would you like me to do with it?\n")                                    
        except Exception as ex:
            print(ex)
        
    # create an agent.
    async def create_agents(self):
        try:
            instructions="""You are an AI assistant for expense claim submission.
                                    When a user submits expenses data and requests an expense claim, use the plug-in function to send an email to expenses@contoso.com with the subject 'Expense Claim`and a body that contains itemized expenses with a total.
                                    Then confirm to the user that you've done so."""
            email_plugin = EmailPlugin()
            self.expenses_agent= await self.create_agent(self.expenses_agent_name, instructions, email_plugin)            
        except Exception as ex:
                print(ex)

    # execute a task requested to an agent.
    async def execute_task(self):
        # Use the agent to process the expenses data
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None    
        try:                
            # Add the input prompt to a list of messages to be submitted                
            prompt_messages = [f"{self.user_prompt}: {self.expenses_data}"]
            # Invoke the agent for the specified thread with the messages
            response = await self.expenses_agent.get_response(prompt_messages, thread=thread)
            # Display the response
            print(f"# {response.name}:\n{response}")        
        except Exception as ex:
            print(ex)
        finally:
            # Cleanup: Delete the thread
            await thread.delete() if thread else None  
    
    # Cleanup: Delete the agent
    async def delete_agents(self):
        try:
            await self.project_client.agents.delete_agent(self.expenses_agent.id)
        except Exception as ex:
            print(ex)
    
# Create a Plugin for the email functionality    
class EmailPlugin:
    """A Plugin to simulate email functionality."""
    
    @kernel_function(description="Sends an email.")
    def send_email(self,
                   to: Annotated[str, "Who to send the email to"],
                   subject: Annotated[str, "The subject of the email."],
                   body: Annotated[str, "The text body of the email."]):        
        print("\nTo:", to)
        print("Subject:", subject)
        print(body, "\n")