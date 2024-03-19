
class Kanji:
	def __init__(self, data):
		self.character = data['literal']
		self.meanings = data['meanings']
		self.grade = data['grade']
		self.stroke_count = data['stroke_count']
		self.frequency = data['frequency']
		self.jlpt = data['jlpt']
		self.onyomi = data['onyomi']
		self.kunyomi = data['kunyomi']
		self.parts = data['parts']
		self.radical =	data['radical']
	
	def __dict__(self):
		data = {
			'character': self.character,
			'meanings': self.meanings,
			'grade': self.grade,
			'stroke_count': self.stroke_count,
			'frequency': self.frequency,
			'jlpt': self.jlpt,
			'onyomi': self.onyomi,
			'kunyomi': self.kunyomi,
			'parts': self.parts,
			'radical': self.radical
		}
		return data
	def __repr__(self) -> str:
		return f'Kanji({self.character})'