import pytest
from src.core.base_ingestor import BaseIngestor

# We create a dummy implementation to test the Base Class
class MockIngestor(BaseIngestor):
    def transform(self, data):
        return data.upper()

def test_base_ingestor_transform():
    ingestor = MockIngestor(config={})
    assert ingestor.transform("hello") == "HELLO"
