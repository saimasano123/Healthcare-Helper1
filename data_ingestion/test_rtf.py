from rtf_converter import rtf_to_txt

sample_rtf = r"{\rtf1\ansi This is a test.}"
plain_text = rtf_to_txt(sample_rtf)

print("Extracted text:", plain_text)