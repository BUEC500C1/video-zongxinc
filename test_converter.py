import converter

def test_1():
	assert converter.compressVideo(['@iGuessPoems','@UnusualPoems', '@PotatoHugots', '@Poem4your_sprog'], 10) == 0
def test_2():
	assert converter.compressVideo(['@iGuessPoems','@UnusualPoems'], 5) == 0


