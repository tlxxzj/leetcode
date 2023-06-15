func fullJustify(words []string, maxWidth int) []string {
	res := []string{}

	i, j := 0, 0
	for i = 0; i < len(words); i = j {
		width := 0
		for j = i; j < len(words) && width+len(words[j]) <= maxWidth; j++ {
			width += len(words[j]) + 1
		}
		n := j - i
		line := ""
		if n == 1 {
			line = words[i] + strings.Repeat(" ", maxWidth-len(words[i]))
		} else if j < len(words) {
			spaces := maxWidth - width + n
			space := spaces / (n - 1)
			extra := spaces % (n - 1)
			for k := i; k < j; k++ {
				line += words[k]
				if k < j-1 {
					line += strings.Repeat(" ", space)
					if k-i < extra {
						line += " "
					}
				}
			}
		} else {
			for k := i; k < j; k++ {
				line += words[k]
				if k < j-1 {
					line += " "
				}
			}
			line += strings.Repeat(" ", maxWidth-len(line))
		}
		res = append(res, line)
	}
	return res
}
