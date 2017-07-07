
import glyphs as glyphs
import random

GLYPH_SET = glyphs.HIRAGANA

while True:
    romaji, kana = random.choice(list(GLYPH_SET.items()))
    answer = input(romaji + ' ? ')
    print(kana)