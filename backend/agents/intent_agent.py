from typing import Dict
from .base import BaseAgent


class QueryIntentAgent(BaseAgent):
    def run(self, input_data: Dict) -> Dict:
        return {
            "intent": "unknown"
        }
