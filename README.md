python-antispam
============

Prevents spam in your python web apps. Cloud features allow you to use additional anti-spam functionality. Cloud features allow you to use additional anti-spam functionality, such as: Personal IP/Email lists, blocking by country, language, stop words and etc.

Spam attacks log - allows to view all filtered requests in the "Log of spam attacks".
The log contains a detailed information about each request for a time period. At any time, you can check the request and make sure that the filtering is correct. A Python API for antispam service cleantalk.org. Invisible protection from spam, no captches, no puzzles, no animals and no math.

## How API stops spam?
API uses several simple tests to stop spammers.
  * Spam bots signatures.
  * Blacklists checks by Email, IP, web-sites domain names.
  * JavaScript availability.
  * Comment submit time.
  * Relevance test for the comment.

## How API works?
API sends a comment's text and several previous approved comments to the servers. Servers evaluates the relevance of the comment's text on the topic, tests on spam and finaly provides a solution - to publish or put on manual moderation of comments. If a comment is placed on manual moderation, the plugin adds to the text of a comment explaining the reason for the ban server publishing.

## Requirements

   * Python 2.6 and above
   * Python 3 and above 
   * CleanTalk account https://cleantalk.org/register?product=anti-spam

## SPAM test for text comment sample 

```python
from cleantalk import CleanTalk


ct = CleanTalk(auth_key='yourkey')
ct_result = ct.request(
                message = 'abc', # Visitor comment
                sender_ip = '196.19.250.114', # Visitor IP address
                sender_email = 'stop_email@example.com', # Visitor email
                sender_nickname = 'spam_bot', # Visitor nickname
                # event_token = 'xxx' # fill it with ct_bot_detector_event_token hidden input from your form (auto generate)
        )
#Check
if ct_result['allow']:
    print('Comment allowed. Reason ' + ct_result['comment'])
else:
    print('Comment blocked. Reason ' + ct_result['comment'])
```

## API Response description
API returns Python dictionary object, where keys:
  * allow (0|1) - allow to publish or not, in other words spam or ham
  * comment (string) - server comment for requests.
  * id (string MD5 HEX hash) - unique request idenifier.

## Installing via PyPi
Run the next command in the terminal:

```python
pip install cleantalk-python-antispam
```
Then you can use Cleantalk class import:
```python
from cleantalk_python_antispam.cleantalk import CleanTalk
```

For improve protection include javascript to your layout before \<\/body\> tag:
```html
<script type="text/javascript" src="https://moderate.cleantalk.org/ct-bot-detector-wrapper.js"></script>
```

## Changelog
Version 1.2
  * New. Now page URL could be added to the request.
  * Mod. Tests file updated.
  * Mod. Readme updated.
