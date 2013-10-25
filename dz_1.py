# -*- coding: utf-8-*-

from copy import deepcopy


def p(x1, x2):
    if x1 != x2:
        return 1
    else:
        return 0


def n(x):
    if x == 1:
        return 0
    else:
        return 1


def check_sum(u):
    u[0] = p(p(u[2], u[4]), u[6])
    u[1] = p(p(u[2], u[5]), u[6])
    u[3] = p(p(u[4], u[5]), u[6])


def main():
    #for ee in range(0, 7):
    a = [1, 1, 1, 0]  # исходное число
    ee = 4  # в каком бите допущена ошибка [0, 6]
    b = [0, 0, a[0], 0, a[1], a[2], a[3]]
    check_sum(b)

    d = deepcopy(b)
    d[ee] = n(d[ee])

    m = [0, 0, d[2], 0, d[4], d[5], d[6]]
    check_sum(m)

    res = []
    for i in range(0, 7):
        if d[i] != m[i]:
            res.append(i+1)
    ww = sum(res)-1  # индекс ошибочного бита
    d[ww] = n(d[ww])
    r = [d[2], d[4], d[5], d[6]]  # рез-ат с исправленной ошибкой

    print [p(a[i], r[i]) for i in range(0, 4)]


if __name__ == '__main__':
    main()