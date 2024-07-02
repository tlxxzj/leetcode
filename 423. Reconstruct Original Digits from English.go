func originalDigits(s string) string {
	m := make(map[rune]int)
	for _, c := range s {
		m[c]++
	}

	digits := []rune{}

	// zero
	if m['z'] > 0 {
		count := m['z']
		for i := 0; i < count; i++ {
			digits = append(digits, '0')
		}
		m['z'] -= count
		m['e'] -= count
		m['r'] -= count
		m['o'] -= count
	}

	// two
	if m['w'] > 0 {
		count := m['w']
		for i := 0; i < count; i++ {
			digits = append(digits, '2')
		}
		m['t'] -= count
		m['w'] -= count
		m['o'] -= count
	}

	// four
	if m['u'] > 0 {
		count := m['u']
		for i := 0; i < count; i++ {
			digits = append(digits, '4')
		}
		m['f'] -= count
		m['o'] -= count
		m['u'] -= count
		m['r'] -= count
	}

	// six
	if m['x'] > 0 {
		count := m['x']
		for i := 0; i < count; i++ {
			digits = append(digits, '6')
		}
		m['s'] -= count
		m['i'] -= count
		m['x'] -= count
	}

	// eight
	if m['g'] > 0 {
		count := m['g']
		for i := 0; i < count; i++ {
			digits = append(digits, '8')
		}
		m['e'] -= count
		m['i'] -= count
		m['g'] -= count
		m['h'] -= count
		m['t'] -= count
	}

	// one
	if m['o'] > 0 {
		count := m['o']
		for i := 0; i < count; i++ {
			digits = append(digits, '1')
		}
		m['o'] -= count
		m['n'] -= count
		m['e'] -= count
	}

	// three
	if m['t'] > 0 {
		count := m['t']
		for i := 0; i < count; i++ {
			digits = append(digits, '3')
		}
		m['t'] -= count
		m['h'] -= count
		m['r'] -= count
		m['e'] -= count * 2
	}

	// five
	if m['f'] > 0 {
		count := m['f']
		for i := 0; i < count; i++ {
			digits = append(digits, '5')
		}
		m['f'] -= count
		m['i'] -= count
		m['v'] -= count
		m['e'] -= count
	}

	// seven
	if m['s'] > 0 {
		count := m['s']
		for i := 0; i < count; i++ {
			digits = append(digits, '7')
		}
		m['s'] -= count
		m['e'] -= count * 2
		m['v'] -= count
		m['n'] -= count
	}

	// nine
	if m['i'] > 0 {
		count := m['i']
		for i := 0; i < count; i++ {
			digits = append(digits, '9')
		}
		m['n'] -= count * 2
		m['i'] -= count
		m['e'] -= count
	}

	slices.Sort(digits)
	return string(digits)
}
