from abc import ABC, abstractmethod


# class Document(ABC):

#     @abstractmethod
#     def load(self): pass

#     @abstractmethod
#     def view(self): pass

#     @abstractmethod
#     def format(self): pass

#     @abstractmethod
#     def calculate(self): pass


# class PDF(Document):

#     def load(self): pass

#     def view(self): pass


# document1 = PDF()  # TypeError: Can't instantiate abstract class PDF without an implementation for abstract methods


class Document(ABC):

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

    @abstractmethod
    def format(self): pass

    @abstractmethod
    def calculate(self): pass


class DocumentPDF(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass


class DocumentTXT(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass


class DocumentExcel(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass
