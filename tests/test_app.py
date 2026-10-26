# Copyright (c) 2026 Jack Plowman

import unittest

from src.run import GitDashApp, IssuesScreen, PullRequestsScreen


class NavigationTests(unittest.IsolatedAsyncioTestCase):
    """Verify navigation stays compatible with upgraded Textual releases."""

    async def test_navigation_and_exit(self) -> None:
        """Open both screens, return home, and exit through the UI."""
        app = GitDashApp()
        async with app.run_test() as pilot:
            home = app.screen
            await pilot.click("#issues-button")
            self.assertIsInstance(app.screen, IssuesScreen)
            await pilot.click("#back-button")
            self.assertIs(app.screen, home)
            await pilot.click("#pull-requests-button")
            self.assertIsInstance(app.screen, PullRequestsScreen)
            await pilot.click("#back-button")
            self.assertIs(app.screen, home)
            await pilot.click("#exit-button")
        self.assertFalse(app.is_running)
