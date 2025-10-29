"""
Template generator for Shopify pages with multiple variations in plain text format
Generates random templates to avoid repetition
"""

import random


class PageTemplateGenerator:
    """Generate customized Shopify page templates in plain text format"""

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

    @staticmethod
    def get_random_about_us_template(store_name: str,
                                     support_email: str,
                                     social_links: str = "") -> dict:
        """Get a random About Us template"""
        template = random.choice(PageTemplateGenerator.ABOUT_US_TEMPLATES)

        # Format social links - use provided links or placeholder
        if social_links and social_links.strip():
            formatted_social = social_links.strip()
        else:
            formatted_social = "[Your social media links]"

        content = template["content"].format(store_name=store_name,
                                             support_email=support_email,
                                             social_links=formatted_social)

        return {"template_name": template["name"], "content": content}

    @staticmethod
    def get_random_shipping_policy_template(store_name: str,
                                            support_email: str,
                                            social_links: str = "") -> dict:
        """Get a random Shipping Policy template"""
        template = random.choice(
            PageTemplateGenerator.SHIPPING_POLICY_TEMPLATES)

        # Format social links - use provided links or placeholder
        if social_links and social_links.strip():
            formatted_social = social_links.strip()
        else:
            formatted_social = "[Your social media links]"

        content = template["content"].format(store_name=store_name,
                                             support_email=support_email,
                                             social_links=formatted_social)

        return {"template_name": template["name"], "content": content}

    @staticmethod
    def generate_both_templates(store_name: str,
                                support_email: str,
                                social_links: str = "") -> dict:
        """Generate both templates with random selection"""
        about_us = PageTemplateGenerator.get_random_about_us_template(
            store_name, support_email, social_links)
        shipping = PageTemplateGenerator.get_random_shipping_policy_template(
            store_name, support_email, social_links)

        return {
            'about_us': about_us['content'],
            'about_us_template': about_us['template_name'],
            'shipping_policy': shipping['content'],
            'shipping_policy_template': shipping['template_name']
        }
