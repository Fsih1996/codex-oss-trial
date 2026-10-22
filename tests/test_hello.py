from datetime import date

import hello


def test_prints_greeting_and_today(capsys):
    hello.main()
    out = capsys.readouterr().out
    assert "Hello from codex-oss-trial!" in out
    assert date.today().isoformat() in out
