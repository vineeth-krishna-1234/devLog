import unittest
from unittest.mock import MagicMock
from design_patterns.behavioral.observer import (
    ConcreteSubject,
    ObserverOne,
    ObserverTwo,
)


class TestObserverPattern(unittest.TestCase):
    def setUp(self):
        # Setup for every test case
        self.subject = ConcreteSubject()
        self.observer_one = ObserverOne()
        self.observer_two = ObserverTwo()

        # Mock the update method for observer instances
        self.observer_one.update = MagicMock()
        self.observer_two.update = MagicMock()

    def test_subscribe_observers(self):
        # Subscribe observers to the subject
        self.subject.subscribe(self.observer_one)
        self.subject.subscribe(self.observer_two)

        # Notify observers and check if their update methods were called
        self.subject.notify()
        self.observer_one.update.assert_called_once()
        self.observer_two.update.assert_called_once()

    def test_unsubscribe_observer(self):
        # Subscribe both observers
        self.subject.subscribe(self.observer_one)
        self.subject.subscribe(self.observer_two)

        # Unsubscribe the first observer
        self.subject.unsubscribe(self.observer_one)

        # Notify observers and verify that only the second observer is notified
        self.subject.notify()
        self.observer_one.update.assert_not_called()
        self.observer_two.update.assert_called_once()

    def test_notify_no_observers(self):
        # Notify without any observers subscribed
        # This should not raise any errors or call update on any observers
        self.subject.notify()  # Nothing should happen
        self.observer_one.update.assert_not_called()
        self.observer_two.update.assert_not_called()


if __name__ == "__main__":
    unittest.main()
