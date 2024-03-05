from abc import ABC, abstractmethod


# observer
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

        
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


# strategy
class FormattingStrategy(ABC):
    @abstractmethod
    def format(self, text):
        return f"<b>{text}</b>"


# command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class InsertTextCommand(Command):
    def __init__(self, text):
        self.text = text

    def execute(self):
        return self.text


# state
class State(ABC):
    @abstractmethod
    def handle(self, editor):
        # print("Normal mode")
        pass


class NormalState(State):
    def handle(self, editor):
        print("Normal mode")


class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class TextElement(Element):
    def accept(self, visitor):
        return visitor.visit(self)


class Visitor(ABC):
    @abstractmethod
    def visit(self, element):
        pass


# mediator
class EditorMediator:
    def notify(self, sender, event):
        pass

class Memento:
    def __init__(self, state):
        self.state = state


class Originator:
    def __init__(self):
        self._state = None

    def save(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.state


# edtior example
class TextEditor(Subject):
    def __init__(self):
        super().__init__()
        self.state = NormalState()
        self.text = ""


    def insert_text(self, text):
        self.text = text
        self.notify()


    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state


    def get_text(self):
        return self.text


# client code
# editor = TextEditor()
# editor.attach(Observer())

# # strategy pattern
# strategy = BoldStrategy()
# formatted_text = strategy.format("Hello world")
# print(formatted_text)

# # command pattern
# command = InsertTextCommand("Hello world")
# editor.insert_text(command.execute())

# # state pattern
# editor.set_state(NormalState())
