import pytest
from bs4 import BeautifulSoup

def get_soup(file_path):
    """Reads an HTML file and returns a BeautifulSoup object."""
    with open(file_path, 'r') as f:
        return BeautifulSoup(f, 'html.parser')

def test_collections_link_is_correct():
    """
    Tests that the 'Collections' link in the main navigation of index.html
    points to 'collection.html'.
    """
    soup = get_soup('index.html')
    nav_links = soup.select('nav .hidden.md\\:block a')
    collections_link = None
    for link in nav_links:
        if 'Collections' in link.text:
            collections_link = link
            break

    assert collections_link is not None, "Could not find the 'Collections' link in the navigation."
    assert collections_link['href'] == 'collection.html', \
        f"The 'Collections' link should point to 'collection.html', but it points to '{collections_link['href']}'."
