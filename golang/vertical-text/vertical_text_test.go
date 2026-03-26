package verticaltext

import (
	"reflect"
	"testing"
)

func TestVerticalText(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected [][]string
	}{
		{
			name:  "valid matrix",
			input: "Hello World",
			expected: [][]string{
				{"H", "W"},
				{"e", "o"},
				{"l", "r"},
				{"l", "l"},
				{"o", "d"},
			},
		},
		{
			name:  "valid matrix, should allow exmpty string",
			input: "Hello Fellas",
			expected: [][]string{
				{"H", "F"},
				{"e", "e"},
				{"l", "l"},
				{"l", "l"},
				{"o", "a"},
				{" ", "s"},
			},
		},
		{
			name:  "first word longer",
			input: "Hello Hi",
			expected: [][]string{
				{"H", "H"},
				{"e", "i"},
				{"l", " "},
				{"l", " "},
				{"o", " "},
			},
		},
		{
			name:  "equal length words",
			input: "Cat Dog",
			expected: [][]string{
				{"C", "D"},
				{"a", "o"},
				{"t", "g"},
			},
		},
		{
			name:  "single char words",
			input: "A B",
			expected: [][]string{
				{"A", "B"},
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := verticalText(tt.input)
			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("vertical Text(%v) = %v, want %v", tt.input, result, tt.expected)
			}
		})
	}
}
