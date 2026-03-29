"""
Compact template generator - creates 100 diverse templates from metadata
This approach is more maintainable and avoids massive file sizes
"""

import random

# Template builders for About Us
def build_about_us_startup(name, store_name, support_email, social_links):
    """Build startup/innovation themed About Us"""
    templates = {
        "Disruptive Innovator": f"""🚀 {store_name.upper()} - DISRUPTING THE STATUS QUO
================================================================================

We're Not Your Average Store
--------------------------------------------------------------------------------

At {store_name}, we saw an industry stuck in the past and decided to shake things up. We're here to challenge conventions, break molds, and deliver products that actually make sense for modern life.

Our Innovation-First Approach
--------------------------------------------------------------------------------

💡 Think Different: We question everything and improve constantly
⚡ Move Fast: Agile development means rapid improvements
🎯 User-Focused: Your feedback drives our roadmap
🔬 Test & Learn: We iterate based on real data

Why We're Different
--------------------------------------------------------------------------------

Traditional stores sell products. We build solutions.

We leverage technology, data analytics, and customer insights to curate a selection that evolves with your needs. Every product is vetted through our innovation framework.

Join the Revolution
--------------------------------------------------------------------------------

Be part of something bigger. Early adopters get exclusive access to new features and products.

📧 {support_email}
{social_links}

— The {store_name} Team""",

        "Tech-First Pioneer": f"""⚡ WELCOME TO {store_name}
================================================================================

Where Technology Meets Commerce
--------------------------------------------------------------------------------

We're pioneers in the digital-first shopping experience. Leveraging AI, machine learning, and cutting-edge e-commerce tech to bring you a smarter way to shop.

Our Tech Stack
--------------------------------------------------------------------------------

🤖 AI-Powered Recommendations
📊 Data-Driven Curation  
🔒 Bank-Level Security
⚡ Lightning-Fast Checkout

The {store_name} Difference
--------------------------------------------------------------------------------

We're not just selling products—we're building the future of retail. Every click, every purchase helps us refine our algorithms to serve you better.

Innovation in Action
--------------------------------------------------------------------------------

• Real-time inventory optimization
• Predictive shipping estimates
• Personalized shopping journeys
• Seamless omnichannel experience

📧 {support_email}
{social_links}

Welcome to the future.

— {store_name}"""
    }
    return templates.get(name, templates["Disruptive Innovator"])

# Save this as a reference - we'll integrate into main file
print("Template builder functions created")
print("Next: Integrate into template_generator.py")
