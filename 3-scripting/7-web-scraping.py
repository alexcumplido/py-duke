# Web scraping
# HTML Parsing
# APIs
# Unstructured data
# JSON
# Normalization
# Persisting data
# XML Extensible Markup Language
# CSV Comma Separated Values

from html.parser import HTMLParser

content = """
<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>1992 World Junior Championships in Athletics – Men's high jump - Wikipedia</title>
"""

content = """
<tr>
    <td>EXPLOIT-DB-10168</td>
    <td><a href="http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-47672" target="_blank">CVE-2009-47672</a></td>
</tr>
<tr>
    <td>EXPLOIT-DB-20245</td>
    <td><a href="http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-12345" target="_blank">CVE-2011-12345</a></td>
</tr>
<tr>
    <td>EXPLOIT-DB-30487</td>
    <td><a href="http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-67890" target="_blank">CVE-2015-67890</a></td>
</tr>
<tr>
    <td>EXPLOIT-DB-40598</td>
    <td><a href="http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-54321" target="_blank">CVE-2017-54321</a></td>
</tr>
<tr>
    <td>EXPLOIT-DB-50932</td>
    <td><a href="http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13579" target="_blank">CVE-2020-13579</a></td>
</tr>
"""

class Parser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.recording = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.recording = True
        elif tag == "a":
            self.recording = True
        else:
            self.recording = False
            
    def handle_data(self, data):
       if self.recording:
            print(f"Found data for tag: {repr(data)}")
            self.recording = False
            
parser = Parser()

parser.feed(content)
quit()
with open("./1992_World_Junior_Championships_in_Athletics_–_Men's_high_jump.txt") as _file:
    parser.feed(_file.read())

# print(p.title)