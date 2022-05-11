package main

import "fmt"

func main() {

	a, b := 5, 6;

	fmt.Println("Bitwise  AND of a and b:", a & b);
	fmt.Println("Bitwise  OR of a and b:", a | b);
	fmt.Println("Bitwise  XOR of a and b:", a ^ b);
	fmt.Println("Bitwise  LEFT SHIFT of a and b:", a << b);
	fmt.Println("Bitwise  RIGHT SHIFT of a and b:", a >> b);

}