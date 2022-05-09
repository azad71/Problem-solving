package main

import (
	"fmt"
	"strings"
)

func maximumWordInSentence(sentences []string) int {
	count := 0;

	for _, sentence := range sentences {
		wordCount :=  len(strings.Split(sentence, " "))

		if wordCount > count {
			count = wordCount;
		}
	}

	return count;
}

func main() {
	sentences := []string {"alice and bob love leetcode", "i think so too", "this is great thanks very much"}

	fmt.Println(maximumWordInSentence((sentences)))
}