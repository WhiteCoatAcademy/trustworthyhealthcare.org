/*exported quizJSON */

var quizJSON = {
    'info': {
        'name':    'Phishing Quiz',
        'main':    '<p class="lead">Think you\'re smart enough to not be phished? Take the quiz to find out!</p>',
        'results': '<h5>Learn More</h5><p>Etiam scelerisque, nunc ac egestas consequat, odio nibh euismod nulla, eget auctor orci nibh vel nisi. Aliquam erat volutpat. Mauris vel neque sit amet nunc gravida congue sed sit amet purus.</p>',
        'level1':  'Jeopardy Ready',
        'level2':  'Jeopardy Contender',
        'level3':  'Jeopardy Amateur',
        'level4':  'Jeopardy Newb',
        'level5':  'Stay in school, kid...' // no comma here
    },
    'questions': [
        {
            'q': 'Phishing is an illegal method used by criminals to obtain private information for the purposes of identity or data theft. They utilize fraudulent emails to trick people into submitting their personal information such as social security numbers, passwords, or credit card numbers.',
            'a': [
                {'option': 'True',      'correct': true},
                {'option': 'False',     'correct': false}
            ],
            'correct': '<p><span>That\'s right!</span> Phishing is a form of online identity or data theft in which a scammer sends emails with links to fraudulent websites that are designed to trick you into entering personal data or information such as passwords or credit card numbers. The sender’s email address, the content of the email, and the links in the message will be designed to appear to come from websites you trust, such as your credit card company or employer. The message will request that you provide personal information; however, these links actually take you to fraudulent websites that allow the scammers to obtain your private information and use it maliciously.</p>',
            'incorrect': '<p><span>Nope.</span> Phishing is a form of online identity or data theft in which a scammer sends emails with links to fraudulent websites that are designed to trick you into entering personal data or information such as passwords or credit card numbers. The sender’s email address, the content of the email, and the links in the message will be designed to appear to come from websites you trust, such as your credit card company or employer. The message will request that you provide personal information; however, these links actually take you to fraudulent websites that allow the scammers to obtain your private information and use it maliciously.</p>' // no comma here
        },
        { // Question 2 - Multiple Choice, Multiple True Answers, Select Any
            'q': 'Phishing scammers utilize fraudulent emails to trick people into submitting their personal information such as social security numbers, passwords, or credit card numbers.',
            'a': [
                {'option': 'True',      'correct': true},
                {'option': 'False',     'correct': false}
            ],
            'select_any': true,
            'correct': '<p><span>Nice job!</span> Phishing is a form of online identity or data theft in which a scammer sends emails with links to fraudulent websites that are designed to trick you into entering personal data or information such as passwords or credit card numbers. The sender’s email address, the content of the email, and the links in the message will be designed to appear to come from websites you trust, such as your credit card company or employer. The message will request that you provide personal information; however, these links actually take you to fraudulent websites that allow the scammers to obtain your private information and use it maliciously.</p>',
            'incorrect': '<p><span>Nope.</span> Phishing is a form of online identity or data theft in which a scammer sends emails with links to fraudulent websites that are designed to trick you into entering personal data or information such as passwords or credit card numbers. The sender’s email address, the content of the email, and the links in the message will be designed to appear to come from websites you trust, such as your credit card company or employer. The message will request that you provide personal information; however, these links actually take you to fraudulent websites that allow the scammers to obtain your private information and use it maliciously. </p>'
        },
        { // Question 3 - Multiple Choice, Multiple True Answers, Select All
            'q': 'The validity and trustworthiness of an email can be determined simply based on the sender’s email address.',
            'a': [
                {'option': 'True',      'correct': true},
                {'option': 'False',     'correct': false}
            ],
            'correct': '<p><span>Great!</span> It is easy to make an email appear to be from a different address than that which it truly came from. Therefore, don\’t make assumptions about whether the links in an email are safe simply based on who the email appears to have come from, even if it is your employer.</p>',
            'incorrect': '<p><span>Nope.</span> It is easy to make an email appear to be from a different address than that which it truly came from. Therefore, don\’t make assumptions about whether the links in an email are safe simply based on who the email appears to have come from, even if it is your employer.</p>'
        },
        { // Question 4
            'q': 'Emails asking for your full name, social security number, or password of any kind can be trusted if they appear to be from your employer.',
            'a': [
                {'option': 'True',      'correct': true},
                {'option': 'False',     'correct': false}
            ],
            'correct': '<p><span>Great!</span> All employers should be aware of phishing schemes and the risks they pose. Thus, employers should never ask you for private information via email. To be safe, employers should instruct you to go to the normal log-in website that you regularly use. Go to this website by typing the URL into the web browser yourself. Any legitimate interaction needed by a business or office can then be conducted after accessing your account through the traditional route, not by navigating via links in an email or by sending private information through email.</p>',
            'incorrect': '<p><span>Nope.</span> All employers should be aware of phishing schemes and the risks they pose. Thus, employers should never ask you for private information via email. To be safe, employers should instruct you to go to the normal log-in website that you regularly use. Go to this website by typing the URL into the web browser yourself. Any legitimate interaction needed by a business or office can then be conducted after accessing your account through the traditional route, not by navigating via links in an email or by sending private information through email.</p>'
        },
        { // Question 5
            'q': 'Opening attachments and/or installing software contained in an email is a smart way to assess the safety of an email.',
            'a': [
                {'option': 'True',      'correct': true},
                {'option': 'False',     'correct': false}
            ],
            'correct': '<p><span>Great!</span> It is a safe practice not to open attachments sent to you via email unless you completely trust the sender of an email and are expecting that attachment. Exploring unexpected attachments and/or software linked to emails can be dangerous to your computer as well as the entire network you might be on.</p>',
            'incorrect': '<p><span>Nope.</span> It is a safe practice not to open attachments sent to you via email unless you completely trust the sender of an email and are expecting that attachment. Exploring unexpected attachments and/or software linked to emails can be dangerous to your computer as well as the entire network you might be on.</p>'
        },
        { // Question 6
            'q': 'Clicking on the links in an email is a reliable way to log-in to or access a private account on a website.',
            'a': [
                {'option': 'True',      'correct': true},
                {'option': 'False',     'correct': false}
            ],
            'correct': '<p><span>Great!</span> Especially since most employers, businesses, and governmental offices are aware of phishing schemes and the risks they pose, legitimate emails about private information or an account of yours should instruct you to go to the normal log-in website that you regularly use. Any legitimate interaction needed by business or office can then be conducted after accessing your account through the traditional route, NOT by navigating via links in an email. </p>',
            'incorrect': '<p><span>Nope.</span> Especially since most employers, businesses, and governmental offices are aware of phishing schemes and the risks they pose, legitimate emails about private information or an account of yours should instruct you to go to the normal log-in website that you regularly use. Any legitimate interaction needed by business or office can then be conducted after accessing your account through the traditional route, NOT by navigating via links in an email. </p>'
        }
    ]
};
