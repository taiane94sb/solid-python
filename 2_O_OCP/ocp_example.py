# class Company:
#     def do_work(self, worker: int) -> None:
#         if worker == 1:
#             print("Programmer creating code")
#         if worker == 2:
#             print("Seller selling the product")
#         if worker == 3:
#             print("HR hiring new devs")
#         else:
#             print('Error, no Worker!')


class Programer:
    def make(self):
        print("Programmer creating code")


class Seller:
    def make(self):
        print("Seller selling the product")


class RH:
    def make(self):
        print("HR hiring new devs")


class Company:
    def do_work(self, worker: any) -> None:
        worker.make()


programmer = Programer()
seller = Seller()
rh = RH()

company = Company()
company.do_work(programmer)  # Programmer creating code
company.do_work(seller)  # Seller selling the product
company.do_work(rh)  # HR hiring new devs
