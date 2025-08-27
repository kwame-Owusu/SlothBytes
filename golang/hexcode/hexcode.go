package hexcode

import (
	"strings"
)

func isValidHexCode(code string) bool {
	if len(code) != 7 || !strings.HasPrefix(code, "#") {
		return false
	}

	for _, char := range strings.ToLower(code[1:]) {
		if !((char >= '0' && char <= '9') || (char >= 'a' && char <= 'f')) {
			return false
		}
	}
	return true
}
