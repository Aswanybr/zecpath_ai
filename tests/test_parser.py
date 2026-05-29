from parsers.resume_parser import extract_text

def test_resume_parser():

    sample = "data/resumes/resume1.pdf"

    result = extract_text(sample)

    assert result is not None