import ollama
from abc import ABC, abstractmethod
from infrastructure.config.settings import settings
from application.dtos.message_operation_input import MessageOperationInput


class LLMBaseService(ABC):
    def __init__(self):
        self.client = ollama.Client(host=settings.llm_ollama_host)

    @abstractmethod
    def send_message(self, type: MessageOperationInput):
        pass
