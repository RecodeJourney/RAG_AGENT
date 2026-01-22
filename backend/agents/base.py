from abc import ABC, abstractmethod
from typing import Dict


class BaseAgent(ABC):
    @abstractmethod
    def run(self, input_data: Dict) -> Dict:
        pass
