package main

import "fmt"

func findValue(operations []string) int {
	x := 0;

	for _, op := range operations {
		
		if op == "++X" || op == "X++" {
			x += 1;
		} else if op == "--X" || op == "X--" {
			x -= 1;
		}
	} 

	return x;
}

func main() {
	operations := []string {"++X", "++X", "--X", "X++", "X++"};

	value := findValue(operations);

	fmt.Println(value)
}