package verticaltext

import (
	"strings"
)

func verticalText(s string) [][]string {
	parts := strings.Split(s, " ")
	firstWord := parts[0]
	secondWord := parts[1]
	maxLen := max(len(firstWord), len(secondWord))
	matrix := make([][]string, maxLen)

	for i := range maxLen {
		first, second := " ", " "
		if i < len(firstWord) {
			first = string(firstWord[i])
		}
		if i < len(secondWord) {
			second = string(secondWord[i])
		}
		matrix[i] = []string{first, second}
	}

	return matrix
}
