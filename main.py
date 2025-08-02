import os
import asyncio
from dotenv import load_dotenv

from aif_semantic_kernel_client_functions import execute_ai_agent

# main function
async def main():
    try:  
        # Starting the AI Foundary Project
        print('Starting the AI Foundary Project')
        # Initialization of configuration   
        load_dotenv() 
        # Execute an AI Agent 
        agent_type = os.getenv("AI_AGENT_TYPE")
        await execute_ai_agent(agent_type) 
        # Stopping the AI Foundary Project
        print('Stopping the AI Foundary Project')   
    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
     asyncio.run(main())