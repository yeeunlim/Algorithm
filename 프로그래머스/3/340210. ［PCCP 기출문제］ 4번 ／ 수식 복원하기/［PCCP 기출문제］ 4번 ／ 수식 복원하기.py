def solution(expressions):
    def max_digit_in_expr(expr):
        m = 0
        for ch in expr:
            if ch.isdigit():
                m = max(m, int(ch))
        return m

    def to_base(num, base):
        if num == 0:
            return "0"

        sign = ""
        if num < 0:
            sign = "-"
            num = -num

        res = []
        while num > 0:
            res.append(str(num % base))
            num //= base

        return sign + "".join(reversed(res))

    def valid_known_expr(expr, base):
        a, op, b, _, c = expr.split()

        # 숫자 안의 모든 자릿수가 base보다 작아야 함
        for s in (a, b, c):
            for ch in s:
                if int(ch) >= base:
                    return False

        x = int(a, base)
        y = int(b, base)
        z = int(c, base)

        if op == "+":
            return x + y == z
        else:
            return x - y == z

    def calc_expr(expr, base):
        a, op, b, _, _ = expr.split()

        x = int(a, base)
        y = int(b, base)

        if op == "+":
            return to_base(x + y, base)
        else:
            return to_base(x - y, base)

    # 모든 숫자에 등장한 최대 digit보다 큰 진법만 가능
    min_base = max(2, max(max_digit_in_expr(expr) for expr in expressions) + 1)

    candidates = []

    for base in range(min_base, 10):
        ok = True

        for expr in expressions:
            if expr.endswith("X"):
                continue

            if not valid_known_expr(expr, base):
                ok = False
                break

        if ok:
            candidates.append(base)

    answer = []

    for expr in expressions:
        if not expr.endswith("X"):
            continue

        results = set()

        for base in candidates:
            results.add(calc_expr(expr, base))

        if len(results) == 1:
            value = results.pop()
        else:
            value = "?"

        answer.append(expr[:-1] + value)

    return answer