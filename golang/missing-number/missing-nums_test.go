package missingnumber

import "testing"

func TestIsValidHexCode(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected int
	}{
		{
			name:     "num 5 missing",
			input:    []int{1, 2, 3, 4, 6, 7, 8, 9, 10},
			expected: 5,
		},
		{
			name:     "num 10 missing",
			input:    []int{10, 5, 1, 2, 4, 6, 8, 3, 9},
			expected: 7,
		},
		{
			name:     "nothing missing",
			input:    []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
			expected: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := missingNum(tt.input)
			if result != tt.expected {
				t.Errorf("missingNum(%q) = %v, want %v", tt.input, result, tt.expected)
			}
		})
	}
}
