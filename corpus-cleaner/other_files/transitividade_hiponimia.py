A = 1
B = 2
C = 3


def check_transitivity(A, B, C):
    if A < B and B < C:
        return True
    else:
        return False


def show_hipothesis(check_transitivity):
    if check_transitivity:
        return f"Transitividade dos hipônimos assegurada!"
    else:
        return f"Transitividade dos hipônimos não assegurada!"


if __name__ == "__main__":
    print(show_hipothesis(check_transitivity(A, B, C)))
