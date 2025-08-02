
from aif_agent_factory import AIF_AgentFactory
from aif_semantic_kernel_multi_agent import AIF_SemanticKernelMultiAgent

# Derived Factory Class to create a support agent.
class AIF_IncidentAgentFactory(AIF_AgentFactory):
    def __init__(self):
        print("AIF_SupportAgentFactory")

    async def create_agent(self):
        return AIF_SemanticKernelMultiAgent()

