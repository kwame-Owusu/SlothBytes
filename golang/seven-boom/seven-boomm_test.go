package sevenboom

import "testing"

func TestSevenBoom(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected string
	}{
		{
			name:     "contains single 7",
			input:    []int{1, 2, 3, 7, 8},
			expected: "Boom!",
		},
		{
			name:     "contains 7 inside number",
			input:    []int{10, 27, 35},
			expected: "Boom!",
		},
		{
			name:     "multiple 7 occurrences",
			input:    []int{7, 17, 70},
			expected: "Boom! Boom! Boom!",
		},
		{
			name:     "no 7 present",
			input:    []int{1, 2, 3, 4, 5},
			expected: "there is no 7 in the array",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := sevenBoom(tt.input)
			if result != tt.expected {
				t.Errorf("sevenBoom(%v) = %v, want %v", tt.input, result, tt.expected)
			}
		})
	}
}
