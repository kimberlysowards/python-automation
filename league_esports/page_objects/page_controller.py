"""Controller that holds all the page objects.

Each website consists of pages and these pages are "controlled"
or centralized using a Page Controller. This not only increases readability,
but it also simplifies usage of the Page Objects.

Classes:
    - Pages

Usage:
    Each completed Page Object Model (POM) should be added
    as a property of the Pages class.

Example:
  1 def test_using_page_controller(self):
  2     pages = Pages(driver, wait)
  3     pages.home.goto()
  4     pages.league.goto("NA LCS")
  5     
  6     assert pages.league.map.schedule_tab.is_displayed


  1 def test_without_page_controller(self):
  2     home = HomePage(driver, wait)
  3     home.goto()
  4     league = LeaguePage(driver, wait)
  5     league.goto("NA LCS")
  6     
  7     assert league.map.schedule_tab.is_displayed
"""

__author__ = "Carlos Kidman"

from league_esports.page_objects.home import HomePage
from league_esports.page_objects.league import LeaguePage


class Pages:
    def __init__(self, driver, wait):
        self._home = HomePage(driver, wait)
        self._league = LeaguePage(driver, wait)
    
    @property
    def home(self):
        return self._home

    @property
    def league(self):
        return self._league
