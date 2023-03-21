from setuptools import setup
import codecs

long_description = b"cleantalk_python_antispam\n===============\n\nA Python API for antispam service cleantalk.org. Invisible protection from spam, no captches, no puzzles, no animals and no math.\n\n## How API stops spam?\nAPI uses several simple tests to stop spammers.\n- Spam bots signatures.\n- Blacklists checks by Email, IP, web-sites domain names.\n- JavaScript availability.\n- Comment submit time.\n- Relevance test for the comment.\n\n## How API works?\nAPI sends a comment's text and several previous approved comments to the servers. Servers evaluates the relevance of the comment's text on the topic, tests on spam and finaly provides a solution - to publish or put on manual moderation of comments. If a comment is placed on manual moderation, the plugin adds to the text of a comment explaining the reason for the ban server publishing.\n\n## Requirements\n\n- Python 2.6 and above\n- Python 3 and above \n\n## SPAM test for text comment sample \n\n```python\nfrom cleantalk import CleanTalk\n\n\nct = CleanTalk(auth_key='yourkey')\nct_result = ct.request(\n\tmessage = 'abc', # Visitor comment\n\tsender_ip = '196.19.250.114', # Visitor IP address\n\tsender_email = 'stop_email@example.com', # Visitor email\n\tsender_nickname = 'spam_bot', # Visitor nickname\n\tjs_on = 1, # Is visitor has JavaScript\n\tsubmit_time = 12 # Seconds from start form filling till the form POST\n)\n#Check\nif ct_result['allow']:\n\tprint('Comment allowed. Reason ' + ct_result['comment'])\n\t\n\tprint('Comment blocked. Reason ' + ct_result['comment'])\n```\n\n## API Response description\nAPI returns Python dictionary object, where keys:\n- allow (0|1) - allow to publish or not, in other words spam or ham\n- comment (string) - server comment for requests.\n- id (string MD5 HEX hash) - unique request idenifier.\n  \n## Installing via PyPi\nRun the next command in the terminal:\n```python\npip install cleantalk-python-antispam\n```\nThen you can use Cleantalk class import:\n```python\nfrom cleantalk_python_antispam.cleantalk import CleanTalk\n```"
long_description = codecs.decode(long_description, 'ASCII')

setup(name='cleantalk_python_antispam',
      version='1.2.0',
      description='CleanTalk module for Python',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['cleantalk_python_antispam'],
      author_email='plugins@cleantalk.org',
      zip_safe=False)


