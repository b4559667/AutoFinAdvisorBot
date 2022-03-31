from math import pow


class Calculations:

    def __init__(self, Y, t1, t2, t3, r, h):
        self.__Y = float(Y)
        self.__t1 = float(t1)
        self.__t2 = float(t2)
        self.__t3 = float(t3)
        self.__r = float(r / 100)
        self.__h = float(h / 100)
        self.__i = 0.063
        self.__rr = round(((1 + self.__r) / (1 + self.__i)) - 1, 3)

    def __future_annuity_value(self):
        N1 = self.__t2 - self.__t1
        FVA = round((pow((1 + self.__rr), N1) - 1) / self.__rr, 3)
        return FVA

    def __current_annuity_value(self):
        N2 = self.__t3 - self.__t2
        PVA = round((1 - pow((1 + self.__rr), -N2)) / self.__rr, 3)
        return PVA

    def calc_result(self):
        resultFVA = Calculations.__future_annuity_value(self)
        resultPVA = Calculations.__current_annuity_value(self)
        step1 = resultPVA * self.__Y
        step2 = resultFVA + resultPVA
        C = round(step1 / step2)
        S = round(self.__Y - C)
        return (C, S)
