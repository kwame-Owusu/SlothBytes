package dailytemperatures

import (
	"reflect"
	"testing"
)

func TestVerticalText(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected []int
	}{
		{
			name:     "valid input and output",
			input:    []int{30, 38, 30, 36, 35, 40, 28},
			expected: []int{1, 4, 1, 2, 1, 0, 0},
		},
		{
			name:     "valid test",
			input:    []int{22, 21, 20},
			expected: []int{0, 0, 0},
		},
		{
			name:     "valid test",
			input:    []int{22, 25, 21, 1, 2, 3},
			expected: []int{1, 0, 0, 1, 1, 0},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := dailyTemps(tt.input)
			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("dailyTemps(%v) = %v, want %v", tt.input, result, tt.expected)
			}
		})
	}
}
