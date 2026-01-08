package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(removeEdgeVowels("solving remove edge vowels"))
	fmt.Println(removeEdgeVowels("hello world, i love programming"))
	fmt.Println(removeEdgeVowels("hi, how are you doing"))
}

func removeEdgeVowels(s string) string {
	vowels := "aeiouAEIOU"
	words := strings.Split(s, " ")

	for i, word := range words {
		runes := []rune(word)

		firstVowel := -1
		lastVowel := -1

		// find first and last vowel positions
		for j, r := range runes {
			if strings.ContainsRune(vowels, r) {
				if firstVowel == -1 {
					firstVowel = j
				}
				lastVowel = j
			}
		}

		// no vowels, leave word unchanged
		if firstVowel == -1 {
			continue
		}

		// build new word
		var builder []rune
		for j, r := range runes {
			if j != firstVowel && j != lastVowel {
				builder = append(builder, r)
			}
		}

		words[i] = string(builder)
	}

	return strings.Join(words, " ")
}
