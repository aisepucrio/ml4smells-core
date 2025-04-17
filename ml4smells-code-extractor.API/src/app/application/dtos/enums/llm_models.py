from enum import Enum

class LLMModels(str, Enum):
    gemma2_2b = "gemma2:2b"
    gpt_4o_mini = "gpt-4o-mini"
    mistral_latest = "mistral:latest"
    gpt_4o      = "gpt-4o"
