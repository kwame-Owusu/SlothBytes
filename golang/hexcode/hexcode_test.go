package hexcode

import "testing"

func TestIsValidHexCode(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected bool
	}{
		{
			name:     "Valid hex code uppercase",
			input:    "#CD5C5C",
			expected: true,
		},
		{
			name:     "Valid hex code uppercase mixed",
			input:    "#EAECEE",
			expected: true,
		},
		{
			name:     "Valid hex code lowercase",
			input:    "#eaecee",
			expected: true,
		},
		{
			name:     "Invalid - length exceeds 6",
			input:    "#CD5C58C",
			expected: false,
		},
		{
			name:     "Invalid - contains Z (not A-F)",
			input:    "#CD5C5Z",
			expected: false,
		},
		{
			name:     "Invalid - contains unacceptable character &",
			input:    "#CD5C&C",
			expected: false,
		},
		{
			name:     "Invalid - missing # symbol",
			input:    "CD5C5C",
			expected: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := isValidHexCode(tt.input)
			if result != tt.expected {
				t.Errorf("isValidHexCode(%q) = %v, want %v", tt.input, result, tt.expected)
			}
		})
	}
}
