package sevenboom

import (
	"strconv"
	"strings"
)

func sevenBoom(arr []int) string {
	var b strings.Builder

	for _, n := range arr {
		if strings.Contains(strconv.Itoa(n), "7") {
			b.WriteString("Boom! ")
		}
	}

	if b.Len() == 0 {
		return "there is no 7 in the array"
	}

	return strings.TrimSpace(b.String())
}
