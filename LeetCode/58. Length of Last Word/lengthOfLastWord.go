package main

import (
	"fmt"
	"strings"
)

func lengthOfLastWord(s string) int {
	listStr := strings.Fields(s)
	return len(listStr[len(listStr)-1])
}

func main() {
	fmt.Println(lengthOfLastWord("Hello World"))
	fmt.Println(lengthOfLastWord("   fly me   to   the moon  "))
	fmt.Println(lengthOfLastWord("luffy is still joyboy"))
}
