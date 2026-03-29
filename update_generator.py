import os
import sys

file_path = os.path.join("utils", "template_generator.py")
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add import re and variables
target1 = '''import random


class PageTemplateGenerator:
    """Generate customized Shopify page templates in plain text format with non-repeating rotation"""
    
    # Class variables for rotation tracking
    _about_us_indices = None
    _about_us_current_index = 0
    _shipping_policy_indices = None
    _shipping_policy_current_index = 0'''

repl1 = '''import random
import re


class PageTemplateGenerator:
    """Generate customized Shopify page templates in plain text format with non-repeating rotation"""
    
    # Class variables for rotation tracking
    _about_us_indices = None
    _about_us_current_index = 0
    _fashion_about_us_indices = None
    _fashion_about_us_current_index = 0
    _shipping_policy_indices = None
    _shipping_policy_current_index = 0

    FASHION_ABOUT_US_TEMPLATES = [
        {
            "name": "Women's Fashion Core",
            "content": """[WELCOME TO|HELLO AND WELCOME TO|GREETINGS FROM] {store_name}
================================================================================

[Empowering Women Through Style|Style That Empowers|Confidence You Can Wear]
--------------------------------------------------------------------------------

[We believe that|Our philosophy is that|To us,] {niche_name} is [more than just fabric|not just about clothes|much more than apparel]—it's confidence you can wear. Welcome to {store_name}, your destination for [stylish, comfortable, and empowering fashion|chic, everyday apparel|clothing that makes you feel amazing].

[Our Story|How We Started|Our Journey]
--------------------------------------------------------------------------------

It started with a simple [problem|realization|frustration]: most women's fashion forces you to choose between feeling comfortable and looking great. We decided to bridge that gap. We curate {niche_name} that [fit beautifully|enhance your figure|look stunning], feel amazing, and keep up with your busy life.

[Why Choose Us?|What Makes Us Different|Our Commitment]
--------------------------------------------------------------------------------

✨ [Carefully Curated|Thoughtfully Selected|Handpicked Quality]: We handpick every item to ensure it meets our [quality standards|high expectations].
✨ [Designed for Real Women|Made to Flatter|True Fit]: We stock styles that flatter, inspire, and elevate everyday wardrobes.
✨ [Customer First|You Come First|Dedicated Support]: Your satisfaction is our [top priority|main focus].

[Get in Touch|Contact Us|Let's Connect]
--------------------------------------------------------------------------------

📧 Email: {support_email}

[Stay connected with us|Follow our journey|Join our community]:
{social_links}

[Warmly|With love|Best regards],
The {store_name} Team"""
        },
        {
            "name": "Women's Fashion - Trendy & Chic",
            "content": """[HELLO GORGEOUS!|HI THERE!|WELCOME BEAUTIFUL!] WELCOME TO {store_name}
================================================================================

[Your New Wardrobe Obsession|The Closet Upgrade You Needed|Fresh Styles Delivered]
--------------------------------------------------------------------------------

[Ready to upgrade your closet?|Looking for something new?|Time for a wardrobe refresh?] We're {store_name}, and we're [obsessed with|passionate about] bringing you the [latest trends|freshest looks] in {niche_name} without the luxury markup.

[What We're All About|Our Mission|Who We Are]
--------------------------------------------------------------------------------

We noticed that finding [high-quality, trendy|stylish, durable|fashion-forward] {niche_name} was either too expensive or too confusing. So we [simplified it|changed the game]. We curate seasonal collections that make dressing up (or dressing down) the easiest part of your day.

[Our Promise|Why Shop With Us|What To Expect]
--------------------------------------------------------------------------------

🎯 [Trend-Forward|Always Searching]: We stay ahead of the curve so you don't have to.
💎 [Quality Materials|Premium Fabrics]: Beautiful fabrics that look and feel premium.
🤝 [Genuine Support|Here to Help]: Got sizing questions? We're here to help!

[Let's Connect!|Say Hello!|Reach Out]
--------------------------------------------------------------------------------

[Got questions or want to show off your new look?|Need help finding your size?]

✉️ Drop us a line: {support_email}

[Follow our journey and tag us|Stay in the loop]:
{social_links}

[Stay fabulous!|Keep glowing!|Shine on!]
— [Your friends at|With love from] {store_name}"""
        },
        {
            "name": "Women's Fashion - Timeless Elegance",
            "content": """[THE {store_name} EXPERIENCE|DISCOVER {store_name}|WELCOME TO {store_name}]
================================================================================

[Timeless Elegance in Every Thread|Classic Styles That Endure|Sophistication Meets Comfort]
--------------------------------------------------------------------------------

Welcome to {store_name}, a sanctuary for those who appreciate refined {niche_name}. We believe in building a wardrobe that outlasts [fleeting trends|short-lived fads].

[Our Philosophy|What Drives Us|The Heart of Our Brand]
--------------------------------------------------------------------------------

[True style is eternal|Elegance never fades]. We carefully curate a versatile selection of {niche_name} designed to be the [foundation of your personal style|cornerstone of your closet]. Every piece is selected for its classic silhouette, superior drape, and endless wearability.

[The {store_name} Standard|Our Commitment to Quality|Why We Stand Out]
--------------------------------------------------------------------------------

• [Quality First|Uncompromising Quality]: We prioritize excellent craftsmanship and durable fabrics.
• [Versatility|Day-to-Night Wear]: Pieces that transition effortlessly from day to night.
• [Dedicated Service|Personalized Care]: We treat every customer with the utmost care.

[Connect With Us|Get In Touch|Reach Out]
--------------------------------------------------------------------------------

[For styling advice or order inquiries:|Need help?]

📧 {support_email}

[Follow us:|Join us on social:]
{social_links}

[Thank you for choosing {store_name}.|We're glad you're here.]"""
        }
    ]'''

content = content.replace(target1, repl1)


# 2. Update get_random_about_us_template and add parser
target2 = '''    @classmethod
    def get_random_about_us_template(cls, store_name: str,
                                     support_email: str,
                                     social_links: str = "") -> dict:
        """Get a non-repeating About Us template using shuffle-based rotation"""
        # Get next template using rotation
        index = cls._get_next_about_us_index()
        template = cls.ABOUT_US_TEMPLATES[index]

        # Format social links - use provided links or placeholder
        if social_links and social_links.strip():
            formatted_social = social_links.strip()
        else:
            formatted_social = "[Your social media links]"

        content = template["content"].format(store_name=store_name,
                                             support_email=support_email,
                                             social_links=formatted_social)

        return {"template_name": template["name"], "content": content}'''

repl2 = '''    @classmethod
    def _parse_spintax(cls, text: str) -> str:
        if not text:
            return ""
        pattern = re.compile(r'\\[([^\\[\\]]*?\\|[^\\[\\]]*?)\\]')
        while True:
            match = pattern.search(text)
            if not match:
                break
            options = match.group(1).split('|')
            replacement = random.choice(options)
            text = text[:match.start()] + replacement + text[match.end():]
        return text

    @classmethod
    def _get_next_fashion_about_us_index(cls):
        if cls._fashion_about_us_indices is None:
            cls._fashion_about_us_indices = list(range(len(cls.FASHION_ABOUT_US_TEMPLATES)))
            random.shuffle(cls._fashion_about_us_indices)
            cls._fashion_about_us_current_index = 0
        if cls._fashion_about_us_current_index >= len(cls._fashion_about_us_indices):
            random.shuffle(cls._fashion_about_us_indices)
            cls._fashion_about_us_current_index = 0
        index = cls._fashion_about_us_indices[cls._fashion_about_us_current_index]
        cls._fashion_about_us_current_index += 1
        return index

    @classmethod
    def get_random_about_us_template(cls, store_name: str,
                                     support_email: str,
                                     social_links: str = "",
                                     niche_name: str = "") -> dict:
        """Get a non-repeating About Us template using shuffle-based rotation"""
        is_fashion = "women" in niche_name.lower() or "fashion" in niche_name.lower() or "clothing" in niche_name.lower() or "apparel" in niche_name.lower()
        
        if is_fashion:
            index = cls._get_next_fashion_about_us_index()
            template = cls.FASHION_ABOUT_US_TEMPLATES[index]
        else:
            index = cls._get_next_about_us_index()
            template = cls.ABOUT_US_TEMPLATES[index]

        if social_links and social_links.strip():
            formatted_social = social_links.strip()
        else:
            formatted_social = "[Your social media links]"
            
        formatted_niche = niche_name if niche_name else "our beautiful products"

        # Note: older universal templates might not have {niche_name} in them.
        # Python's .format() throws KeyError only if a {} parameter is MISSING in kwargs.
        # If kwargs has extra values, it doesn't fail.
        content = template["content"].format(store_name=store_name,
                                             support_email=support_email,
                                             social_links=formatted_social,
                                             niche_name=formatted_niche)

        content = cls._parse_spintax(content)
        return {"template_name": template["name"], "content": content}'''

content = content.replace(target2, repl2)


# 3. Update get_random_shipping_policy_template
target3 = '''    @classmethod
    def get_random_shipping_policy_template(cls, store_name: str,
                                            support_email: str,
                                            social_links: str = "") -> dict:
        """Get a non-repeating Shipping Policy template using shuffle-based rotation"""
        # Get next template using rotation
        index = cls._get_next_shipping_policy_index()
        template = cls.SHIPPING_POLICY_TEMPLATES[index]

        # Format social links - use provided links or placeholder
        if social_links and social_links.strip():
            formatted_social = social_links.strip()
        else:
            formatted_social = "[Your social media links]"

        content = template["content"].format(store_name=store_name,
                                             support_email=support_email,
                                             social_links=formatted_social)

        return {"template_name": template["name"], "content": content}'''

repl3 = '''    @classmethod
    def get_random_shipping_policy_template(cls, store_name: str,
                                            support_email: str,
                                            social_links: str = "",
                                            niche_name: str = "") -> dict:
        """Get a non-repeating Shipping Policy template using shuffle-based rotation"""
        index = cls._get_next_shipping_policy_index()
        template = cls.SHIPPING_POLICY_TEMPLATES[index]

        if social_links and social_links.strip():
            formatted_social = social_links.strip()
        else:
            formatted_social = "[Your social media links]"

        formatted_niche = niche_name if niche_name else "our beautiful products"

        content = template["content"].format(store_name=store_name,
                                             support_email=support_email,
                                             social_links=formatted_social,
                                             niche_name=formatted_niche)

        content = cls._parse_spintax(content)
        return {"template_name": template["name"], "content": content}'''

content = content.replace(target3, repl3)

# 4. Update generate_both_templates
target4 = '''    @classmethod
    def generate_both_templates(cls, store_name: str,
                                support_email: str,
                                social_links: str = "") -> dict:
        """Generate both templates with non-repeating rotation selection"""
        about_us = cls.get_random_about_us_template(
            store_name, support_email, social_links)
        shipping = cls.get_random_shipping_policy_template(
            store_name, support_email, social_links)

        return {
            'about_us': about_us['content'],
            'about_us_template': about_us['template_name'],
            'shipping_policy': shipping['content'],
            'shipping_policy_template': shipping['template_name']
        }'''

repl4 = '''    @classmethod
    def generate_both_templates(cls, store_name: str,
                                support_email: str,
                                social_links: str = "",
                                niche_name: str = "") -> dict:
        """Generate both templates with non-repeating rotation selection"""
        about_us = cls.get_random_about_us_template(
            store_name, support_email, social_links, niche_name)
        shipping = cls.get_random_shipping_policy_template(
            store_name, support_email, social_links, niche_name)

        return {
            'about_us': about_us['content'],
            'about_us_template': about_us['template_name'],
            'shipping_policy': shipping['content'],
            'shipping_policy_template': shipping['template_name']
        }'''
content = content.replace(target4, repl4)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully processed {file_path}")
