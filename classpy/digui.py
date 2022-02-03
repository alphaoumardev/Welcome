def digui(alpha):
    if len(alpha) == 1:
        return alpha
    else:
        return digui(alpha[1:]) + alpha[0]


digui(10)
