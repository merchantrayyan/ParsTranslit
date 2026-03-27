import os
import re
import ctranslate2
from typing import List



# Persian → Latin digits
fa_digits = {
    "۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4",
    "۵": "5", "۶": "6", "۷": "7", "۸": "8", "۹": "9",
    "٠": "0",
    "١": "1",
    "٢": "2",
    "٣": "3",
    "٤": "4",
    "٥": "5",
    "٦": "6",
    "٧": "7",
    "٨": "8",
    "٩": "9",
}

fa_to_lat_digits = {
    "۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4",
    "۵": "5", "۶": "6", "۷": "7", "۸": "8", "۹": "9",
}
lat_digits = {v: k for k, v in fa_to_lat_digits.items()}

fa_punc_to_lat = {
    "،": ",",      
    "؛": ";",     
    "؟": "?",      
    "«": "“",      
    "»": "”",      
    "ـ": "_",      
    "!": "!",      
    "\u06D4": ".", 
}

lat_punc_to_fa = {
    ",": "،",
    ";": "؛",
    "?": "؟",
    "!": "!",
    "“": "«",
    "”": "»",
    '"': '"',  
    "«": "«",
    "(": "(",
    ".": ".",
    ")": ")",
    ":": ":"
}
def convert_straight_quotes_to_arabic(text):
    """Convert straight quotes (") to Arabic quotation marks (« and ») based on position.
    First quote in a pair becomes « (left/opening), second becomes » (right/closing).
    """
    result = []
    quote_count = 0
    
    for char in text:
        if char == '"':
            # Alternate between opening and closing quotes
            if quote_count % 2 == 0:
                result.append(' «')  # Opening quote
            else:
                result.append('» ')  # Closing quote
            quote_count += 1
        else:
            result.append(char)
    
    return ''.join(result)

def normalize_text(s: str, preserve_structure: bool = True) -> str:
    if preserve_structure:
        # Only normalize excessive whitespace (3+ spaces -> 2 spaces)
        s = re.sub(r'[ \t]{3,}', '  ', s) 
        return s
    else:
        # Original behavior
        s = s.strip()
        s = re.sub(r"\s+", " ", s)
        return s

def prepare_input(text: str, direction: str) -> List[List[str]]:
    #model expects text tokenized by character in specific way
    # hello => 
    text = normalize_text(text, preserve_structure=False)
    words = text.split()
    chars = list(('_'.join([f"@{''.join(list(word))}$" for word in words])))
    #print(chars)
    return [chars]

def transliterate(text: str,direction: str):
    if direction == "tgfa":
        translator = ctranslate2.Translator("ct2_tgfa")
    elif direction == "fatg":
        translator = ctranslate2.Translator("ct2_fatg")
    
    segments = re.split(r'(\d+|[\u06F0-\u06F9]+|[^\w\s\u200c\u064B-\u065F\u08F0-\u08FF]|\n+)', text)

    translated_segments = []
    for seg in segments:
        #print(seg)
        if seg and seg.strip() == '' and '\n' in seg:
            translated_segments.append(seg)  
            continue
        
        if re.fullmatch(r'\d+|[\u06F0-\u06F90-9]+', seg):
            numbers = ""
            seg_lower = seg.lower()
            if direction == "tgfa":
                # Convert Latin digits to Persian digits 
                for x in seg_lower:
                    if x in fa_digits:
                        numbers += (fa_digits[x])
                    elif x in lat_digits:
                        numbers += (lat_digits[x])
                    elif x in fa_punc_to_lat:
                        numbers += (fa_punc_to_lat[x])
            else:  
                # Convert Persian digits to Latin digits 
                for x in seg_lower:
                    if x in fa_digits:
                        numbers += fa_digits[x]  
                    elif x in lat_digits:
                        numbers += x  # 
                    else:
                        numbers += x  #
            translated_segments.append(numbers)
            continue

        if not seg.strip():
            translated_segments.append(seg)  
            continue

        if re.fullmatch(r'[^\w\s]+', seg):
            seg_lower = seg.lower()
            # Handle punctuation conversion using dictionaries
            if direction == "fatg":
                
                if seg_lower in fa_punc_to_lat:
                    translated_segments.append(fa_punc_to_lat[seg_lower])
                elif seg_lower in lat_punc_to_fa:
                    translated_segments.append(seg)
                else:
                    translated_segments.append(seg)
            else:  # tgfa
                if seg_lower in lat_punc_to_fa:
                    translated_segments.append(lat_punc_to_fa[seg_lower])
                elif seg_lower in fa_punc_to_lat:
                    translated_segments.append(seg)
                else:
                    translated_segments.append(seg)
            continue

        
        seg_stripped = seg.strip()
        if not seg_stripped:
            translated_segments.append(seg)
            continue
        
        # Patterns for detecting foreign content to preserve
        email_pattern = r'\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b'
        url_pattern = r'https?://[^\s]+|www\.[a-z0-9.-]+\.[a-z]{2,}(?:/[^\s]*)?'
        ascii_word_pattern = r'\b[a-z][a-z0-9_\-]*[a-z0-9]\b|\b[a-z]\b'
        
        
        seg_lower = seg_stripped.lower()
        contains_foreign = bool(
            re.search(email_pattern, seg_lower, re.IGNORECASE) or
            re.search(url_pattern, seg_lower, re.IGNORECASE) or
            re.search(ascii_word_pattern, seg_lower, re.IGNORECASE)
        )
        
        if contains_foreign:
            
            translated_segments.append(seg_stripped)
        else:
            
            inputs = prepare_input(seg_lower, direction)
            #print(inputs)
            results = translator.translate_batch(
                inputs,
                beam_size=5,
                max_batch_size=128,
            )
                #print(results)
            hypotheses = results[0]
            tokens_dict = hypotheses[0].split() if isinstance(hypotheses[0], str) else hypotheses[0]
            out_tokens = tokens_dict['tokens']
            # Detokenize
            
            output_text = "".join(out_tokens).strip()
            #print(output_text)
            output_text = (
                output_text.replace('@', '')
                        .replace('$', '')
                        .replace('_', ' ')
            )
            translated_segments.append(output_text)
    #print(translated_segments)
    #print(final_output)
    final_output = "".join(translated_segments)
    
    # Space before number (if not at start and not after punctuation/whitespace)
    final_output = re.sub(r'([^\s\d\u06F0-\u06F9])(\d|[\u06F0-\u06F9])', r'\1 \2', final_output)
    # Space after number (if not at end and not before punctuation/whitespace)
    final_output = re.sub(r'(\d|[\u06F0-\u06F9])([^\s\d\u06F0-\u06F9\-])', r'\1 \2', final_output)
    
    if direction == "fatg":
        for fa_punc, lat_punc in fa_punc_to_lat.items():
            final_output = final_output.replace(fa_punc, lat_punc)
        
        final_output = re.sub(r'\s+([,;:\.\?\!])', r'\1', final_output)
        final_output = re.sub(r'([,;:\.\?\!\)])(?!\s)', r'\1 ', final_output)
        final_output = re.sub(r'([\)\]\}”])(?![\s\-])(?!$)', r'\1 ', final_output)
        final_output = re.sub(r'(?<!\s)([\(\“])', r' \1', final_output)
        print(final_output)
    else:
        for lat_punc, fa_punc in lat_punc_to_fa.items():
            if lat_punc:  # Skip empty strings
                final_output = final_output.replace(lat_punc, fa_punc)
        # Convert straight quotes to Arabic quotation marks based on position
        final_output = convert_straight_quotes_to_arabic(final_output)
        # Arabic punctuation spacing normalization (equivalent to lines 362-365)
        final_output = re.sub(r'\s+([،؛:\.\؟\!\u06D4])', r'\1', final_output)  # Remove spaces before Arabic punctuation
        final_output = re.sub(r'([،؛:\.\؟\!\)\u06D4])(?!\s)', r'\1 ', final_output)  # Add space after Arabic punctuation
        final_output = re.sub(r'([\)\]\}»])(?![\s\-])(?!$)', r'\1 ', final_output)  # Add space after closing brackets/quotes
        final_output = re.sub(r'(?<!\s)([\(\«])', r' \1', final_output)  # Add space before opening brackets/quotes
        print(final_output)
    return final_output

def main():
    text_tgfa = "Соҷида Ғуломова дар оилаи ҳунарманд ба дунё омада, хоҳараш Фотима Ғуломова ва бародараш Исфандиёр Ғуломов низ ҳунарпешагони шинохтаи театру синамои тоҷик мебошанд."
    text_fatg = "فعالیت سازمان ملل در مرز ایران و افغانستان به دلیل محدودیت جدید طالبان بر کارمندان زن تعلیق شد"

    print("=== Transliteration 1 (tgfa) ===")
    print(text_tgfa)
    result_tgfa = transliterate(text_tgfa, "tgfa")
    #print(result_tgfa)

    print("=== Transliteration 2 (fatg) ===")
    print(text_fatg)
    result_fatg = transliterate(text_fatg, "fatg")
    #print(result_fatg)


if __name__ == "__main__":
    main()