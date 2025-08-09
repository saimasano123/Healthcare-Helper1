import re

def rtf_to_txt(rtf):
	# Simple extraction: remove RTF formatting for basic cases
	text = re.sub(r'{\\rtf1\\ansi\s*', '', rtf)
	text = re.sub(r'[{}\\]', '', text)
	return text.strip()

sample_rtf = r"{\rtf1\ansi This is a test.}"
plain_text = rtf_to_txt(sample_rtf)

print("Extracted text:", plain_text)