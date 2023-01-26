import requests
from ovos_plugin_manager.templates.stt import STT


class PrivoxSTT(STT):
    LEGACY_URL = "http://api.privox.io/stt"
    URL = "https://secure.privox.io/stt"
    LANGUAGES = {'af': 'afrikaans',
                 'am': 'amharic',
                 'ar': 'arabic',
                 'as': 'assamese',
                 'az': 'azerbaijani',
                 'ba': 'bashkir',
                 'be': 'belarusian',
                 'bg': 'bulgarian',
                 'bn': 'bengali',
                 'bo': 'tibetan',
                 'br': 'breton',
                 'bs': 'bosnian',
                 'ca': 'catalan',
                 'cs': 'czech',
                 'cy': 'welsh',
                 'da': 'danish',
                 'de': 'german',
                 'el': 'greek',
                 'en': 'english',
                 'es': 'spanish',
                 'et': 'estonian',
                 'eu': 'basque',
                 'fa': 'persian',
                 'fi': 'finnish',
                 'fo': 'faroese',
                 'fr': 'french',
                 'gl': 'galician',
                 'gu': 'gujarati',
                 'ha': 'hausa',
                 'haw': 'hawaiian',
                 'he': 'hebrew',
                 'hi': 'hindi',
                 'hr': 'croatian',
                 'ht': 'haitian creole',
                 'hu': 'hungarian',
                 'hy': 'armenian',
                 'id': 'indonesian',
                 'is': 'icelandic',
                 'it': 'italian',
                 'ja': 'japanese',
                 'jw': 'javanese',
                 'ka': 'georgian',
                 'kk': 'kazakh',
                 'km': 'khmer',
                 'kn': 'kannada',
                 'ko': 'korean',
                 'la': 'latin',
                 'lb': 'luxembourgish',
                 'ln': 'lingala',
                 'lo': 'lao',
                 'lt': 'lithuanian',
                 'lv': 'latvian',
                 'mg': 'malagasy',
                 'mi': 'maori',
                 'mk': 'macedonian',
                 'ml': 'malayalam',
                 'mn': 'mongolian',
                 'mr': 'marathi',
                 'ms': 'malay',
                 'mt': 'maltese',
                 'my': 'myanmar',
                 'ne': 'nepali',
                 'nl': 'dutch',
                 'nn': 'nynorsk',
                 'no': 'norwegian',
                 'oc': 'occitan',
                 'pa': 'punjabi',
                 'pl': 'polish',
                 'ps': 'pashto',
                 'pt': 'portuguese',
                 'ro': 'romanian',
                 'ru': 'russian',
                 'sa': 'sanskrit',
                 'sd': 'sindhi',
                 'si': 'sinhala',
                 'sk': 'slovak',
                 'sl': 'slovenian',
                 'sn': 'shona',
                 'so': 'somali',
                 'sq': 'albanian',
                 'sr': 'serbian',
                 'su': 'sundanese',
                 'sv': 'swedish',
                 'sw': 'swahili',
                 'ta': 'tamil',
                 'te': 'telugu',
                 'tg': 'tajik',
                 'th': 'thai',
                 'tk': 'turkmen',
                 'tl': 'tagalog',
                 'tr': 'turkish',
                 'tt': 'tatar',
                 'uk': 'ukrainian',
                 'ur': 'urdu',
                 'uz': 'uzbek',
                 'vi': 'vietnamese',
                 'yi': 'yiddish',
                 'yo': 'yoruba',
                 'zh': 'chinese'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # {fast, normal, better, best, xcribe or xcribe2}
        self.quality = self.config.get("quality", "fast")
        self.key = self.config.get("key")

    def execute(self, audio, language=None):
        lang = language or self.lang
        lang = lang.split("-")[0]
        lang = self.LANGUAGES.get(lang)

        files = {
            'file': audio.get_wav_data(),
            'quality': (None, self.quality),
            'language': (None, lang),
            'key': (None, self.key),
        }
        utt = requests.post(self.LEGACY_URL, files=files).text
        return utt

    def available_languages(self) -> set:
        return set(self.LANGUAGES.keys())


PrivoxSTTConfig = {}
