# tests/test_twitch.py

import time
from tests.base_test import BaseTest
from pages.twitch_page import TwitchPage

class TestTwitch(BaseTest):

    def test_twitch_page_loads(self):
        """Test to verify that the Twitch page loads successfully."""
        twitch_page = TwitchPage(self.driver)
        twitch_page.load()
        assert twitch_page.is_loaded(), "Twitch page did not load successfully"

    def test_twitch_search_for_channel_and_pick_streamer(self):
        """Test to verify that a user can search for a channel and pick a streamer
        """
        twitch_page = TwitchPage(self.driver)
        twitch_page.load()
        twitch_page.scroll_down()
        twitch_page.scroll_top()
        twitch_page.search_for("StarCraft II")
        selected_streamer_href = twitch_page.pick_first_streamer()
        assert selected_streamer_href in self.driver.current_url, "The selected streamer href is not the current url"
