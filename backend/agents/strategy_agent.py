from typing import Dict
from .base import BaseAgent
from backend.core.strategy import RAGStrategy


class StrategyAgent(BaseAgent):
    def run(self, input_data: Dict) -> Dict:
        return {
            "strategy": RAGStrategy.SIMPLE.value
        }
