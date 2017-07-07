hiragana_unicode = [12354, 12356, 12358, 12360, 12362, 12363, 12365, 12367, 12369, 12371, 12373, 12375, 12377,
                    12379, 12381, 12383, 12385, 12388, 12390, 12392, 12394, 12395, 12396, 12397, 12398, 12399,
                    12402, 12405, 12408, 12411, 12414, 12415, 12416, 12417, 12418, 12420, 12422, 12424, 12425,
                    12426, 12427, 12428, 12429, 12431, 12434, 12435]
hiragana_chars = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'shi', 'su', 'se', 'so', 'ta', 'chi',
                  'tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me',
                  'mo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo', 'n']

hiragana_small_unicode = [12353, 12355, 12357, 12359, 12361, 12387, 12419, 12421, 12423]
hiragana_small_chars = ['a', 'i', 'u', 'e', 'o', 'tsu', 'ya', 'yu', 'yo']

katakana_unicode = [12450, 12452, 12454, 12456, 12458, 12459, 12461, 12463, 12465, 12467, 12469, 12471, 12473, 12475,
                    12477, 12479, 12481, 12484, 12486, 12488, 12490, 12491, 12492, 12493, 12494, 12495, 12498, 12501,
                    12504, 12507, 12510, 12511, 12512, 12513, 12514, 12516, 12518, 12520, 12521, 12522, 12523, 12524,
                    12525, 12527, 12530, 12531]
katakana_chars = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'shi', 'su', 'se', 'so', 'ta', 'chi',
                  'tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me',
                  'mo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo', 'n']

katakana_small_unicode = [12449, 12451, 12453, 12455, 12457, 12483, 12515, 12517, 12519]
katakana_small_chars = ['a', 'i', 'u', 'e', 'o', 'tsu', 'ya', 'yu', 'yo']

dakuten_mod = {'ka': 'ga', 'ki': 'gi', 'ku': 'gu', 'ke': 'ge', 'ko': 'go',
               'sa': 'za', 'shi': 'ji', 'su': 'zu', 'se': 'ze', 'so': 'zo',
               'ta': 'da', 'chi': 'dzi', 'tsu': 'dzu', 'te': 'de', 'to': 'do',
               'ha': 'ba', 'hi': 'bi', 'fu': 'bu', 'he': 'be', 'ho': 'bo'}
handakuten_mod = {'ha': 'pa', 'hi': 'pi', 'fu': 'pu', 'he': 'pe', 'ho': 'po'}
dakuten_unicode = '\u3099'
handakuten_unicode = '\u309A'

# {'a': '(kana a)', ...}
HIRAGANA_SIMPLE = dict(zip(hiragana_chars, map(chr, hiragana_unicode)))
KATAKANA_SIMPLE = dict(zip(katakana_chars, map(chr, katakana_unicode)))

# {'a': '(kana a)', ..., 'ga': '(kana ga)', ..., 'pa': '(kana pa)', ...}
HIRAGANA = {**HIRAGANA_SIMPLE, **{dakuten_mod[k]: HIRAGANA_SIMPLE[k] + dakuten_unicode for k in dakuten_mod},
            **{handakuten_mod[k]: HIRAGANA_SIMPLE[k] + handakuten_unicode for k in handakuten_mod}}
KATAKANA = {**KATAKANA_SIMPLE, **{dakuten_mod[k]: KATAKANA_SIMPLE[k] + dakuten_unicode for k in dakuten_mod},
            **{handakuten_mod[k]: KATAKANA_SIMPLE[k] + handakuten_unicode for k in handakuten_mod}}

# {'a': '(small kana a)', ...}
HIRAGANA_SMALL = dict(zip(hiragana_small_chars, map(chr, hiragana_small_unicode)))
KATAKANA_SMALL = dict(zip(katakana_small_chars, map(chr, katakana_small_unicode)))


simple_combination_prefix = {'ki': 'ky', 'gi': 'gy', 'shi': 'sh', 'ji': 'jy', 'chi': 'ch', 'dzi': 'dzy', 'ni': 'ny',
                             'hi': 'hy', 'bi': 'by', 'pi': 'py', 'mi': 'my', 'ri': 'ry'}
katakana_only_combinations = {'va': KATAKANA['u'] + dakuten_unicode + KATAKANA_SMALL['a'],
                              'vi': KATAKANA['u'] + dakuten_unicode + KATAKANA_SMALL['i'],
                              'vu': KATAKANA['u'] + dakuten_unicode,
                              've': KATAKANA['u'] + dakuten_unicode + KATAKANA_SMALL['e'],
                              'vo': KATAKANA['u'] + dakuten_unicode + KATAKANA_SMALL['o'],
                              'wi': KATAKANA['u'] + KATAKANA_SMALL['i'],
                              'we': KATAKANA['u'] + KATAKANA_SMALL['e'],
                              'wo': KATAKANA['u'] + KATAKANA_SMALL['o'],
                              'fa': KATAKANA['fu'] + KATAKANA_SMALL['a'],
                              'fi': KATAKANA['fu'] + KATAKANA_SMALL['i'],
                              'fe': KATAKANA['fu'] + KATAKANA_SMALL['e'],
                              'fo': KATAKANA['fu'] + KATAKANA_SMALL['o'],
                              'she': KATAKANA['shi'] + KATAKANA_SMALL['e'],
                              'je': KATAKANA['shi'] + dakuten_unicode + KATAKANA_SMALL['e'],
                              'che': KATAKANA['chi'] + KATAKANA_SMALL['e'],
                              'tu': KATAKANA['to'] + KATAKANA_SMALL['u'],
                              'ty': KATAKANA['te'] + KATAKANA_SMALL['i'],
                              'du': KATAKANA['to'] + dakuten_unicode + KATAKANA_SMALL['u'],
                              'dy': KATAKANA['te'] + dakuten_unicode + KATAKANA_SMALL['i']}

# {'kya': '(kana ki) (small kana ya)', ...}
HIRAGANA_COMBINATIONS = {simple_combination_prefix[prefix] + suffix: HIRAGANA[prefix] + HIRAGANA_SMALL['y' + suffix]
                         for prefix in simple_combination_prefix for suffix in ['a', 'u', 'o']}
KATAKANA_COMBINATIONS = {**{simple_combination_prefix[prefix] + suffix: KATAKANA[prefix] + KATAKANA_SMALL['y' + suffix]
                            for prefix in simple_combination_prefix for suffix in ['a', 'u', 'o']},
                         **katakana_only_combinations}

# {'a': '(kana a)', ...}
HIRAGANA_COMPLETE = {**HIRAGANA, **HIRAGANA_COMBINATIONS}
KATAKANA_COMPLETE = {**KATAKANA, **KATAKANA_COMBINATIONS}