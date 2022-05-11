### Bitwise operatiors and it's usage

Machine understands only bits and we interact with machines in a decimal system. Bitwise operator manipulates number and logics at bit level which is faster than interacting with decimal systems

#### Types of bitwise operator

- **AND(&)**: it takes two numbers as operands and performs AND operations on every bit of two numbers. For example, let's take two number a = 6, b = 5 and their binary value is a = 110 and b = 101. AND operation on a, b would result in 4. How?

<table style="display: flex; justify-content: center;">
  <tbody>
      <tr>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>= a(6)</td>
      </tr>
       <tr>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>= b(5)</td>
      </tr>
       <tr>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>= 4</td>
      </tr>
  </tbody>
<table>

Since last bit of odd number is always 1 and even number is 0, we can find out if a number is whether even or odd by doing AND operation with the number and 1

- **OR(|)**: takes two number and perform OR operatiion. If two numbers has at least on commont bit, it returns 1

- **XOR(^)**: performs XOR operation on two numbers. Returns 1 if any of two bit is different. XOR with same number returns 0.

- **LEFT SHIFT(<<)**: First number bits are shifted left

- **RIGHT SHIFT(>>)** Opposite of LEFT SHIFT

- **BITWISE NOT(~)** Inverse all bits of a number
