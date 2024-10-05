from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass


class Subject(ABC):
    def __init__(self) -> None:
        self._observers = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    def __init__(self) -> None:
        super().__init__()

    def notify(self) -> None:
        for observer in self._observers:
            observer.update()


class ObserverOne(Observer):
    def __init__(self) -> None:
        super().__init__()

    def update(self) -> None:
        print("Received update [OBSERVER 1]")


class ObserverTwo(Observer):
    def __init__(self) -> None:
        super().__init__()

    def update(self) -> None:
        print("Received update [OBSERVER 2]")


if __name__ == "__main__":

    subject = ConcreteSubject()
    observer_one = ObserverOne()
    observer_two = ObserverTwo()

    subject.subscribe(observer=observer_one)
    subject.subscribe(observer=observer_two)
    subject.notify()
    subject.unsubscribe(observer=observer_one)
    subject.notify()
