import requests
from objects import Kanji
from typing import List

URL = 'https://jotoba.de/api'

def search_kanji(kanji: str) -> List[Kanji]:
	"""Search for Kanji by character."""
	k = requests.post(url=f'{URL}/search/kanji',
				   json={
					   'query': kanji,
					   'language': 'English',
					   'no_english': False
				   })
	if k.status_code == 200:
		kanjis = []
		for kanji in k.json()['kanji']:
			kanjis.append(Kanji(data=kanji))
		return kanjis