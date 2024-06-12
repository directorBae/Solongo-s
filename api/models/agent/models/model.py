"""Agent Model Code, Detailed Code Architecture can be reformed.
But It's Recommended to keep the rule that the input and output of the model are defined using dataclasses."""

from dataclasses import dataclass

@dataclass
class AgentModelInput:
    """Agent Model Input"""
    
@dataclass
class AgentModelOutput:
    """Agent Model Output"""

class AgentModel:
    """Agent Model"""
    def __init__(self):
        pass

    def predict(self, input: AgentModelInput) -> AgentModelOutput:
        """Predict"""
        return AgentModelOutput()