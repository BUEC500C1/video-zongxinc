import converter

def test_1():
	assert converter.Video_compress(['@iGuessPoems','@UnusualPoems', '@PotatoHugots', '@Poem4your_sprog'], 10) == 0
def test_2():
	assert converter.Video_compress(['@iGuessPoems','@UnusualPoems'], 5) == 0


