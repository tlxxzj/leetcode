func countSegments(s string) int {
	ff := func(r rune) bool {
		return r == ' '
	}
	return len(strings.FieldsFunc(s, ff))
}