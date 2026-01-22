from typing import Dict
from .base import BaseAgent


class ValidationAgent(BaseAgent):
    def run(self, input_data: Dict) -> Dict:
        return {
            "valid": True
        }
