# Python Anti-Spam & Bot Filter by CleanTalk — No CAPTCHA/reCaptcha Needed
============

Invisible spam protection for your Python apps — no CAPTCHA/reCaptcha, no puzzles, no math.

Spam attacks log - allows to view all filtered requests in the "Log of spam attacks".
The log contains a detailed information about each request for a time period. At any time, you can check the request and make sure that the filtering is correct. A Python API for antispam service cleantalk.org. Invisible protection from spam, no captches, no puzzles, no animals and no math.

## Why CleanTalk?
Tired of distorted images, puzzles with traffic lights, or invisible zebras?
Here’s how CleanTalk compares:

| Feature                         | CAPTCHA                          | CleanTalk                              |
|---------------------------------|----------------------------------|----------------------------------------|
| User Experience                 | Interrupts with puzzles, images  | Completely invisible                    |
| Setup Complexity                | Medium to High                   | Easy integration with Python API       |
| Mobile Usability                | Often frustrating                | Seamless experience                    |
| Accessibility (e.g. screenreaders) | Limited                       | Fully accessible                       |
| Spam Protection Method          | Challenge-based (user solves)    | Behavior-based (bot detection, JS, IP) |
| Requires User Interaction       | ✅ Yes                            | ❌ No                                   |
| Supports Form Relevance Checks | ❌ No                             | ✅ Yes                                  |


## How API works?
CleanTalk uses multiple layers of protection:

- Spam bot signatures
- Blacklist checks (email, IP, domain)
- JavaScript presence
- Submission time analysis
- Comment relevance scoring
- 
## Requirements

- Python 2.6+
- Python 3.x
- CURL support
- CleanTalk account — [Sign up here](https://cleantalk.org/register?product=anti-spam)

## SPAM test for text comment sample 

```python
from cleantalk import CleanTalk
import json


ct = CleanTalk(auth_key='yourkey')
ct_result = ct.request(
                message = 'abc', # Required. Visitor comment
                sender_ip = '196.19.250.114', # Required. Visitor IP address
                sender_email = 'stop_email@example.com', # Required. Visitor email
                sender_nickname = 'spam_bot', # Required. Visitor nickname
                post_info= json.dumps({'post_url': 'https://yoursite.com'}) # Optional. Additional post info in JSON format.
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
<script type="text/javascript" src="https://fd.cleantalk.org/ct-bot-detector-wrapper.js"></script>
```

## Changelog
Version 1.2
  * New. Now page URL could be added to the request.
  * Mod. Tests file updated.
  * Mod. Readme updated.
