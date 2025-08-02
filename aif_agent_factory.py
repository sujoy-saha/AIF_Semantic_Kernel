# Abstract Factory Class to create an agent.
class AIF_AgentFactory:
    async def create_agent(self):
        raise NotImplementedError("This method should be overridden.")
