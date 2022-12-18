# Math

## Modular Arithmetic
In mathematics, modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" when reaching a certain value, called the modulus. 

Two integers $a$ and $b$ can be congruent modulo $n$, which means that there is an integer $k$ such that $a = kn + b$, which is denoted as:

$$ a \equiv b \pmod{n}$$

This means that $a$ and $b$ fall under the same **equivalence class**, all the following numbers fall under the same equivalence class for modulo 5. 

$$ 17 \equiv 7 \equiv 2 \equiv -3 \equiv -8 \pmod{5} $$

This also works for equations:

$$ 6 \cdot 4 \equiv 4 \pmod{5} $$

$$ 3 / 4 \equiv 2 \pmod{5} $$

$$ 3^3 \equiv 2 \pmod{5} $$

<details>
    <summary>further explanation</summary>

1. Subtraction is the same as addition with the additive inverse

$$ x + (-x) = 0 $$

$$ 3 - 6 = 3 + (-6) \implies 3 + 4 = 7 \equiv 2 \pmod{5} $$

2. Division is the same as multiplying it with the modular multiplicative inverse.

$$ x \cdot x^{-1} \equiv 1 \mod{n}$$

$$ 3 / 4 = 3 \cdot \frac{1}{4} = 3 \cdot 4 \implies 2 \cdot 1 \equiv 2 \pmod{5} $$

</details>


Modular arithmetics has some special properties:

```python
(a+b) % m == (a%m + b%m) % m
(a*b) % m == (a%m * b%m) % m
(x % p) % q == x % q            // if q is a factor of q
```

This means that if you're doing many additions and finally take the modulus at the end, you can do take modulus of the numbers in between and those (smaller) numbers. 

With modular exponentiation, there is another optimization step you can take.

$$ b^{x+y} = b^{x} + b^{y} $$
$$ b^{13} = b^8 + b^4 + b^1 , \quad 13 = 1101_{2} $$

```python
def f(base, exponent, modulus):
    # b ** e % m
    total = 1
    while exponent > 0:
        if exponent % 2 == 1:
            total *= base
            total %= modulus
        exponent //= 2  # floor
        base *= base
        base %= modulus
    return total

# already implemented
pow(base, exponent, modulus)
```

Some things to keep in mind when calculating the modulus in different programming languages:
- in Python, keep the sign of the right side
- in Javascript, keep the sign of left side
- in C++, ...


Sources:
[1](https://www.youtube.com/watch?v=msLZQP-OqrE&t=29s&ab_channel=hyper-neutrino)
[2](https://en.wikipedia.org/wiki/Modular_arithmetic)

Relevant AoC problems:
[2022, day 11](https://adventofcode.com/2022/day/11)


