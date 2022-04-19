
import pytest
import os
from common import report_dir, max_fail, rerun


# 实际项目选择使用pytest.ini或main.py
def run():
    html_report = os.path.join(report_dir, 'report.html')
    xml_report = os.path.join(report_dir, 'report.xml')
    pytest.main(["-s", "-v",
                 "--html=" + html_report,
                 "--junit-xml=" + xml_report,
                 "--self-contained-html",
                 "--maxfail", max_fail,
                 "--reruns", rerun])


if __name__ == '__main__':
    run()
