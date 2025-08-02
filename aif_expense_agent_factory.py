from aif_agent_factory import AIF_AgentFactory
from aif_semantic_kernel_single_agent import AIF_SemanticKernelSingle

# Derived Factory Class to create a data agent.
class AIF_ExpenseAgentFactory(AIF_AgentFactory):
    def __init__(self):
        print("AIF_ExpenseAgentFactory")

    async def create_agent(self):
        return AIF_SemanticKernelSingle()