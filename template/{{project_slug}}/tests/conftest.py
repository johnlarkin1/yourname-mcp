"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def sample_query():
    """Provide a sample search query for testing."""
    return "python"
