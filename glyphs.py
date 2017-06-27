hiragana_unicode = [12354, 12356, 12358, 12360, 12362, 12363, 12365, 12367, 12369, 12371, 12373, 12375, 12377,
                    12379, 12381, 12383, 12385, 12388, 12390, 12392, 12394, 12395, 12396, 12397, 12398, 12399,
                    12402, 12405, 12408, 12411, 12414, 12415, 12416, 12417, 12418, 12420, 12422, 12424, 12425,
                    12426, 12427, 12428, 12429, 12431, 12434, 12435]
hiragana_chars = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'shi', 'su', 'se', 'so', 'ta', 'chi',
                  'tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me',
                  'mo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo', 'n']

# {'a': '(hiragana a)', ...}
HIRAGANA_SIMPLE = dict(zip(hiragana_chars, map(chr, hiragana_unicode)))

dakuten_mod = {'ka': 'ga', 'ki': 'gi', 'ku': 'gu', 'ke': 'ge', 'ko': 'go',
               'sa': 'za', 'shi': 'ji', 'su': 'zu', 'se': 'ze', 'so': 'zo',
               'ta': 'da', 'chi': 'dzi', 'tsu': 'dzu', 'te': 'de', 'to': 'do',
               'ha': 'ba', 'hi': 'bi', 'fu': 'bu', 'he': 'be', 'ho': 'bo'}
handakuten_mod = {'ha': 'pa', 'hi': 'pi', 'fu': 'pu', 'he': 'pe', 'ho': 'po'}

# {'a': '(hiragana a)', ..., 'ga': '(hiragana ga)', ..., 'pa': '(hiragana pa)', ...}
HIRAGANA = {**HIRAGANA_SIMPLE, **{dakuten_mod[k]: HIRAGANA_SIMPLE[k] + '\u3099' for k in dakuten_mod},
            **{handakuten_mod[k]: HIRAGANA_SIMPLE[k] + '\u309A' for k in handakuten_mod}}

hiragana_small_unicode = [12353, 12355, 12357, 12359, 12361, 12387, 12419, 12421, 12423]
hiragana_small_chars = ['a', 'i', 'u', 'e', 'o', 'tsu', 'ya', 'yu', 'yo']

# {'a': '(small hiragana a)', ...}
HIRAGANA_SMALL = dict(zip(hiragana_small_chars, map(chr, hiragana_small_unicode)))

hiragana_combination_prefix = {'ki': 'ky', 'gi': 'gy', 'shi': 'sh', 'ji': 'jy', 'chi': 'ch', 'dzi': 'dzy', 'ni': 'ny',
                               'hi': 'hy', 'bi': 'by', 'pi': 'py', 'mi': 'my', 'ri': 'ry'}

# {'kya': '(hiragana ki) (small hiragana ya)', ...}
HIRAGANA_COMBINATIONS = {hiragana_combination_prefix[prefix] + suffix: HIRAGANA[prefix] + HIRAGANA_SMALL['y' + suffix] for prefix in hiragana_combination_prefix for suffix in ['a', 'u', 'o']}

"""
katakana_large_unicode = [12450, 12452, 12454, 12456, 12458] \
                         + list(range(12459, 12483)) \
                         + list(range(12484, 12515)) \
                         + [12516, 12518, 12520] \
                         + list(range(12521, 12526)) \
                         + [12527, 12530, 12531]
katakana_large_chars = ['a', 'i', 'u', 'e', 'o', 'ka', 'ga', 'ki', 'gi', 'ku', 'gu', 'ke', 'ge', 'ko', 'go', 'sa', 'za',
                        'shi', 'ji', 'su', 'zu', 'se', 'ze', 'so', 'zo', 'ta', 'da', 'chi', 'ji', 'tsu', 'zu', 'te',
                        'de', 'to', 'do', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'ba', 'pa', 'hi', 'bi', 'pi', 'fu', 'bu',
                        'pu', 'he', 'be', 'pe', 'ho', 'bo', 'po', 'ma', 'mi', 'mu', 'me', 'mo', 'ya', 'yu', 'yo', 'ra',
                        'ri', 'ru', 're', 'ro', 'wa', 'wo', 'n']

KATAKANA_LARGE = dict(zip(katakana_large_chars, map(chr, katakana_large_unicode)))
"""
