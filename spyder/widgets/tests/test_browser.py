# -*- coding: utf-8 -*-
#
# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
#

"""
Tests for browser.py
"""

# Test library imports
import pytest

# Local imports
from spyder.widgets.browser import WebBrowser

from qtpy.QtCore import QUrl

@pytest.fixture
def browser(qtbot):
    """Set up WebBrowser."""
    widget = WebBrowser()
    qtbot.addWidget(widget)
    return widget    

def test_browser(browser):
    """Run web browser."""
    browser.set_home_url('https://www.google.com/')
    browser.go_home()
    browser.show()
    assert browser
    
def test_text_to_url(browser):
    browser.text_to_url('https://www.google.com/')
    browser.show()
    assert browser
    
def test_url_to_text(browser):
    browser.url_to_text(QUrl('https://www.google.com/'))
    browser.show()
    assert browser
    

    
    
    
if __name__ == "__main__":
    pytest.main()
