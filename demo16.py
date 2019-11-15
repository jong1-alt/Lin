from decimal import Decimal

a1 = Decimal(1.5)
print(a1)
a2 = Decimal(1.4)
print(a2)
a3 = Decimal(2.968)
print(a3)
a4 = Decimal('2.968')
print(a4)
a5 = Decimal(2968) * Decimal(0.001) - Decimal(2.968)
print(a5)
a6 = Decimal(2968) * Decimal('0.001') - Decimal('2.968')
print(a6)
from decimal import ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN

digits = [1.5, 2.5, 3.5, 4.5]
rounds = [ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP]
for d in digits:
    for r in rounds:
        result = Decimal(Decimal(d).quantize(Decimal(1),
                                             rounding=r))
        print(f"{d} using {r} ==> {result}")
