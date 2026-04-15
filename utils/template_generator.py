"""
Template generator for Shopify pages with multiple variations in plain text format
Generates random templates to avoid repetition
"""

import random
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
    _legal_notice_indices = None
    _legal_notice_current_index = 0

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
    ]

    ABOUT_US_TEMPLATES = [{
        "name":
        "Story-Driven Classic",
        "content":
        """ABOUT US
================================================================================

Our Journey - From a Simple Idea to a Community-Driven Brand
--------------------------------------------------------------------------------

Hi there! 👋

We're so glad you found us. Welcome to {store_name}, where passion meets purpose, and every product has a story to tell.

It All Started with a Simple Problem
--------------------------------------------------------------------------------

Like most great ideas, {store_name} was born out of frustration. One evening, while searching for something that truly matched our taste and values, we realized that the market was flooded with options that felt… well, generic. Nothing truly spoke to us.

That's when the thought hit:

"Why not create something that resonates, something that feels personal?"

So, with a lot of ambition and a tiny spark of inspiration, we decided to build something different.

A Brand Built on Passion and Purpose
--------------------------------------------------------------------------------

We didn't want to just sell products. We wanted to create experiences, curate items that inspire confidence and reflect personality. Whether it's a cozy hoodie that wraps you in comfort or a stylish gadget that makes life easier, our mission has always been to add value to your daily routine.

But more than just the products, it's about building a community – a space where quality meets authenticity, and where every purchase supports something bigger.

Why Choose Us?
--------------------------------------------------------------------------------

We know that shopping online can feel impersonal. You want to be sure that what you see is what you get. At {store_name}, we promise:

✨ Handpicked Quality: We obsess over every detail, from sourcing to packaging.
💯 Customer First: Your satisfaction is our top priority, and we're always here to listen.
❤️ A Personal Touch: From our curated collections to our friendly support, we put our heart into everything we do.

What Drives Us?
--------------------------------------------------------------------------------

It's simple: People. Passion. Purpose.

We believe in creating something that makes you feel good, not just about the product itself, but about where it comes from and who made it. Our team is a mix of dreamers and doers, committed to making sure every piece we offer adds value to your life.

The Real Difference - You
--------------------------------------------------------------------------------

We wouldn't be here without you. Whether you're a first-time visitor or a returning customer, your support means the world to us. You're the reason we keep pushing forward, innovating, and striving to be better every single day.

Join Our Journey!
--------------------------------------------------------------------------------

Whether it's a story, a suggestion, or a simple hello – we'd love to hear from you at {support_email}!

Thank you for being a part of the {store_name} family. 🎉

Stay connected with us:
{social_links}

Warmly,
The {store_name} Team"""
    }, {
        "name":
        "Modern Minimalist",
        "content":
        """WHO WE ARE
================================================================================

Welcome to {store_name} — where quality meets simplicity.

Our Mission
--------------------------------------------------------------------------------

We believe in thoughtful curation over endless options. Every product in our collection has been carefully selected to meet the highest standards of quality, design, and functionality.

What Makes Us Different
--------------------------------------------------------------------------------

• Curated Selection: Only the best makes it to our store
• Transparent Practices: No hidden fees, no surprises
• Real Support: Actual humans who care about your experience

Our Values
--------------------------------------------------------------------------------

Quality over Quantity — We'd rather offer 10 amazing products than 100 mediocre ones.

Customer-Centric — Your satisfaction isn't just a goal; it's our foundation.

Continuous Improvement — We're always learning, growing, and getting better for you.

================================================================================

Get in Touch
--------------------------------------------------------------------------------

Have questions? Want to share feedback? We're all ears!

📧 Email: {support_email}

Connect with us:
{social_links}

— The {store_name} Team"""
    }, {
        "name":
        "Personal & Friendly",
        "content":
        """👋 HEY THERE! WELCOME TO {store_name}
================================================================================

We're not your typical online store. We're a small team of real people who absolutely love what we do.

How It All Began
--------------------------------------------------------------------------------

Picture this: Late nights, endless brainstorming sessions, and way too much coffee. ☕

That's how {store_name} came to life. We saw a gap in the market — people wanted quality products with genuine service, not just another faceless online transaction.

So we built this. A place where YOU matter, where your experience is everything.

What We're All About
--------------------------------------------------------------------------------

🎯 Real Quality: We test everything ourselves. If we wouldn't use it, we won't sell it.

💬 Honest Communication: No marketing fluff. Just straight talk about our products.

🤝 Customer Love: You're not a ticket number — you're part of our community.

Meet the Team
--------------------------------------------------------------------------------

We're designers, problem-solvers, and product enthusiasts. But most importantly, we're people who care about making your shopping experience awesome.

Our Promise to You
--------------------------------------------------------------------------------

We promise to:
• Always be honest about our products
• Respond to your messages (yes, real humans!)
• Keep improving based on your feedback
• Treat you the way we'd want to be treated

================================================================================

Let's Connect!
--------------------------------------------------------------------------------

Got questions? Ideas? Just want to say hi? We love hearing from you!

✉️ Drop us a line: {support_email}

Follow our journey:
{social_links}

Thanks for being here. Seriously. 💙

— Your friends at {store_name}"""
    }, {
        "name":
        "Professional & Trustworthy",
        "content":
        """ABOUT {store_name}
================================================================================

Company Overview
--------------------------------------------------------------------------------

{store_name} is a leading e-commerce destination committed to delivering exceptional products and outstanding customer service. We've built our reputation on trust, quality, and reliability.

Our Foundation
--------------------------------------------------------------------------------

Founded with a clear vision: to bridge the gap between quality and affordability. We understand that our customers deserve the best, and we work tirelessly to deliver exactly that.

Core Principles
--------------------------------------------------------------------------------

1. Quality Assurance
Every product undergoes rigorous quality checks before reaching your doorstep. We partner with trusted suppliers and manufacturers to ensure consistent excellence.

2. Customer Commitment
Your satisfaction is our primary metric of success. Our dedicated support team is available to assist you throughout your shopping journey.

3. Transparent Operations
We believe in honest business practices. Clear pricing, straightforward policies, and open communication define how we operate.

4. Continuous Excellence
We actively listen to customer feedback and continuously refine our offerings and services.

Why Customers Trust Us
--------------------------------------------------------------------------------

✓ Verified Quality: Stringent quality control processes
✓ Secure Shopping: Protected transactions and data privacy
✓ Responsive Support: Professional assistance when you need it
✓ Fair Policies: Clear terms and customer-friendly returns

================================================================================

Customer Support
--------------------------------------------------------------------------------

Our team is ready to assist you with any inquiries.

Contact Us: {support_email}

Stay connected:
{social_links}

Thank you for choosing {store_name}.

The {store_name} Team"""
    }, {
        "name":
        "Aspirational & Inspiring",
        "content":
        """WELCOME TO {store_name}
================================================================================

✨ Where Dreams Meet Reality
--------------------------------------------------------------------------------

We believe that everyone deserves to feel amazing. That's why we created {store_name} — a place where style, quality, and self-expression come together.

Our Story
--------------------------------------------------------------------------------

It started with a simple belief: You deserve better.

Better products. Better experiences. Better moments.

We watched as people settled for "good enough" when they deserved exceptional. So we set out to change that.

What We Stand For
--------------------------------------------------------------------------------

🌟 Empowerment Through Quality
Every product we offer is chosen to help you feel confident, capable, and amazing.

💎 Excellence as Standard
We don't believe in compromises. Quality isn't a luxury — it's a right.

🌈 Celebrating Uniqueness
Your style is personal. Our collections are curated to help you express your authentic self.

The {store_name} Promise
--------------------------------------------------------------------------------

We promise to inspire you, support you, and deliver products that make a real difference in your daily life.

Because you're not just a customer — you're part of our story.

Join Our Community
--------------------------------------------------------------------------------

Thousands of people have already discovered what makes {store_name} special. Now it's your turn.

• 💝 Exclusive access to new collections
• 🎁 Special offers for community members
• 🌟 Tips, inspiration, and insider updates

================================================================================

Let's Stay Connected
--------------------------------------------------------------------------------

We'd love to hear your story. Reach out anytime!

📬 Email: {support_email}

Follow us for daily inspiration:
{social_links}

Here's to living your best life. ✨

With love,
The {store_name} Team"""
    }, {
        "name":
        "Eco-Conscious & Ethical",
        "content":
        """🌱 ABOUT {store_name}
================================================================================

Shopping with Purpose
--------------------------------------------------------------------------------

At {store_name}, every purchase is a vote for a better world. We're committed to ethical practices, sustainable sourcing, and conscious consumerism.

Our Mission
--------------------------------------------------------------------------------

To prove that you don't have to compromise your values to get quality products. We believe in:

• 🌍 Environmental Responsibility: Sustainable practices at every step
• 🤝 Fair Trade: Supporting ethical suppliers and manufacturers
• ♻️ Minimal Waste: Eco-friendly packaging and operations
• 💚 Conscious Choices: Products that align with your values

What Makes Us Different
--------------------------------------------------------------------------------

Transparency First
We're open about our supply chain, sourcing, and business practices. You deserve to know where your products come from.

Quality That Lasts
We choose durable, well-made products over disposable alternatives. Better for you, better for the planet.

Community Impact
A portion of every purchase supports environmental and social causes. Your shopping makes a real difference.

Join the Movement
--------------------------------------------------------------------------------

When you shop at {store_name}, you're joining thousands of conscious consumers who believe in making better choices.

Together, we're proving that sustainable shopping doesn't have to be complicated.

================================================================================

Get in Touch
--------------------------------------------------------------------------------

Questions about our practices? Want to learn more? We're here!

📧 Contact: {support_email}

Join our community:
{social_links}

Thank you for shopping consciously. 🌿

The {store_name} Team"""
    }, {
        "name":
        "Fun & Quirky",
        "content":
        """🎉 HEY! YOU FOUND US!
================================================================================

Welcome to {store_name} — Where Shopping Meets Fun!
--------------------------------------------------------------------------------

Let's be real: shopping online can be boring. Same old descriptions, same old vibes, same old everything.

Not here! 🚀

Who Are We?
--------------------------------------------------------------------------------

We're the folks who said "enough with boring shopping" and decided to do something about it.

{store_name} is where you'll find:
• 🎁 Products that actually make you smile
• 😊 Real people (not robots) answering your questions
• ✨ A shopping experience that doesn't feel like a chore
• 🎯 Stuff you didn't know you needed (but totally do)

Our Super Scientific Process
--------------------------------------------------------------------------------

Step 1: Find awesome products
Step 2: Test them ourselves
Step 3: Only add them if we'd buy them
Step 4: Share them with you!

See? Told you it was scientific. 😄

Why People Love Shopping Here
--------------------------------------------------------------------------------

💙 We're Actually Fun: Shopping shouldn't be serious all the time

🎪 Cool Stuff: We find products that make life more interesting

🤗 Real Humans: Got questions? Actual people will answer them!

⚡ No BS: We tell it like it is. No marketing mumbo-jumbo.

The {store_name} Vibe
--------------------------------------------------------------------------------

Think of us as your shopping buddy who has great taste and always knows where to find cool stuff.

We're here to make your day a little brighter, your shopping a little easier, and your life a little more fun.

================================================================================

Let's Be Friends!
--------------------------------------------------------------------------------

Seriously, we want to hear from you!

📨 Say hi: {support_email}

Hang out with us online:
{social_links}

Thanks for stopping by! Now go find something awesome. 🎈

Your pals at {store_name}"""
    }, {
        "name":
        "Luxury & Premium",
        "content":
        """{store_name}
================================================================================

Excellence, Curated
--------------------------------------------------------------------------------

Welcome to {store_name} — where discerning taste meets exceptional quality.

Our Philosophy
--------------------------------------------------------------------------------

In a world of mass production and fleeting trends, we offer something rare: timeless quality and refined elegance.

Each item in our collection represents the pinnacle of craftsmanship, design excellence, and enduring value.

The {store_name} Standard
--------------------------------------------------------------------------------

Uncompromising Quality
We work exclusively with premier manufacturers and artisans who share our commitment to excellence. Every detail matters.

Curated Selection
Our collections are thoughtfully assembled for those who appreciate the finer things. Quality, not quantity, defines our approach.

Distinguished Service
Your experience with us should be as exceptional as our products. Our team is dedicated to providing service that exceeds expectations.

Why Choose {store_name}
--------------------------------------------------------------------------------

• 🏆 Premium Quality: Only the finest makes our selection
• 💎 Exclusive Access: Curated collections you won't find everywhere
• 🎯 Expert Curation: Every item carefully selected by specialists
• ⭐ White-Glove Service: Personalized attention to detail

Our Commitment
--------------------------------------------------------------------------------

We are committed to providing an experience worthy of your trust and patronage. From selection to delivery, every touchpoint reflects our dedication to excellence.

================================================================================

Concierge Service
--------------------------------------------------------------------------------

For inquiries and personalized assistance:

📧 {support_email}

Follow us:
{social_links}

Thank you for choosing {store_name}.

Where excellence is standard."""
    }, {
        "name":
        "Tech-Savvy & Innovative",
        "content":
        """⚡ {store_name}
================================================================================

Innovation Meets Commerce
--------------------------------------------------------------------------------

Welcome to {store_name} — where we're redefining online shopping with technology, data, and a customer-first approach.

Our Approach
--------------------------------------------------------------------------------

We leverage cutting-edge technology to deliver:

• 🔍 Smart Curation: AI-powered product recommendations tailored to you
• ⚙️ Seamless Experience: Optimized checkout and lightning-fast delivery
• 📊 Data-Driven Quality: We analyze thousands of data points to ensure excellence
• 🔒 Secure Platform: Bank-level encryption and privacy protection

What Makes Us Different
--------------------------------------------------------------------------------

Tech That Works For You
We use technology to make shopping easier, not more complicated. From intelligent search to personalized recommendations, everything is designed with you in mind.

Continuous Innovation
We're constantly testing new features, improving our platform, and finding better ways to serve you.

Transparent Operations
Real-time order tracking, instant notifications, and full visibility into your shopping journey.

Our Promise
--------------------------------------------------------------------------------

To combine the efficiency of technology with the warmth of human service. You get fast, smart shopping backed by real people who care.

Join the Future of Shopping
--------------------------------------------------------------------------------

Experience what happens when innovation meets customer obsession.

================================================================================

Need Help? We're Here
--------------------------------------------------------------------------------

💬 Live Support: Available in your account dashboard
📧 Email: {support_email}

Stay in the loop:
{social_links}

Welcome to the future of shopping.

— Team {store_name}"""
    }, {
        "name":
        "Family-Owned & Heartfelt",
        "content":
        """❤️ WELCOME TO THE {store_name} FAMILY
================================================================================

A Family Business Built on Love
--------------------------------------------------------------------------------

Hi, we're the folks behind {store_name} — a small, family-owned business that started in our living room and grew with the support of wonderful customers like you.

Our Story
--------------------------------------------------------------------------------

What began as a simple idea around our kitchen table has become something we're incredibly proud of. But here's the thing — we've never forgotten where we started.

Every package we ship, every customer we help, every product we choose — it all comes from the same place: our family to yours.

What Family Means to Us
--------------------------------------------------------------------------------

👨‍👩‍👧‍👦 Personal Touch: We treat every customer like extended family

💝 Care & Attention: Your orders are packed with the same care we'd want for our own loved ones

🤗 Real Relationships: We remember you, we value you, we appreciate you

🏡 Home-Grown Values: Honesty, integrity, and genuine service

Why Choose a Family Business?
--------------------------------------------------------------------------------

When you shop with us, you're not a transaction — you're part of our story.

You're supporting real people, real dreams, and real values. Your purchase helps us send our kids to school, keep our employees happy, and give back to our community.

Our Promise to You
--------------------------------------------------------------------------------

We promise to always:
• Treat you with honesty and respect
• Stand behind everything we sell
• Be here when you need us
• Never forget that you're the reason we can do what we love

================================================================================

We'd Love to Hear from You
--------------------------------------------------------------------------------

Seriously — we read every email, and we love connecting with our customers!

📧 Email us: {support_email}

{social_links}

Thank you for supporting our family business. It means more than you know. 💙

With gratitude,
The {store_name} Family"""
    }, {
        "name": "Disruptive Innovator",
        "content": """🚀 {store_name} - INNOVATION FIRST
================================================================================

Challenging the Status Quo
--------------------------------------------------------------------------------

We're not here to follow trends—we're here to set them. {store_name} was built on the belief that commerce should be smarter, faster, and more customer-centric.

Our Approach: Tech-Driven Excellence
--------------------------------------------------------------------------------

💡 Data-Informed Decisions | ⚡ Rapid Innovation | 🎯 Customer-Obsessed

We leverage cutting-edge technology to deliver products that solve real problems. Every item is vetted through our innovation framework.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Master Craftsman",
        "content": """✨ {store_name} - WHERE CRAFT MEETS PASSION
================================================================================

Handmade with Heart
--------------------------------------------------------------------------------

Every product tells a story. At {store_name}, we celebrate the artisans, the makers, and the craftspeople who pour their soul into their work.

Our Commitment to Quality
--------------------------------------------------------------------------------

🎨 Handpicked Artisans | 🔨 Traditional Techniques | ❤️ Made with Love

We believe in quality that lasts, beauty that endures, and craftsmanship that honors tradition.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Value Champion",
        "content": """{store_name} - QUALITY MEETS AFFORDABILITY
================================================================================

Great Products, Better Prices
--------------------------------------------------------------------------------

We believe everyone deserves access to quality products without breaking the bank. That's why we work tirelessly to bring you the best value possible.

How We Keep Prices Low
--------------------------------------------------------------------------------

💰 Direct Sourcing | 📦 Efficient Operations | 🤝 Fair Partnerships

Smart shopping shouldn't mean compromising on quality.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Wellness Advocate",
        "content": """🌿 {store_name} - YOUR WELLNESS PARTNER
================================================================================

Health is Wealth
--------------------------------------------------------------------------------

At {store_name}, we're passionate about helping you live your healthiest, happiest life. Every product is chosen with your wellbeing in mind.

Our Wellness Philosophy
--------------------------------------------------------------------------------

🍃 Natural Ingredients | 🧘 Holistic Approach | 💚 Sustainable Choices

Your health journey starts here.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Adventure Seeker",
        "content": """⛰️ {store_name} - GEAR FOR THE BOLD
================================================================================

Built for Explorers
--------------------------------------------------------------------------------

Life's an adventure, and we're here to equip you for it. {store_name} curates gear for those who refuse to stay still.

Adventure Awaits
--------------------------------------------------------------------------------

🏔️ Tested in the Wild | 🎒 Adventure-Ready | 🌍 Explore More

Get out there and make memories.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Essential Minimalist",
        "content": """{store_name} - LESS IS MORE
================================================================================

Simplicity by Design
--------------------------------------------------------------------------------

In a world of excess, we choose intention. {store_name} offers carefully curated essentials that enhance your life without cluttering it.

Minimalist Principles
--------------------------------------------------------------------------------

✨ Quality Over Quantity | 🎯 Purpose-Driven | 🖤 Timeless Design

Live simply, live well.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Community First",
        "content": """🤝 {store_name} - POWERED BY COMMUNITY
================================================================================

Together We're Stronger
--------------------------------------------------------------------------------

{store_name} isn't just a store—it's a community. We believe in the power of connection, collaboration, and collective impact.

Our Community Values
--------------------------------------------------------------------------------

👥 People Over Profit | 💬 Open Dialogue | 🌟 Shared Success

Join us and be part of something bigger.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Knowledge Sharer",
        "content": """📚 {store_name} - SHOP SMARTER
================================================================================

Informed Choices, Better Outcomes
--------------------------------------------------------------------------------

We believe knowledge is power. That's why {store_name} goes beyond selling—we educate, inform, and empower our customers.

Learn With Us
--------------------------------------------------------------------------------

📖 Expert Guides | 🎓 Product Education | 💡 Smart Shopping Tips

Make confident, informed decisions.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Global Connector",
        "content": """🌍 {store_name} - CONNECTING CULTURES
================================================================================

Bringing the World to Your Door
--------------------------------------------------------------------------------

{store_name} celebrates diversity by curating products from around the globe. Discover unique items that tell stories from different cultures.

Our Global Mission
--------------------------------------------------------------------------------

🗺️ Worldwide Sourcing | 🎨 Cultural Appreciation | 🤝 Fair Trade

Experience the world through shopping.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Trendsetter",
        "content": """✨ {store_name} - AHEAD OF THE CURVE
================================================================================

Where Trends Are Born
--------------------------------------------------------------------------------

Don't follow trends—set them. {store_name} brings you tomorrow's must-haves today.

Always First
--------------------------------------------------------------------------------

🎯 Trend Forecasting | 🚀 Early Access | 💫 Style Leadership

Be the first to know, the first to own.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Sustainability Champion",
        "content": """♻️ {store_name} - SHOP WITH PURPOSE
================================================================================

Good for You, Good for the Planet
--------------------------------------------------------------------------------

Every purchase at {store_name} is a vote for a sustainable future. We're committed to eco-friendly practices at every step.

Our Green Promise
--------------------------------------------------------------------------------

🌱 Sustainable Materials | 📦 Eco Packaging | 🌍 Carbon Conscious

Shop guilt-free.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Performance Driven",
        "content": """⚡ {store_name} - BUILT TO PERFORM
================================================================================

For Those Who Demand More
--------------------------------------------------------------------------------

Average isn't in our vocabulary. {store_name} delivers high-performance products for high-performing people.

Performance Standards
--------------------------------------------------------------------------------

🏆 Tested & Proven | 💪 Built to Last | 🎯 Results-Focused

Elevate your game.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Nostalgic Curator",
        "content": """🕰️ {store_name} - TIMELESS TREASURES
================================================================================

Bringing Back the Good Old Days
--------------------------------------------------------------------------------

{store_name} celebrates nostalgia with products that remind you of simpler times. Classic quality, vintage charm, modern convenience.

Vintage Vibes, Modern Standards
--------------------------------------------------------------------------------

📻 Retro Inspired | 🎞️ Classic Quality | ❤️ Memory Lane

Relive the magic.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Local Hero",
        "content": """🏘️ {store_name} - PROUDLY LOCAL
================================================================================

Supporting Our Community
--------------------------------------------------------------------------------

{store_name} is rooted in our local community. We source locally, employ locally, and give back locally.

Local Impact
--------------------------------------------------------------------------------

🏠 Community-Owned | 🤝 Local Partnerships | 💚 Neighborhood Pride

Shop local, impact local.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Creative Collective",
        "content": """🎨 {store_name} - WHERE CREATIVITY LIVES
================================================================================

Celebrating Creative Expression
--------------------------------------------------------------------------------

{store_name} is a platform for artists, designers, and creative minds. We showcase products that inspire and delight.

Creative Community
--------------------------------------------------------------------------------

🖌️ Artist Collaborations | 🎭 Unique Designs | ✨ Creative Freedom

Express yourself.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Problem Solver",
        "content": """{store_name} - SOLUTIONS, NOT JUST PRODUCTS
================================================================================

Solving Real Problems
--------------------------------------------------------------------------------

We don't sell products for the sake of it. Every item at {store_name} solves a specific problem or fills a genuine need.

Solution-Focused Approach
--------------------------------------------------------------------------------

🔧 Practical Solutions | 💡 Smart Design | ✅ Real Results

Find your solution here.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Lifestyle Brand",
        "content": """✨ {store_name} - LIVE YOUR BEST LIFE
================================================================================

More Than Products, It's a Lifestyle
--------------------------------------------------------------------------------

{store_name} isn't just about what you buy—it's about how you live. We curate products that enhance your lifestyle.

The {store_name} Lifestyle
--------------------------------------------------------------------------------

🌟 Aspirational Living | 🎯 Curated Collections | 💫 Elevated Everyday

Upgrade your lifestyle.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Tech Enthusiast",
        "content": """💻 {store_name} - FOR THE TECH-SAVVY
================================================================================

Gadgets, Gear, and Innovation
--------------------------------------------------------------------------------

{store_name} is your destination for the latest tech and innovative gadgets. We're as obsessed with technology as you are.

Tech-Forward Selection
--------------------------------------------------------------------------------

🤖 Latest Tech | ⚙️ Smart Gadgets | 🔌 Innovation Hub

Stay ahead of the curve.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Comfort Specialist",
        "content": """☁️ {store_name} - COMFORT IS EVERYTHING
================================================================================

Your Comfort, Our Priority
--------------------------------------------------------------------------------

Life's too short to be uncomfortable. {store_name} specializes in products that make your life cozier, easier, and more comfortable.

Comfort-First Philosophy
--------------------------------------------------------------------------------

🛋️ Ultimate Comfort | 😌 Stress-Free Living | ☁️ Cozy Vibes

Get comfortable.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Gift Expert",
        "content": """🎁 {store_name} - THE PERFECT GIFT AWAITS
================================================================================

Gifting Made Easy
--------------------------------------------------------------------------------

Finding the perfect gift shouldn't be stressful. {store_name} curates thoughtful gifts for every occasion and every person.

Gift-Giving Simplified
--------------------------------------------------------------------------------

🎀 Curated Selections | 💝 Thoughtful Choices | 🎉 Every Occasion

Make someone's day.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Quality Inspector",
        "content": """✅ {store_name} - QUALITY GUARANTEED
================================================================================

Obsessed with Quality
--------------------------------------------------------------------------------

At {store_name}, every product undergoes rigorous quality inspection. We're perfectionists, so you don't have to be.

Quality Control Process
--------------------------------------------------------------------------------

🔍 Thorough Inspection | ✅ Strict Standards | 🏆 Excellence Only

Quality you can trust.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Seasonal Specialist",
        "content": """🍂 {store_name} - CELEBRATING EVERY SEASON
================================================================================

Seasonal Selections
--------------------------------------------------------------------------------

{store_name} brings you the best products for every season. From summer essentials to winter warmers, we've got you covered year-round.

Season by Season
--------------------------------------------------------------------------------

🌸 Spring Fresh | ☀️ Summer Ready | 🍁 Fall Favorites | ❄️ Winter Warmth

Embrace every season.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Budget Optimizer",
        "content": """{store_name} - STRETCH YOUR DOLLAR
================================================================================

Maximum Value, Minimum Spend
--------------------------------------------------------------------------------

{store_name} helps you get more for less. We're experts at finding quality products at prices that won't hurt your wallet.

Smart Shopping Strategies
--------------------------------------------------------------------------------

💵 Best Deals | 🎯 Value Picks | 💰 Budget-Friendly

Shop smarter, save more.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Exclusive Access",
        "content": """👑 {store_name} - MEMBERS ONLY
================================================================================

Exclusive Products, Exclusive Community
--------------------------------------------------------------------------------

{store_name} offers access to products you won't find anywhere else. Join our exclusive community of discerning shoppers.

VIP Benefits
--------------------------------------------------------------------------------

🌟 Exclusive Products | 🎁 Member Perks | 👑 VIP Treatment

Join the elite.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Fast & Efficient",
        "content": """⚡ {store_name} - SPEED IS OUR SPECIALTY
================================================================================

Quick, Easy, Efficient
--------------------------------------------------------------------------------

We know your time is valuable. {store_name} is optimized for speed—fast browsing, quick checkout, rapid delivery.

Efficiency Promise
--------------------------------------------------------------------------------

🚀 Lightning Fast | ⏱️ Time-Saving | ✅ Hassle-Free

Shop in seconds.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Personalization Pro",
        "content": """{store_name} - MADE JUST FOR YOU
================================================================================

Personalized Shopping Experience
--------------------------------------------------------------------------------

One size doesn't fit all. {store_name} offers personalized recommendations and customizable products tailored to your unique needs.

Your Personal Shopper
--------------------------------------------------------------------------------

🎯 Custom Recommendations | ✨ Personalized Service | 💝 Made for You

It's all about you.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Safety First",
        "content": """🛡️ {store_name} - YOUR SAFETY MATTERS
================================================================================

Safe, Secure, Trustworthy
--------------------------------------------------------------------------------

{store_name} prioritizes your safety in every aspect—from secure transactions to safe products to privacy protection.

Safety Standards
--------------------------------------------------------------------------------

🔒 Secure Shopping | ✅ Safety Tested | 🛡️ Privacy Protected

Shop with confidence.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Customer Obsessed",
        "content": """❤️ {store_name} - YOU'RE OUR EVERYTHING
================================================================================

Customer-Centric to the Core
--------------------------------------------------------------------------------

At {store_name}, you're not just a customer—you're the reason we exist. Every decision we make starts with one question: "Is this good for our customers?"

Our Customer Promise
--------------------------------------------------------------------------------

💯 Your Satisfaction | 🎯 Your Needs First | ❤️ Your Happiness

You come first, always.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Transparent Truth",
        "content": """{store_name} - RADICAL TRANSPARENCY
================================================================================

Honest, Open, Transparent
--------------------------------------------------------------------------------

No hidden fees. No fine print. No surprises. {store_name} believes in complete transparency in everything we do.

Our Transparency Pledge
--------------------------------------------------------------------------------

📖 Open Book | 💬 Honest Communication | ✅ No Surprises

What you see is what you get.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Beginner Friendly",
        "content": """{store_name} - PERFECT FOR BEGINNERS
================================================================================

Start Your Journey Here
--------------------------------------------------------------------------------

New to this? Perfect! {store_name} specializes in helping beginners get started with confidence. We make complex simple.

Beginner-Friendly Approach
--------------------------------------------------------------------------------

📚 Easy Guides | 🎓 Learning Resources | 🤝 Patient Support

Everyone starts somewhere.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Expert Authority",
        "content": """{store_name} - TRUSTED BY EXPERTS
================================================================================

Industry-Leading Expertise
--------------------------------------------------------------------------------

{store_name} is recognized by industry experts as the authority in our field. We set the standards others follow.

Expert Credentials
--------------------------------------------------------------------------------

🏆 Industry Recognition | 📊 Proven Track Record | 🎯 Expert-Approved

Trust the experts.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Variety Vault",
        "content": """{store_name} - ENDLESS VARIETY
================================================================================

Something for Everyone
--------------------------------------------------------------------------------

With {store_name}'s vast selection, you'll always find what you're looking for—and discover things you didn't know you needed.

Diverse Selection
--------------------------------------------------------------------------------

🎨 Huge Variety | 🌈 All Styles | 🎯 Every Need

Explore endless possibilities.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Reward Enthusiast",
        "content": """🎁 {store_name} - SHOP & EARN REWARDS
================================================================================

Every Purchase Pays Back
--------------------------------------------------------------------------------

At {store_name}, loyalty pays. Earn rewards, unlock perks, and enjoy exclusive benefits with every purchase.

Rewards Program
--------------------------------------------------------------------------------

⭐ Points on Every Purchase | 🎁 Exclusive Perks | 💝 VIP Benefits

Get rewarded for shopping.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Mobile-First Maven",
        "content": """📱 {store_name} - SHOP ON THE GO
================================================================================

Optimized for Mobile
--------------------------------------------------------------------------------

{store_name} is built for how you actually shop—on your phone, on the go, whenever inspiration strikes.

Mobile Excellence
--------------------------------------------------------------------------------

📱 Mobile-Optimized | ⚡ Fast Loading | 👆 Easy Navigation

Shop anywhere, anytime.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Social Butterfly",
        "content": """💬 {store_name} - JOIN THE CONVERSATION
================================================================================

More Than Shopping, It's Social
--------------------------------------------------------------------------------

{store_name} is where shopping meets social. Share finds, get inspired, and connect with fellow shoppers.

Social Shopping
--------------------------------------------------------------------------------

📸 Share Your Finds | 💬 Community Chat | 🌟 Get Inspired

Shop social.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Green Guardian",
        "content": """🌿 {store_name} - PLANET-POSITIVE SHOPPING
================================================================================

Every Purchase Plants a Tree
--------------------------------------------------------------------------------

{store_name} is committed to environmental stewardship. We offset our carbon footprint and actively contribute to reforestation.

Environmental Commitment
--------------------------------------------------------------------------------

🌳 Carbon Neutral | ♻️ Sustainable Practices | 🌍 Planet-Positive

Shop for a better planet.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Subscription Savvy",
        "content": """{store_name} - SUBSCRIBE & SAVE
================================================================================

Never Run Out Again
--------------------------------------------------------------------------------

{store_name} makes life easier with convenient subscriptions. Get your essentials delivered automatically and save money.

Subscription Benefits
--------------------------------------------------------------------------------

💰 Save on Every Order | 📦 Auto-Delivery | ⏰ Never Forget

Set it and forget it.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Bundle Master",
        "content": """{store_name} - BETTER TOGETHER
================================================================================

Curated Bundles, Better Value
--------------------------------------------------------------------------------

{store_name} creates thoughtful product bundles that save you money and give you everything you need in one click.

Bundle Benefits
--------------------------------------------------------------------------------

💰 Bundle Savings | 🎁 Perfectly Paired | ✅ Complete Solutions

Get more, spend less.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Review Champion",
        "content": """⭐ {store_name} - RATED 5 STARS
================================================================================

Our Customers Love Us
--------------------------------------------------------------------------------

Don't just take our word for it. {store_name} has thousands of 5-star reviews from happy customers just like you.

Customer Reviews
--------------------------------------------------------------------------------

⭐⭐⭐⭐⭐ 5-Star Rated | 💬 Real Reviews | 🏆 Customer Approved

See what others are saying.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Flash Deal Hunter",
        "content": """⚡ {store_name} - DAILY DEALS & FLASH SALES
================================================================================

Don't Miss Out
--------------------------------------------------------------------------------

{store_name} offers exciting flash sales and daily deals. Check back often for limited-time offers on your favorite products.

Deal Alerts
--------------------------------------------------------------------------------

⏰ Flash Sales | 🎯 Daily Deals | 💰 Limited-Time Offers

Catch them while you can.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Curiosity Cultivator",
        "content": """🧐 {store_name} - FEED YOUR CURIOSITY
================================================================================

Discover Something New
--------------------------------------------------------------------------------

At {store_name}, we believe in the joy of discovery. We curate unique, intriguing products that spark curiosity and inspire wonder.

Explore & Learn
--------------------------------------------------------------------------------

✨ Unique Finds | 💡 Inspiring Products | 🌍 World of Discovery

Unleash your inner explorer.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Efficiency Expert",
        "content": """⏱️ {store_name} - MAXIMIZE YOUR TIME
================================================================================

Smart Shopping, Simplified Living
--------------------------------------------------------------------------------

{store_name} is designed to save you time and effort. We offer efficient solutions and products that streamline your life.

Time-Saving Solutions
--------------------------------------------------------------------------------

🚀 Quick Solutions | ✅ Hassle-Free | 🎯 Smart Choices

Reclaim your time.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Empowerment Engine",
        "content": """💪 {store_name} - EMPOWERING YOUR CHOICES
================================================================================

Shop with Confidence & Purpose
--------------------------------------------------------------------------------

{store_name} empowers you to make informed decisions. We provide the tools, knowledge, and products to help you thrive.

Our Empowerment Pledge
--------------------------------------------------------------------------------

💡 Informed Choices | 🚀 Personal Growth | 🌟 Confident Living

Be your best self.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Artisan Advocate",
        "content": """🎨 {store_name} - CELEBRATING ARTISANSHIP
================================================================================

Handcrafted Excellence
--------------------------------------------------------------------------------

{store_name} is a proud advocate for artisans and their craft. We bring you products made with skill, dedication, and passion.

Support True Craft
--------------------------------------------------------------------------------

🖌️ Handcrafted Quality | 🌟 Unique Creations | 🤝 Ethical Sourcing

Invest in artistry.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Future Forward",
        "content": """🔮 {store_name} - SHAPING TOMORROW, TODAY
================================================================================

Innovating for What's Next
--------------------------------------------------------------------------------

{store_name} is constantly looking ahead, bringing you products and ideas that define the future of commerce and lifestyle.

Our Vision
--------------------------------------------------------------------------------

✨ Next-Gen Products | 🚀 Forward Thinking | 🌐 Future-Proof

Step into tomorrow.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Ethical Explorer",
        "content": """🌱 {store_name} - CONSCIOUS CHOICES
================================================================================

Shop with a Conscience
--------------------------------------------------------------------------------

{store_name} is dedicated to ethical sourcing and responsible consumption. Every product has a story you can feel good about.

Our Ethical Promise
--------------------------------------------------------------------------------

🤝 Fair Trade | 💚 Sustainable Practices | 🐾 Cruelty-Free

Make a positive impact.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Joy Spreader",
        "content": """😊 {store_name} - SPREADING JOY, ONE ORDER AT A TIME
================================================================================

Bringing Smiles to Your Doorstep
--------------------------------------------------------------------------------

At {store_name}, our mission is simple: to bring a little more joy into your life with every package you receive.

Our Joyful Approach
--------------------------------------------------------------------------------

✨ Delightful Products | 🎁 Thoughtful Packaging | 😄 Happy Experiences

Find your happy.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Heritage Keeper",
        "content": """📜 {store_name} - PRESERVING TRADITION
================================================================================

Honoring the Past, Crafting the Future
--------------------------------------------------------------------------------

{store_name} celebrates timeless traditions and heritage crafts. We offer products with rich histories and enduring value.

Our Legacy
--------------------------------------------------------------------------------

🕰️ Timeless Designs | 🌍 Cultural Roots | 💎 Enduring Quality

Connect with history.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Simplicity Seeker",
        "content": """⚪ {store_name} - THE BEAUTY OF SIMPLICITY
================================================================================

Uncomplicated Living
--------------------------------------------------------------------------------

{store_name} believes in the power of simplicity. We offer elegant, functional products that enhance your life without complexity.

Simple by Design
--------------------------------------------------------------------------------

Minimalist Aesthetic | ✨ Functional Elegance | 🧘 Peaceful Living

Embrace the simple life.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Dream Weaver",
        "content": """✨ {store_name} - WHERE DREAMS TAKE FLIGHT
================================================================================

Inspiring Your Imagination
--------------------------------------------------------------------------------

{store_name} is more than a store; it's a place where ideas flourish and dreams find their form. Discover products that inspire.

Ignite Your Imagination
--------------------------------------------------------------------------------

💭 Creative Inspiration | 🌟 Aspirational Products | 🚀 Limitless Possibilities

Dream big.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Urban Explorer",
        "content": """🏙️ {store_name} - YOUR URBAN ESSENTIALS
================================================================================

Navigate the City with Style
--------------------------------------------------------------------------------

{store_name} curates products for the modern urbanite. Gear up for city adventures, work, and everything in between.

City-Ready Collection
--------------------------------------------------------------------------------

🚶 Urban Mobility | 💼 Smart Solutions | 🌆 City Style

Conquer the concrete jungle.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Home Haven",
        "content": """🏡 {store_name} - CREATE YOUR SANCTUARY
================================================================================

Making Your House a Home
--------------------------------------------------------------------------------

{store_name} offers everything you need to transform your living space into a personal haven of comfort and style.

Home Sweet Home
--------------------------------------------------------------------------------

🛋️ Cozy Comfort | 🌿 Serene Spaces | 💖 Personal Touches

Love where you live.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Pet Pal",
        "content": """🐾 {store_name} - FOR YOUR FURRY FRIENDS
================================================================================

Happy Pets, Happy Life
--------------------------------------------------------------------------------

At {store_name}, we're as passionate about pets as you are. We offer high-quality products to keep your companions healthy and happy.

Pet-Approved Products
--------------------------------------------------------------------------------

🐶 Cat & Dog Essentials | 🐱 Playful & Practical | ❤️ Pet Wellness

Spoil your best friend.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Parent Partner",
        "content": """👨‍👩‍👧‍👦 {store_name} - SUPPORTING PARENTS
================================================================================

Making Parenthood Easier
--------------------------------------------------------------------------------

{store_name} is here to support parents through every stage. We offer practical, safe, and fun products for your little ones.

Parenting Made Simple
--------------------------------------------------------------------------------

👶 Baby & Kids Gear | ✅ Safety First | 🧸 Fun & Educational

You've got this, parents!

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Student Success",
        "content": """🎓 {store_name} - YOUR STUDY ESSENTIALS
================================================================================

Equipping Minds for Success
--------------------------------------------------------------------------------

{store_name} provides students with the tools they need to excel. From study aids to dorm decor, we've got your academic journey covered.

Student-Focused Solutions
--------------------------------------------------------------------------------

📚 Study Tools | 💡 Learning Aids | 🎒 Campus Life

Achieve your potential.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Fitness Fanatic",
        "content": """🏋️ {store_name} - POWER YOUR WORKOUT
================================================================================

Achieve Your Fitness Goals
--------------------------------------------------------------------------------

{store_name} is your partner in health and fitness. We offer top-tier gear and supplements to help you crush your goals.

Train Hard, Live Strong
--------------------------------------------------------------------------------

💪 Performance Gear | 🍎 Nutrition Support | 🏃 Active Lifestyle

Unleash your strength.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Beauty Boss",
        "content": """💄 {store_name} - UNLEASH YOUR BEAUTY
================================================================================

Radiate Confidence
--------------------------------------------------------------------------------

{store_name} believes true beauty comes from within, but a little help never hurts! Discover products that enhance your natural glow.

Your Beauty Journey
--------------------------------------------------------------------------------

✨ Skincare & Makeup | 💖 Self-Care Essentials | 🌟 Inner Radiance

Shine bright.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Gamer's Paradise",
        "content": """🎮 {store_name} - LEVEL UP YOUR GAME
================================================================================

For Gamers, By Gamers
--------------------------------------------------------------------------------

{store_name} is the ultimate destination for gamers. Find the latest gear, accessories, and collectibles to enhance your play.

Game On!
--------------------------------------------------------------------------------

🕹️ High-Performance Gear | 👾 Collectibles | 🏆 Victory Awaits

Dominate the game.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Bookworm's Nook",
        "content": """📚 {store_name} - YOUR NEXT GREAT READ
================================================================================

Escape into Stories
--------------------------------------------------------------------------------

{store_name} is a sanctuary for book lovers. Discover new worlds, timeless classics, and everything in between.

Literary Adventures
--------------------------------------------------------------------------------

📖 Bestsellers & Classics | 🖋️ Author Spotlights | ☕ Cozy Reading

Turn the page.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Music Maestro",
        "content": """🎶 {store_name} - HARMONY IN EVERY NOTE
================================================================================

Your Soundtrack to Life
--------------------------------------------------------------------------------

{store_name} celebrates the power of music. Find instruments, audio gear, and accessories to create your perfect sound.

Tune In
--------------------------------------------------------------------------------

🎸 Instruments & Gear | 🎧 High-Fidelity Audio | 🎤 Express Yourself

Let the music play.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Foodie's Delight",
        "content": """🍽️ {store_name} - A FEAST FOR THE SENSES
================================================================================

Culinary Adventures Await
--------------------------------------------------------------------------------

{store_name} is a paradise for food lovers. Discover gourmet ingredients, kitchen gadgets, and delicious treats.

Taste the Difference
--------------------------------------------------------------------------------

🌶️ Gourmet Goods | 🔪 Kitchen Essentials | 🥂 Epicurean Delights

Savor every bite.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Travel Companion",
        "content": """✈️ {store_name} - YOUR JOURNEY STARTS HERE
================================================================================

Explore the World with Confidence
--------------------------------------------------------------------------------

{store_name} provides essential gear for every adventurer. Pack smart, travel far, and make unforgettable memories.

Ready for Adventure
--------------------------------------------------------------------------------

🗺️ Travel Essentials | 🎒 Durable Gear | 🌍 Explore More

Wanderlust approved.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Gardener's Oasis",
        "content": """🌱 {store_name} - GROW YOUR GREEN THUMB
================================================================================

Cultivate Your Own Paradise
--------------------------------------------------------------------------------

{store_name} is dedicated to helping your garden flourish. Find tools, seeds, and decor to create your perfect outdoor space.

Green Living
--------------------------------------------------------------------------------

🌻 Gardening Tools | 🌿 Plant Care | 🏡 Outdoor Decor

Blossom with us.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "DIY Dynamo",
        "content": """🛠️ {store_name} - BUILD YOUR DREAMS
================================================================================

Empowering Your Projects
--------------------------------------------------------------------------------

{store_name} is your go-to for all things DIY. From home improvement to creative crafts, we supply the tools and inspiration.

Get Creative
--------------------------------------------------------------------------------

🔨 Tools & Supplies | 💡 Project Ideas | ✨ Craft Your Vision

Make it yourself.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Art Collector",
        "content": """🖼️ {store_name} - CURATING BEAUTY
================================================================================

Discover Your Next Masterpiece
--------------------------------------------------------------------------------

{store_name} brings art into your everyday. Explore unique pieces, prints, and artistic decor that speak to your soul.

Art for Everyone
--------------------------------------------------------------------------------

🎨 Original Art | 🖼️ Unique Prints | ✨ Aesthetic Decor

Adorn your world.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Science Seeker",
        "content": """🔬 {store_name} - EXPLORE THE UNKNOWN
================================================================================

Fueling Scientific Curiosity
--------------------------------------------------------------------------------

{store_name} is for the curious minds and future innovators. Discover educational kits, gadgets, and scientific wonders.

Unravel the Mysteries
--------------------------------------------------------------------------------

🧪 STEM Kits | 🔭 Educational Toys | 💡 Discovery Awaits

Question everything.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Wellness Warrior",
        "content": """🧘 {store_name} - HOLISTIC WELLBEING
================================================================================

Mind, Body, Spirit Harmony
--------------------------------------------------------------------------------

{store_name} supports your journey to holistic wellness. Find products that nourish your mind, body, and spirit.

Balance Your Life
--------------------------------------------------------------------------------

🌿 Natural Remedies | 🧘 Mindfulness Tools | 💖 Self-Care Rituals

Find your center.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Outdoor Enthusiast",
        "content": """🌲 {store_name} - EMBRACE THE WILD
================================================================================

Your Gateway to Nature
--------------------------------------------------------------------------------

{store_name} equips you for every outdoor adventure. From hiking trails to camping trips, we've got your back.

Adventure Awaits
--------------------------------------------------------------------------------

🏕️ Camping Gear | ⛰️ Hiking Essentials | 🛶 Water Sports

Explore beyond limits.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Fashion Forward",
        "content": """👗 {store_name} - YOUR STYLE STATEMENT
================================================================================

Define Your Look
--------------------------------------------------------------------------------

{store_name} brings you the latest trends and timeless pieces to express your unique style. Fashion is personal.

Dress to Impress
--------------------------------------------------------------------------------

👠 Trendy Apparel | 👜 Chic Accessories | ✨ Personal Style

Own your runway.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Collector's Corner",
        "content": """💎 {store_name} - TREASURES FOR THE CURIOUS
================================================================================

Hunt for the Unique
--------------------------------------------------------------------------------

{store_name} is a haven for collectors. Discover rare finds, limited editions, and unique items that complete your collection.

The Thrill of the Find
--------------------------------------------------------------------------------

✨ Rare Collectibles | 🎁 Limited Editions | 🔍 Unique Finds

Expand your collection.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Party Planner",
        "content": """🎉 {store_name} - CELEBRATE EVERYTHING
================================================================================

Make Every Occasion Special
--------------------------------------------------------------------------------

{store_name} helps you throw the perfect party. From decorations to gifts, we've got everything you need to celebrate in style.

Party On!
--------------------------------------------------------------------------------

🎈 Festive Decor | 🎁 Perfect Gifts | 🥳 Event Essentials

Let the good times roll.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Mindful Living",
        "content": """🌸 {store_name} - LIVE WITH INTENTION
================================================================================

Cultivating Peace & Presence
--------------------------------------------------------------------------------

{store_name} offers products that support a mindful lifestyle. Find tools for meditation, relaxation, and conscious living.

Embrace Serenity
--------------------------------------------------------------------------------

🧘 Meditation Aids | 🌿 Natural Wellness | 💖 Inner Peace

Live mindfully.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Eco-Conscious Creator",
        "content": """🌎 {store_name} - CRAFTING A BETTER WORLD
================================================================================

Sustainable Solutions for Creative Minds
--------------------------------------------------------------------------------

{store_name} empowers creators to make a positive impact. Discover eco-friendly materials and tools for sustainable crafting.

Create Responsibly
--------------------------------------------------------------------------------

♻️ Recycled Materials | 🌱 Sustainable Supplies | 🎨 Green Art

Innovate with integrity.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Digital Nomad",
        "content": """💻 {store_name} - WORK FROM ANYWHERE
================================================================================

Your Mobile Office Essentials
--------------------------------------------------------------------------------

{store_name} equips digital nomads for productivity on the go. Find portable tech, ergonomic solutions, and travel-friendly gear.

Freedom to Work
--------------------------------------------------------------------------------

🚀 Portable Tech | 🌐 Connectivity Solutions | 🎒 Travel-Ready

Your office is wherever you are.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Self-Care Sanctuary",
        "content": """🛀 {store_name} - INDULGE IN SELF-CARE
================================================================================

Prioritize Your Wellbeing
--------------------------------------------------------------------------------

{store_name} is your destination for all things self-care. Create your personal sanctuary with products that soothe and rejuvenate.

Rituals of Relaxation
--------------------------------------------------------------------------------

🛁 Bath & Body | 🕯️ Aromatherapy | 💖 Pamper Yourself

You deserve it.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Storyteller's Source",
        "content": """📖 {store_name} - TELL YOUR STORY
================================================================================

Inspiring Narratives, Unique Products
--------------------------------------------------------------------------------

{store_name} believes every product has a story, and every customer has one to tell. Find items that help you express yourself.

Craft Your Narrative
--------------------------------------------------------------------------------

✍️ Creative Tools | 🎭 Expressive Art | 🌟 Personal Expression

Your story, beautifully told.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Wellness Wanderer",
        "content": """🌍 {store_name} - GLOBAL WELLNESS JOURNEY
================================================================================

Discover Health from Around the World
--------------------------------------------------------------------------------

{store_name} curates wellness products inspired by global traditions and natural remedies. Explore ancient secrets for modern health.

World of Wellbeing
--------------------------------------------------------------------------------

🌿 Global Remedies | 🧘 Holistic Practices | ✨ Cultural Wellness

Your passport to health.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Playful Pioneer",
        "content": """🎉 {store_name} - EMBRACE THE FUN
================================================================================

Innovation with a Smile
--------------------------------------------------------------------------------

{store_name} brings a playful spirit to commerce. We offer innovative products that are not just smart, but also spark joy.

Serious Fun
--------------------------------------------------------------------------------

🚀 Playful Tech | 😄 Joyful Discoveries | 💡 Creative Solutions

Where fun meets function.

📧 {support_email}
{social_links}

— {store_name}"""
    }, {
        "name": "Conscious Consumer",
        "content": """💚 {store_name} - SHOP WITH IMPACT
================================================================================

Every Purchase Makes a Difference
--------------------------------------------------------------------------------

{store_name} is for the conscious consumer. We partner with brands committed to ethical production, fair labor, and environmental stewardship.

Your Impact Matters
--------------------------------------------------------------------------------

🤝 Ethical Brands | 🌱 Sustainable Products | 🌍 Positive Change

Shop for a better world.

📧 {support_email}
{social_links}

— {store_name}"""
    }]

    SHIPPING_POLICY_TEMPLATES = [{
        "name":
        "Professional & Transparent",
        "content":
        """SHIPPING POLICY
================================================================================

Thank You for Choosing {store_name}!
--------------------------------------------------------------------------------

We're committed to bringing you high-quality products at the best possible prices. To make this happen, we've strategically positioned our warehouse in Asia, allowing us to reduce costs and pass those savings directly to you.

📦 Shipping Times
--------------------------------------------------------------------------------

We understand that waiting for your order can be exciting (and maybe a little nerve-wracking!). Here's what to expect:

🇺🇸 United States:
Estimated delivery: 7-15 business days
(Business days exclude weekends and holidays)

🌍 International Orders:
Estimated delivery: 9-18 business days
(Timing varies by destination and customs processing)

⏱️ Processing Time
--------------------------------------------------------------------------------

Once your order is placed:
• 1-3 business days for processing and packing
• You'll receive a confirmation email with tracking information
• Track your package every step of the way!

💰 Why Our Pricing Works
--------------------------------------------------------------------------------

Our Asia-based warehouse enables us to:
✓ Offer competitive prices
✓ Work with trusted manufacturers
✓ Maintain quality control at the source
✓ Pass savings to you

📍 Tracking Your Order
--------------------------------------------------------------------------------

We know you're excited! As soon as your order ships, we'll send you a tracking link so you can follow its journey right to your door. 📬

⚠️ Possible Delays
--------------------------------------------------------------------------------

Sometimes external factors may cause slight delays:
• Customs processing
• Weather conditions
• Global shipping disruptions

We truly appreciate your patience and understanding during these times.

================================================================================

💬 Questions About Your Order?
--------------------------------------------------------------------------------

Our friendly support team is here to help!

📧 Email: {support_email}

Follow our journey:
{social_links}

Thank you for being part of the {store_name} family. Your support means everything to us! ❤️

Warm wishes,
The {store_name} Team"""
    }, {
        "name":
        "Customer-Friendly & Clear",
        "content":
        """🚚 SHIPPING INFORMATION
================================================================================

How We Deliver Your Order
--------------------------------------------------------------------------------

At {store_name}, we work hard to get your products to you quickly and safely. Here's everything you need to know!

Delivery Times
--------------------------------------------------------------------------------

United States 🇺🇸
• ⏰ 7-15 business days
• 📅 Business days = Monday-Friday (excluding holidays)
• 📦 Free tracking included

International 🌎
• ⏰ 9-18 business days
• 🛃 May require customs clearance
• 📦 Full tracking provided

Order Processing
--------------------------------------------------------------------------------

What Happens After You Order:

Day 1-3: We carefully pack your order
Day 3: Your package ships out
Day 3+: You get tracking information
Day 7-15: Your order arrives! 🎉

Why Shipping Takes Time
--------------------------------------------------------------------------------

Great question! Here's the honest truth:

Our warehouse is located in Asia, which allows us to:
• 💰 Offer lower prices (no middleman!)
• ✅ Ensure quality control at the source
• 🌟 Work directly with manufacturers

The trade-off? Slightly longer shipping times. But we believe the savings and quality make it worthwhile!

Track Your Package
--------------------------------------------------------------------------------

We'll send you a tracking number as soon as your order ships. You can check its status anytime!

What If There's a Delay?
--------------------------------------------------------------------------------

Sometimes things happen:
• 🛃 Customs inspections
• 🌧️ Weather issues
• 🚛 Carrier delays

If your order seems delayed, reach out to us — we'll track it down!

================================================================================

Need Help?
--------------------------------------------------------------------------------

Questions about your shipment? We're here!

📧 {support_email}

Stay connected:
{social_links}

Thanks for shopping with us! 😊

— {store_name}"""
    }, {
        "name":
        "Detailed & Comprehensive",
        "content":
        """SHIPPING & DELIVERY POLICY
================================================================================

Overview
--------------------------------------------------------------------------------

Thank you for choosing {store_name}. This policy outlines our shipping procedures, delivery times, and what you can expect when ordering from us.

📦 Shipping Methods & Times
--------------------------------------------------------------------------------

Domestic Shipping (United States)

Processing Time: 1-3 business days
Transit Time: 7-15 business days
Total Time: 8-18 business days
Tracking: ✓ Included

International Shipping

Processing Time: 1-3 business days
Transit Time: 9-18 business days
Customs Clearance: 2-7 days (varies)
Tracking: ✓ Included

Note: Business days = Monday-Friday, excluding public holidays

🏭 Our Warehouse Location
--------------------------------------------------------------------------------

Our fulfillment center is strategically located in Asia for several important reasons:

• Cost Efficiency: Direct access to manufacturers = lower prices for you
• Quality Control: We oversee production and quality at the source
• Product Selection: Access to wider range of products and suppliers
• Better Pricing: Savings we pass directly to our customers

📋 Order Processing
--------------------------------------------------------------------------------

Step-by-Step Process:

1. Order Received
You receive an order confirmation email immediately

2. Processing (1-3 days)
Your order is verified, packed, and prepared for shipment

3. Shipment
Package is handed to our shipping carrier

4. Tracking Sent
You receive tracking information via email

5. In Transit
Your package travels to your location

6. Delivery
Package arrives at your doorstep!

📍 Tracking Your Order
--------------------------------------------------------------------------------

Once shipped, you'll receive:
• ✉️ Email with tracking number
• 🔗 Direct link to carrier tracking page
• 📱 Regular status updates

⚠️ Potential Delays
--------------------------------------------------------------------------------

While we strive for timely delivery, these factors may cause delays:

Customs Processing:
International shipments must clear customs. This typically takes 2-7 days but can vary.

Weather Conditions:
Severe weather may temporarily halt shipping operations.

Peak Seasons:
Holidays and peak shopping periods may extend delivery times.

Address Issues:
Incorrect or incomplete addresses can cause delays. Please verify your shipping information!

🌍 International Orders
--------------------------------------------------------------------------------

Important Notes:
• You may be responsible for customs duties and taxes
• These fees are set by your country and are not included in our prices
• Customs processing times vary by country
• Refused shipments may incur return fees

================================================================================

💬 Need Assistance?
--------------------------------------------------------------------------------

Our support team is ready to help with any shipping questions:

📧 Email: {support_email}
⏰ Response Time: Within 24 hours

Please include your order number when contacting us!

Connect with us:
{social_links}

================================================================================

Thank you for your patience and for choosing {store_name}. We're committed to delivering quality products and excellent service.

The {store_name} Team"""
    }, {
        "name":
        "Honest & Straightforward",
        "content":
        """LET'S TALK SHIPPING
================================================================================

The Honest Truth About Our Delivery
--------------------------------------------------------------------------------

We believe in being 100% transparent with you. Here's exactly how our shipping works.

⏰ How Long Will It Take?
--------------------------------------------------------------------------------

Short answer:
• 🇺🇸 USA: 7-15 business days
• 🌍 International: 9-18 business days

Long answer:

After you order, we need 1-3 days to process and pack your order (we're thorough!). Then your package ships from our warehouse in Asia.

Yes, Asia. Here's why...

🌏 Why Ship From Asia?
--------------------------------------------------------------------------------

We're going to be straight with you:

Our warehouse is in Asia because it allows us to offer you better prices.

By working directly with manufacturers and handling logistics ourselves, we cut out multiple middlemen. The savings? We pass them to you.

The trade-off: Shipping takes longer than Amazon Prime.

The benefit: You pay less for the same (or better) quality.

We think it's worth it. We hope you do too!

📦 What Happens After You Order
--------------------------------------------------------------------------------

Day 1: We get your order (exciting!)
Days 1-3: We pack it carefully
Day 3: It ships out
Days 4-18: It travels to you
Day 7-18: It arrives! 🎉

🔍 Can I Track My Order?
--------------------------------------------------------------------------------

Yes! As soon as your package ships, you'll get:
• 📧 An email with your tracking number
• 🔗 A link to track your package
• 📱 Updates as it moves

❓ What If It's Delayed?
--------------------------------------------------------------------------------

Sometimes packages get held up by:
• Customs (they're thorough too)
• Weather (we can't control Mother Nature)
• Carrier delays (they're only human)

If your order seems stuck, email us. We'll investigate and get you answers.

================================================================================

Still Have Questions?
--------------------------------------------------------------------------------

We're real people who actually read and respond to emails!

📧 {support_email}

Follow us:
{social_links}

Thanks for understanding our shipping process. We promise the wait is worth it!

— The {store_name} Team"""
    }, {
        "name":
        "Visual & Engaging",
        "content":
        """🚚 YOUR ORDER'S JOURNEY
================================================================================

From Our Warehouse to Your Doorstep
--------------------------------------------------------------------------------

Ever wondered what happens after you click "Order"? Let us show you! 📦

🗺️ The Journey
--------------------------------------------------------------------------------

📍 START: Our Warehouse (Asia)
        ⬇️
📦 STEP 1: Packing (Days 1-3)
Your order is carefully checked, packed, and labeled
        ⬇️
✈️ STEP 2: Takeoff!
Package is handed to international carrier
        ⬇️
🛃 STEP 3: Customs Check
Quick security inspection (nothing personal!)
        ⬇️
🚛 STEP 4: Local Delivery
Transferred to local carrier in your country
        ⬇️
🏠 FINISH: Your Address!
Happy unboxing! 🎉

⏱️ Timeline
--------------------------------------------------------------------------------

Destination  |  Processing  |  Shipping  |  Total
🇺🇸 USA      |  1-3 days    |  7-15 days |  8-18 days
🌍 International | 1-3 days | 9-18 days | 10-21 days

💡 Why Asia?
--------------------------------------------------------------------------------

Great question! Here's the breakdown:

✅ Direct from Source = Lower costs
✅ Quality Control = We oversee everything
✅ Better Prices = Savings passed to you
✅ Wider Selection = More products available

⏰ Longer Shipping = The only trade-off

📱 Tracking Your Package
--------------------------------------------------------------------------------

Stay updated every step of the way!

You'll receive:
• 📧 Tracking email when your order ships
• 🔗 Direct link to tracking page
• 📍 Real-time location updates

⚠️ Heads Up!
--------------------------------------------------------------------------------

Sometimes delays happen:

🛃 Customs: Usually quick, sometimes slow
🌧️ Weather: Mother Nature's rules
📅 Holidays: Everyone takes breaks
🚛 High Volume: Peak season traffic

Don't worry — we'll keep you updated!

================================================================================

Questions? We're Here!
--------------------------------------------------------------------------------

📧 Email us: {support_email}
💬 We respond within 24 hours!

Stay in touch:
{social_links}

Thank you for choosing {store_name}! 💙

The {store_name} Team"""
    }, {
        "name":
        "Reassuring & Supportive",
        "content":
        """SHIPPING POLICY - WE'VE GOT YOU COVERED
================================================================================

Your Order is in Good Hands
--------------------------------------------------------------------------------

We understand that ordering online requires trust. At {store_name}, we take that trust seriously. Here's everything you need to know about how we'll get your order to you safely.

📦 What to Expect
--------------------------------------------------------------------------------

For US Customers:
• ⏰ Delivery in 7-15 business days
• 📧 Tracking information provided
• 📦 Secure, protective packaging
• ✅ Quality checked before shipping

For International Customers:
• ⏰ Delivery in 9-18 business days
• 📧 Full tracking included
• 🛃 Customs forms completed by us
• 🌍 Worldwide shipping available

Why We Ship From Asia
--------------------------------------------------------------------------------

We want to be upfront with you: our warehouse is located in Asia. This isn't a secret or something we hide — it's actually a strategic advantage that benefits you.

Here's how:

💰 Better Prices: Working directly with manufacturers means no markups
✨ Quality Control: We're at the source, ensuring standards are met
🎯 Product Selection: Access to products not easily available elsewhere
🤝 Direct Relationships: Better communication with makers

Yes, shipping takes a bit longer. But we believe the combination of quality and value makes it worthwhile.

We Keep You Informed
--------------------------------------------------------------------------------

You'll never wonder where your order is:

✉️ Order Confirmation — Immediate
📦 Shipping Notification — Within 3 days
📍 Tracking Updates — Throughout delivery
📬 Delivery Confirmation — When it arrives

If Something Goes Wrong
--------------------------------------------------------------------------------

We hope your delivery goes perfectly. But if it doesn't, we're here to help.

📧 Email us at {support_email}

We will:
✓ Track down your package
✓ Investigate any delays
✓ Work with carriers on your behalf
✓ Find a solution that works for you

Your Patience = Your Savings
--------------------------------------------------------------------------------

We know waiting isn't fun. But here's what your patience gets you:

• Better prices than retail stores
• Direct-from-source quality
• Products you might not find elsewhere
• Support for a business that values you

We think it's a fair trade. We hope you do too!

================================================================================

We're Here for You
--------------------------------------------------------------------------------

Questions? Concerns? Just want an update?

📧 {support_email}
⏰ We respond to every email within 24 hours

Connect with us:
{social_links}

Thank you for trusting {store_name} with your order. We won't let you down.

With appreciation,
The {store_name} Team"""
    }]

    LEGAL_NOTICE_TEMPLATES = [
        {
            "name": "Standard Legal Notice",
            "content": """LEGAL NOTICE / IMPRESSUM
================================================================================

Information provided according to legal requirements.

Company Information
--------------------------------------------------------------------------------
Store Name: {store_name}
Address: {company_address}
Phone: {phone_number}
Email: {support_email}

Legal Representatives
--------------------------------------------------------------------------------
{store_name} is represented by its management team. 
For specific legal inquiries, please contact our support team.

[Dispute Resolution|Online Dispute Resolution|EU Dispute Resolution]
--------------------------------------------------------------------------------
The European Commission provides a platform for online dispute resolution (OS), which you can find at https://ec.europa.eu/consumers/odr. We are [neither obliged nor willing|not obligated] to participate in a dispute settlement procedure before a consumer arbitration board.

Liability for Content
--------------------------------------------------------------------------------
As a service provider, we are responsible for our own content on these pages according to the general laws. However, we are not obligated to monitor transmitted or stored third-party information or to investigate circumstances that indicate illegal activity.

Liability for Links
--------------------------------------------------------------------------------
Our offer contains links to external, third-party websites, the contents of which we have no influence on. Therefore, we cannot assume any liability for these external contents. The respective provider or operator of the pages is always responsible for the content of the linked pages.

Copyright
--------------------------------------------------------------------------------
The content and works created by the site operators on these pages are subject to copyright law. The duplication, processing, distribution, and any kind of exploitation outside the limits of copyright require the written consent of the respective author or creator.
"""
        },
        {
            "name": "Minimal Legal Information",
            "content": """LEGAL INFORMATION
================================================================================

Business Details
--------------------------------------------------------------------------------
Store/Company Name: {store_name}
Registered Address: {company_address}

Contact Details
--------------------------------------------------------------------------------
Email Address: {support_email}
Telephone: {phone_number}

Social Media: 
{social_links}

[Disclaimer|Liability Disclosure]
--------------------------------------------------------------------------------
The information provided on this website is for general informational purposes only. We [strive to keep the information up to date|make every effort to provide accurate details] but make no warranties of any kind about the completeness or accuracy of the website content.

Intellectual Property
--------------------------------------------------------------------------------
All materials within this website are the intellectual property of {store_name}. These materials may not be copied or reproduced without our written permission.
"""
        },
        {
            "name": "Corporate Impressum",
            "content": """IMPRESSUM & LEGAL NOTICE
================================================================================

This Legal Notice is intended to provide the necessary transparency regarding the ownership and operation of {store_name}.

Company Details
--------------------------------------------------------------------------------
Operating Entity: {store_name}
Headquarters Address: {company_address}
Contact Phone: {phone_number}
Support Email: {support_email}

[Copyright Notice|Intellectual Property Rights]
--------------------------------------------------------------------------------
Copyright © {store_name}. All rights reserved. 
The text, images, graphics, sound files, animation files, video files and their arrangement on our Internet sites are all subject to Copyright and other intellectual property protection. 

Trademarks
--------------------------------------------------------------------------------
Unless otherwise indicated, all marks displayed on {store_name} internet sites are subject to trademark rights, including its corporate logos and emblems.

Disclaimer of Warranty
--------------------------------------------------------------------------------
We provide all [information and content|data and details] "as is" and without warranties of any kind, whether express or implied.
"""
        },
        {
            "name": "E-commerce Standard Legal",
            "content": """LEGAL NOTICE
================================================================================

Welcome to the Legal Notice page of {store_name}.

Contact Information
--------------------------------------------------------------------------------
If you have any questions, concerns, or requests regarding our store or products, feel free to reach out to us at:
• Email: {support_email}
• Phone: {phone_number}
• Mail: {company_address}

Follow Us:
{social_links}

Business Licensing & Registration
--------------------------------------------------------------------------------
{store_name} operates as an e-commerce retailer. We comply with all applicable online retail [regulations|laws] and data protection directives.

Website Terms of Use
--------------------------------------------------------------------------------
By accessing this website, you [agree to be bound by|accept] these website Terms and Conditions of Use, all applicable laws and regulations, and agree that you are responsible for compliance with any applicable local laws.

Content Liability
--------------------------------------------------------------------------------
While we [work hard to ensure|do our best to maintain] transparency and accuracy, {store_name} cannot be held liable for typographical errors or omissions relating to product descriptions, pricing, and availability.
"""
        },
        {
            "name": "Global Retail Legal Notice",
            "content": """LEGAL INFORMATION & IMPRESSUM
================================================================================

About Us
--------------------------------------------------------------------------------
{store_name} is an international e-commerce platform dedicated to providing quality {niche_name} to our customers worldwide.

Company Identity
--------------------------------------------------------------------------------
Trade Name: {store_name}
Corporate Address: {company_address}
Contact Email: {support_email}
Customer Support Line: {phone_number}

Regulatory Compliance
--------------------------------------------------------------------------------
Depending on your region, different consumer protection laws apply. We respect and [comply fully|adhere completely] with the relevant e-commerce trade laws, including transparent pricing, return rights, and data privacy regulations.

Copyright and Trademarks
--------------------------------------------------------------------------------
All [content included on this site|website material], such as text, graphics, logos, button icons, images, and software, is the property of {store_name} or its content suppliers and protected by international copyright laws.
"""
        }
    ]

    @classmethod
    def _get_next_about_us_index(cls):
        """Get next About Us template index using shuffle-based rotation"""
        # Initialize indices on first call
        if cls._about_us_indices is None:
            cls._about_us_indices = list(range(len(cls.ABOUT_US_TEMPLATES)))
            random.shuffle(cls._about_us_indices)
            cls._about_us_current_index = 0
        
        # Check if we've completed a full cycle
        if cls._about_us_current_index >= len(cls._about_us_indices):
            # Reshuffle for next cycle
            random.shuffle(cls._about_us_indices)
            cls._about_us_current_index = 0
        
        # Get current index and increment
        index = cls._about_us_indices[cls._about_us_current_index]
        cls._about_us_current_index += 1
        
        return index
    
    @classmethod
    def _parse_spintax(cls, text: str) -> str:
        if not text:
            return ""
        pattern = re.compile(r'\[([^\[\]]*?\|[^\[\]]*?)\]')
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

        content = template["content"].format(store_name=store_name,
                                             support_email=support_email,
                                             social_links=formatted_social,
                                             niche_name=formatted_niche)

        content = cls._parse_spintax(content)
        return {"template_name": template["name"], "content": content}

    @classmethod
    def _get_next_shipping_policy_index(cls):
        """Get next Shipping Policy template index using shuffle-based rotation"""
        # Initialize indices on first call
        if cls._shipping_policy_indices is None:
            cls._shipping_policy_indices = list(range(len(cls.SHIPPING_POLICY_TEMPLATES)))
            random.shuffle(cls._shipping_policy_indices)
            cls._shipping_policy_current_index = 0
        
        # Check if we've completed a full cycle
        if cls._shipping_policy_current_index >= len(cls._shipping_policy_indices):
            # Reshuffle for next cycle
            random.shuffle(cls._shipping_policy_indices)
            cls._shipping_policy_current_index = 0
        
        # Get current index and increment
        index = cls._shipping_policy_indices[cls._shipping_policy_current_index]
        cls._shipping_policy_current_index += 1
        
        return index
    
    @classmethod
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
        return {"template_name": template["name"], "content": content}

    @classmethod
    def _get_next_legal_notice_index(cls):
        """Get next Legal Notice template index using shuffle-based rotation"""
        if cls._legal_notice_indices is None:
            cls._legal_notice_indices = list(range(len(cls.LEGAL_NOTICE_TEMPLATES)))
            random.shuffle(cls._legal_notice_indices)
            cls._legal_notice_current_index = 0
            
        if cls._legal_notice_current_index >= len(cls._legal_notice_indices):
            random.shuffle(cls._legal_notice_indices)
            cls._legal_notice_current_index = 0
            
        index = cls._legal_notice_indices[cls._legal_notice_current_index]
        cls._legal_notice_current_index += 1
        return index

    @classmethod
    def get_random_legal_notice_template(cls, store_name: str,
                                         support_email: str,
                                         social_links: str = "",
                                         niche_name: str = "",
                                         company_address: str = "",
                                         phone_number: str = "") -> dict:
        """Get a non-repeating Legal Notice template using shuffle-based rotation"""
        index = cls._get_next_legal_notice_index()
        template = cls.LEGAL_NOTICE_TEMPLATES[index]

        formatted_social = social_links.strip() if social_links and social_links.strip() else "[Your social media links]"
        formatted_niche = niche_name if niche_name else "products"
        
        if company_address and company_address.strip():
            # Replace tabs or multiple consecutive spaces with a comma and space
            # Example: "509 BYRUM RD\tCHAPARRAL\tNM\t88081" -> "509 BYRUM RD, CHAPARRAL, NM, 88081"
            clean_addr = re.sub(r'\s*\t\s*|\s{2,}', ', ', company_address.strip())
            formatted_address = clean_addr.title() if clean_addr.islower() else clean_addr
        else:
            formatted_address = "[Your Company Address]"
        formatted_phone = phone_number.strip() if phone_number and phone_number.strip() else "[Your Phone Number]"

        content = template["content"].format(store_name=store_name,
                                             support_email=support_email,
                                             social_links=formatted_social,
                                             niche_name=formatted_niche,
                                             company_address=formatted_address,
                                             phone_number=formatted_phone)

        content = cls._parse_spintax(content)
        return {"template_name": template["name"], "content": content}

    @classmethod
    def generate_all_templates(cls, store_name: str,
                               support_email: str,
                               social_links: str = "",
                               niche_name: str = "",
                               company_address: str = "",
                               phone_number: str = "") -> dict:
        """Generate all policies including About Us, Shipping Policy, and Legal Notice"""
        about_us = cls.get_random_about_us_template(
            store_name, support_email, social_links, niche_name)
        shipping = cls.get_random_shipping_policy_template(
            store_name, support_email, social_links, niche_name)
        legal = cls.get_random_legal_notice_template(
            store_name, support_email, social_links, niche_name, company_address, phone_number)

        return {
            'about_us': about_us['content'],
            'about_us_template': about_us['template_name'],
            'shipping_policy': shipping['content'],
            'shipping_policy_template': shipping['template_name'],
            'legal_notice': legal['content'],
            'legal_notice_template': legal['template_name']
        }
