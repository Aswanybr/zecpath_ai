from parsers.resume_parser import extract_text

def test_resume_parser():
    sample = "sample_resume.pdf"
    result = extract_text(sample)

    assert result is not None