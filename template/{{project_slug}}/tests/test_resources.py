"""Tests for resource loading utilities."""

import pytest

from src.util.resources import list_resources, load_resource, search_resources


class TestLoadResource:
    """Tests for the load_resource function."""

    @pytest.mark.unit_test
    def test_load_nonexistent_resource_returns_message(self):
        """Loading a nonexistent resource should return a helpful message."""
        result = load_resource("nonexistent")
        assert "not found" in result.lower()

    @pytest.mark.unit_test
    def test_load_nonexistent_resource_raises_when_requested(self):
        """Loading a nonexistent resource with raise_on_error=True should raise."""
        from src.util.resources import ResourceNotFoundError

        with pytest.raises(ResourceNotFoundError):
            load_resource("nonexistent", raise_on_error=True)


class TestListResources:
    """Tests for the list_resources function."""

    @pytest.mark.unit_test
    def test_list_resources_returns_list(self):
        """list_resources should return a list."""
        result = list_resources()
        assert isinstance(result, list)


class TestSearchResources:
    """Tests for the search_resources function."""

    @pytest.mark.unit_test
    def test_search_empty_query_returns_empty(self):
        """Searching with an empty query should return empty results."""
        result = search_resources("")
        assert result == {}

    @pytest.mark.unit_test
    def test_search_whitespace_query_returns_empty(self):
        """Searching with only whitespace should return empty results."""
        result = search_resources("   ")
        assert result == {}

    @pytest.mark.unit_test
    def test_search_returns_dict(self, sample_query):
        """Search should return a dictionary."""
        result = search_resources(sample_query)
        assert isinstance(result, dict)
