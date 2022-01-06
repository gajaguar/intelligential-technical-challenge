# Intelligential Technical Challenge

By: [G.A.JAGUAR](https://github.com/gajaguar)

## Exercise 1

Given a bidimentional array `n * m`, develop a function that generates an
unidimentional array `1 * nm` which elements correspond with original array's
elements obtained by following a clockwise snail trajectory.

### Example

Input:

```python
[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ],
]
```

Output:

```python
[ 1, 2, 3, 6, 9, 8, 7, 4, 5 ]
```

### Solution

There is a four basic movements that can be performed by _the snail_: right,
down, left and up (in that order, I mean clockwise). Each lap of this curious
animal will reduce the distance by one.

This movements will be repeated until _the snail_ reaches the last element of
original array.

On each step of our dear friend, it will store the current value into a new
array, at the end it will return this last one.

## Exercise 2

## Exercise 3
