from abc import ABC, abstractmethod


class Bank(ABC):
    @abstractmethod
    def balance_check(self):
        pass

    @abstractmethod
    def interest(self):
        pass


class SBI(Bank):
    def balance_check(self):
        print("Balance is 100 rupees")

    def interest(self):
        print("SBI interest is 5 rupees")


if __name__ == '__main__':
    s = SBI()
    s.balance_check()
    s.interest()
