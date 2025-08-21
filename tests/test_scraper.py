import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from scraper import bing_search

def test_bing_search_returns_results():
    query = "planets"
    result_titles = bing_search(query)
    print("\nAutomation Results:")
    for i, title in enumerate(result_titles[:5], 1):
        print(f"{i}. {title}")
    assert len(result_titles) > 0, "No search results found"

def test_bing_search_returns_at_least_five_results():
    query = "planets"
    result_titles = bing_search(query)
    print("\nFirst Five Automation Results:")
    for i, title in enumerate(result_titles[:5], 1):
        print(f"{i}. {title}")
    assert len(result_titles) >= 5, "Less than five search results found"

def test_bing_search_first_result_contains_planet():
    query = "planets"
    result_titles = bing_search(query)
    if result_titles:
        print(f"\nFirst result: {result_titles[0]}")
        assert "planet" in result_titles[0].lower(), "First result does not mention 'planet'"
    else:
        pytest.fail("No search results found")
