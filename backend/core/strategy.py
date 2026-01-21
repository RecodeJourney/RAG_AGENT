from enum import Enum

class RAGStrategy(Enum):
    NAIVE = "naive"
    SIMPLE = "simple"
    MULTI_STEP = "multi_step"
    AGENTIC = "agentic"
    GRAPH = "graph"
    HYDE = "hyde"
    MULTIMODAL = "multimodal"