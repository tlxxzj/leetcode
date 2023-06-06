func countDigitOne(n int) int {
	res := 0
	for i := 1; i <= n; i *= 10 {
		m := (n / i) % 10
		if m == 0 {
			res += n / (i * 10) * i
		} else if m == 1 {
			res += n/(i*10)*i + n%i + 1
		} else {
			res += (n/(i*10) + 1) * i
		}
	}
	return res
}
