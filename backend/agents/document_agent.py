from typing import Dict
from .base import BaseAgent


class DocumentTypeAgent(BaseAgent):
    def run(self, input_data: Dict) -> Dict:
        return {
            "document_type": "unknown"
        }
