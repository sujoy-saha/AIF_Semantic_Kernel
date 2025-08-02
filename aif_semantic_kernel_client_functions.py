from aif_expense_agent_factory import AIF_ExpenseAgentFactory
from aif_incident_agent_factory import AIF_IncidentAgentFactory

# function to create an agent.
async def create_agent(agent_type):
    try:
        agent_factory = None        
        if agent_type.lower() == "single":   
            agent_factory =  AIF_ExpenseAgentFactory()                  
        elif agent_type.lower() == "multi":                    
            agent_factory =  AIF_IncidentAgentFactory()                  
        else:
            raise ValueError("Unknown agent type. Use 'support' or 'data'.")        
        return await agent_factory.create_agent()
    except Exception as ex:
            print(ex)

# execute an AI agent.
async def execute_ai_agent(agent_type):
    try:
        # create an agent clinet
        agent_client = await create_agent(agent_type) 
        # execute an agent to complete activities.
        await agent_client.execute_agent()  
    except Exception as ex:
        print(ex)