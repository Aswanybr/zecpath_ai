from parsers.text_cleaner import clean_resume_text

def test_clean_text():

    sample = "SKILLS\n\nPython    Java"

    cleaned = clean_resume_text(sample)

    assert "Python Java" in cleaned