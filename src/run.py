# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "textual==3.6.0",
# ]
# ///

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Digits


class GitDashApp(App):
    """A simple Git dashboard application."""
    def compose(self) -> ComposeResult:
        """Compose the screen layout."""
        yield Button("Issues", id="issues-button", variant="primary")
        yield Button("Pull Requests", id="pull-requests-button", variant="primary")
        yield Button("Exit", id="exit-button", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        match event.button.id:
            case "exit-button":
                self.exit()
            case "issues-button":
                self.push_screen(IssuesScreen())
            case "pull-requests-button":
                self.push_screen(PullRequestsScreen())

class IssuesScreen(Screen):
    """Screen to display issues."""
    def compose(self) -> ComposeResult:
        """Compose the screen layout."""
        yield Digits("Issues", id="issue-count")
        yield Button("Back", id="back-button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        match event.button.id:
            case "back-button":
                self.app.pop_screen()

class PullRequestsScreen(Screen):
    """Screen to display pull requests."""
    def compose(self) -> ComposeResult:
        """Compose the screen layout."""
        yield Digits("Pull Requests", id="pr-count")
        yield Button("Back", id="back-button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        match event.button.id:
            case "back-button":
                self.app.pop_screen()


if __name__ == "__main__":
    app = GitDashApp()
    app.run()
